import requests
from dotenv import load_dotenv
import os
load_dotenv()

ELEVEN_LABS_API_KEY = os.getenv("ELEVEN_LABS_API_KEY")

#eleven labs 
# convert text to speech

def convert_text_to_speech(message):

    body = {
        'text': message,
        'voice_settings': {
            'stability': 0,
            'similarity_boost': 0
        }
    }

    voice_rachel = '21m00Tcm4TlvDq8ikWAM'


    # constructing endpoint
    headers = {'xi-api-key': ELEVEN_LABS_API_KEY,
               'Content-Type': 'applications/json',
               'accept': 'audio/mpeg'}

    endpoint = f'https://api.elevenlabs.io/v1/text-to-speech/{voice_rachel}'

    #send request
    try:
        response = requests.post(endpoint, json=body, headers=headers)
    except Exception as e:
        return
    
    # handle response
    if response.status_code == 200:
        return response.content
    else:
        return
