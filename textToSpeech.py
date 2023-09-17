from gtts import gTTS
from tempfile import NamedTemporaryFile
from playsound import playsound

def generateSpeech(text):

    # Create a gTTS object
    tts = gTTS(text)

    # Save the speech as an audio file
    tts.save("output.mp3") 

    playsound("output.mp3")

