from openai import OpenAI
from decouple import config
from dotenv import load_dotenv
import json
import os
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()


#import custom functions
from functions.database import get_recent_messages

#conveert audio to text
def convert_audio_to_text(audio_file):
    try: 
        transcript = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file
            )
        message_text = transcript.text
        return message_text
    
    except Exception as e:
        print(e)
        return 
    
# openai chatgpt
#get response to message
def get_chat_response(message_input):
    client = OpenAI()

    messages = get_recent_messages()
    user_message = {'role': 'user',
                    
                    'content': message_input}
    messages.append(user_message)
    print(messages)

    try:
        response = client.chat.completions.create(
            model='gpt-4',
            messages=messages
                                                  )
        message = response.choices[0].message.content

        return message
    except Exception as e:
        print(e)
        pass
    
    
    



