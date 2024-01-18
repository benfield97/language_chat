# uvicorn main:app
# uvicorn main:app --reload


from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai

#custom function imports 
from functions.openai_requests import convert_audio_to_text
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
    print(message_decoded)
    return 'done'

