from gtts import gTTS
from pydub import AudioSegment
import os
import tempfile
import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Capture audio from the microphone
with sr.Microphone() as source:
    print("Say something:")
    audio = recognizer.listen(source)

# Recognize the speech
try:
    text = recognizer.recognize_google(audio)
    print("You said:", text)

    # Convert recognized text to speech using gTTS
    tts = gTTS("You said: " + text)

    # Specify the directory where you want to save the audio file
    save_directory = r'C:\Users\nitsu\Desktop\htn2023\hackthenorth2023\users_speech\\'

    # Save the speech as an audio file in the specified directory
    audio_file_path = os.path.join(save_directory, "output.mp3")
    tts.save(audio_file_path)

    # # Convert the MP3 file to WAV format
    # audio = AudioSegment.from_mp3(mp3_audio_file)
    # wav_audio_file = os.path.join(save_directory, "output.wav")
    # audio.export(wav_audio_file, format="wav")

except sr.UnknownValueError:
    print("Sorry, could not understand your speech.")
except sr.RequestError as e:
    print("Error requesting speech recognition; {0}".format(e))
