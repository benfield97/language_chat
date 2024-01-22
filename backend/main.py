# uvicorn main:app
# uvicorn main:app --reload


from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai
from dotenv import load_dotenv
import os

#custom function imports 
from functions.openai_requests import convert_audio_to_text
from functions.openai_requests import get_chat_response
from functions.database import store_messages, reset_messages
from functions.text_to_speech import convert_text_to_speech

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
# initialize app
app = FastAPI()


# CORS  - Origins
origins = [
    'http://localhost:5173',
    'http://localhost:5174',
    'http://localhost:4173',
    'http://localhost:4174',
    'http://localhost:3000',
]

# CORS - middleware 
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/health')
async def check_health():
    return {'message': 'healthy'}

@app.get('/reset')
async def reset_conversation():
    reset_messages()
    return {'message': 'conversation reset'}

# # post bot response
# # Note: Not playing in browser when using post request
# @app.post('/post-audio')
# async def post_audio(file: UploadFile = File(...)):
#     print('hello')

@app.get('/post-audio')
async def get_audio():

    #get saved audio
    audio_file = open('voice.mp3', 'rb')

    # decode audio
    message_decoded = convert_audio_to_text(audio_file)
    
    # gurard: ensure message decoded
    if not message_decoded:
        return  HTTPException(status_code=400, detail='failed to decode audio')
    
    #get chat response
    chat_response = get_chat_response(message_decoded)

    #guard: ensure chat response

    if not chat_response:
        return HTTPException(status_code=400, detail='failed to get chat response')

    store_messages(message_decoded, chat_response)
    print(chat_response)

    # convert chat response to audio
    audio_output = convert_text_to_speech(chat_response)

    # guard: ensure audio output
    if not audio_output:
        return HTTPException(status_code=400, detail='failed to get audio output')
    
    # create a generator that yields chunks of data
    def iterfile():
        yield audio_output


    #return audiofile
    return StreamingResponse(iterfile(), media_type='audio/mpeg')


