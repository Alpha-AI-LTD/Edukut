# User Interaction Demo

This code is intended only as a demo of how the avatar works.

# TODO

1. Modify the code to use the Wav2Lip model instead of the botlibre SDK for the avatar.

2. Tweak the frontend UI (you could also consider using botfront's webchat widget or any other alternative).

3. Change the SDK application id, if you are continuing to use botlibre SDK.

# Instructions

* Run any rasa bot using the command. This enables the REST API for interacting with the rasa bot as well.

```
rasa run -m models --enable-api --cors "*" --debug
```

* Then open the Chatbot-Widget/index.html in a browser.
