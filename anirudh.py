import numpy as np
from scipy import signal
from PIL import Image


def load_image(path):
    img = np.asarray(Image.open(path))/255.0
    return img

def save(path, img):
    tmp = np.asarray(img*255.0, dtype=np.uint8)
    Image.fromarray(tmp).save(path)

def denoise_image(inp):
    # estimate 'background' color by a median filter
    bg = signal.medfilt2d(inp, 11)
    save('background.png', bg)

    # compute 'foreground' mask as anything that is significantly darker than
    # the background
    mask = inp < bg - 0.1
    save('foreground_mask.png', mask)

    # return the input value for all pixels in the mask or pure white otherwise
    return np.where(mask, inp, 1.0)

image = Image.open('image.jpg')
image = image.convert('L') # convert image to grayscale
new_image = image.resize((832, 536))  
new_image.save('image.jpg')
inp_path = 'image.jpg'
out_path = 'output.jpg'

inp = load_image(inp_path)
out = denoise_image(inp)

save(out_path, out)
