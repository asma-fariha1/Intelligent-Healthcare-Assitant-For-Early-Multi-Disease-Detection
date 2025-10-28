print("Running voice_of_the_doctor.py")
from dotenv import load_dotenv
load_dotenv()


import os

ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")
#print("ELEVENLABS_API_KEY:", ELEVENLABS_API_KEY)

from gtts import gTTS

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)


input_text="Hi this is Ai with us!"
#text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")




#import elevenlabs
#from elevenlabs.client import ElevenLabs

#ELEVENLABS_API_KEY=os.environ.get("ELEVENLABS_API_KEY")

#def text_to_speech_with_elevenlabs_old(input_text,output_filepath):
    #client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    #audio=generate(
        #text= input_text,
        #voice= "Aria",
        #output_format= "mp3_22050_32",
        #model= "eleven_turbo_v2"
    #)
    #elevenlabs.save(audio, output_filepath)

#text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing.mp3") 



import subprocess
import platform
import os
from gtts import gTTS   

def text_to_speech_with_gtts(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windowsk_4214996b691abc2922fbf815e439876f297794c4e6810bd7
            os.startfile(output_filepath)
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


input_text="Hi this is Ai with us, autoplay testing!"
text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing_autoplay.mp3")


#from elevenlabs.text_to_speech import text_to_speech
from elevenlabs.client import ElevenLabs   # ✅ Correct import
import os, subprocess, platform

# 🔑 Hardcode your ElevenLabs API key here
ELEVENLABS_API_KEY = "sk_fba0a85516a1f8e4f7c1e3b59f2e0b31717bacff1d73e884"

# ✅ Initialize ElevenLabs client
client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    # ✅ Generate speech from ElevenLabs
    audio = client.text_to_speech.convert(
        text=input_text,
        voice_id="sccYFB6TkWjH8RZUaqGK",
        model_id="eleven_multilingual_v2",   
        output_format="mp3_22050_32"
    )

    with open(output_filepath, "wb") as f:
     for chunk in audio:   # audio is a generator of chunks
        f.write(chunk)


    # ✅ Play audio depending on OS
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            os.startfile(output_filepath)
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Or mpg123 / ffplay
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")
    return output_filepath    

# ✅ Example call
text_to_speech_with_elevenlabs(input_text,output_filepath="elevenlabs_testing_autoplay.mp3")

