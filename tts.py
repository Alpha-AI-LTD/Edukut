from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
apikey = 'iE78fxOoTE05nUiWO-bEAlEIUzzzwlPTTsvf3SdersEq'
url = 'https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/28dcc33d-d70a-4065-94bc-c69894cf70e4'
# Setup Service
authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)
with open('sample.txt', 'r') as f:
    text = f.readlines()
text = [line.replace('\n','') for line in text]
text = ''.join(str(line) for line in text)
with open('./sample.mp3', 'wb') as audio_file:
    res = tts.synthesize(text, accept='audio/mp3', voice='en-GB_JamesV3Voice').get_result()
    audio_file.write(res.content)
