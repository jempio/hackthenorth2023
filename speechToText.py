import sounddevice as sd
import wavio
import os
import webrtcvad
import numpy as np

# Set the recording parameters
sample_rate = 44100  # Sample rate in Hz
output_directory = "users_speech"  # Replace with your desired directory
filename = "my_speech.wav"  # Name of the audio file

# Ensure the output directory exists, create it if it doesn't
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Set the full path for the audio file
output_path = os.path.join(output_directory, filename)

# Initialize VAD
vad = webrtcvad.Vad()
vad.set_mode(2)  # Use aggressive mode for voice detection

print("Recording... (Speaking will trigger recording)")

# Initialize audio buffer
audio_data = []

# Function to check if audio is non-silent
def is_audio_active(samples):
    return vad.is_speech(samples.tobytes(), sample_rate)

# Start recording audio
with sd.InputStream(callback=lambda indata, frames, time, status: audio_data.extend(indata)):
    sd.sleep(1000)  # Initial recording will start when speech is detected

    # Continue recording as long as there is active speech
    while True:
        audio_chunk = np.array(audio_data)
        if is_audio_active(audio_chunk):
            audio_data.clear()
        else:
            break  # Stop recording when speech stops

# Stop recording
print("Recording stopped")

# Save the recorded audio to the specified directory
wavio.write(output_path, audio_chunk, sample_rate, sampwidth=3)

print(f"Audio saved as {output_path}")
