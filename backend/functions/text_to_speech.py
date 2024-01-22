import requests
from dotenv import load_dotenv
import os
from pathlib import Path
from openai import OpenAI
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def openai_convert_text_to_speech(assistant_message):
    client = OpenAI()

    response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input=assistant_message
    )

    return response



#eleven labs 
# convert text to speech

# def convert_text_to_speech(message):

#     body = {
#         'text': message,
#         'voice_settings': {
#             'stability': 0,
#             'similarity_boost': 0
#         }
#     }

#     voice_rachel = '21m00Tcm4TlvDq8ikWAM'


#     # constructing endpoint
#     headers = {'xi-api-key': ELEVEN_LABS_API_KEY,
#                'Content-Type': 'applications/json',
#                'accept': 'audio/mpeg'}

#     endpoint = f'https://api.elevenlabs.io/v1/text-to-speech/{voice_rachel}'

#     #send request
#     try:
#         response = requests.post(endpoint, json=body, headers=headers)
#     except Exception as e:
#         return
    
#     # handle response
#     if response.status_code == 200:
#         return response.content
#     else:
#         return
