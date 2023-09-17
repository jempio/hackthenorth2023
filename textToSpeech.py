from gtts import gTTS
from pydub import AudioSegment
import os

# Text you want to convert to speech
text = "Hello, this is a sample text-to-speech conversion."

# Create a gTTS object
tts = gTTS(text)

# Save the speech as an MP3 file
tts.save("output.mp3")

# Convert the MP3 file to WAV format
audio = AudioSegment.from_mp3("output.mp3")
audio.export("output.wav", format="wav")

# Clean up by removing the temporary audio files
os.remove("output.mp3")

# Play the audio file if needed
os.system("aplay output.wav")  # You may need to install aplay or use a different player
