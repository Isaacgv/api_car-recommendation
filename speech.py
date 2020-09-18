import json, os
from io import BytesIO
from base64 import b64decode
from cgi import parse_multipart, parse_header
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core.authenticators import BasicAuthenticator

# Basic Authentication with Watson STT API
    
stt_authenticator = BasicAuthenticator(
        'apikey',
        'yH2qmAtMsfapTdFSh12-MgcGoZ9z17SC-rFfY5VCaenz'
)

# Construct a Watson STT client with the authentication object
stt = SpeechToTextV1(
        authenticator=stt_authenticator
    )

# Set the URL endpoint for your Watson STT client
stt.set_service_url(
        'https://api.us-south.speech-to-text.watson.cloud.ibm.com'
)


def recive_audio(audio_file_):


    # Build flac file from stream of bytes
    fo = open("audio_sample.flac", 'wb')
    fo.write(audio_file_.read())
    fo.close()


    with open(
        os.path.join(
            os.path.dirname(__file__), './.',
            'audio_sample.flac'
        ), 'rb'
    ) as audio_file:
        #audio_source = AudioSource(audio_file)
        stt_result = stt.recognize(
            audio=audio_file,
            content_type='audio/flac',
            model='pt-BR_BroadbandModel',
	    ).get_result()
    #pt-BR_NarrowbandModel
    #print(json.dumps(stt_result, indent=2))

    text_tr = stt_result['results'][0]['alternatives'][0]['transcript']
    
    return text_tr
