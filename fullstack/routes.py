import os,re
from app import app
from flask import render_template,url_for,redirect,request,flash
import urllib.request
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = 'C:/static/uploads/'


 
app.secret_key = "yogesh-pal"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

 

     
 
@app.route("/")
@app.route("/Text")
def view_text_page():
    return render_template("Text.html", title=" Text Page")
  
@app.route("/Customize")
def uploader():
        path = 'C:/static/uploads/'
        uploads = sorted(os.listdir(path), key=lambda x: os.path.getctime(path+x))        # Sorting as per image upload date and time
        print(uploads)
        #uploads = os.listdir('static/uploads')
        uploads = ['uploads/' + file for file in uploads]
        uploads.reverse()
        return render_template("Customize.html",uploads=uploads)            # Pass filenames to front end for display in 'uploads' variable

@app.route('/Avatar', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No photo selected for uploading')
        return redirect(request.url)
    else:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #print('upload_image filename: ' + filename)
        return render_template('/', filename=filename)
  


@app.route("/Avatar")
def view_avatar_page():
    return render_template("Avatar.html", title="Avatar page")


 

@app.route("/Customize")
def view_customize_page():
    return render_template("Customize.html", title="Customize page")