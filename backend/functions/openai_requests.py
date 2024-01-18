from openai import OpenAI
from decouple import config


OPENAI_API_KEY = config('OPENAI_API_KEY')

client = OpenAI(api_key=OPENAI_API_KEY)



#conveert audio to transcription
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