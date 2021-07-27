# Avatar Modifications To Chatbot Widget Documentation

As this is demo code most of the code for this part comes from [this project](https://github.com/JiteshGaikwad/Chatbot-Widget). The code from this project takes care of the frontend and user interface interaction. The avatar is implemented using [botlibre](https://www.botlibre.org/) especially the [avatar functionality of the javascript SDK](https://www.botlibre.com/forum-post?id=682689). The following subsections contains documentation for individual files (only the ones that were modified). For running this code refer to /user_interaction_demo/Chatbot-Widget/README.md. 

In the future consider creating your own API similar to that of botlibre using the Wave2Lip model and voice_cloning code (you could also use voice code from IBM and google although they are still in experimental stage) in this repo.

**Note:** The avatar appears only after the first message (this is to reduce initial load time and not to annoy users who aren't willing to use the chat functionality, this behaviour can be easily modified).


## /user_interaction_demo/Chatbot-Widget/scripts/sdk.js

This code includes botlibre SDK. Make sure to modify the code to use your API key (create an account on the botlibre site and you can find it in your user profile).

## /user_interaction_demo/Chatbot-Widget/index.html

Just modified it to include the botlibre SDK. Make sure to include it before including the modules from the static folder.

## /user_interaction_demo/Chatbot-Widget/static/js/components/chat.js

In lines 38 to 43 we create instance of the SDK and avatar. In line 104 we utilize the avatar instance to speak the message.
