import sounddevice as sd
import wavio
import os

# Set the recording parameters
duration = 5  # Recording duration in seconds
sample_rate = 44100  # Sample rate in Hz
output_directory = "users_speech"  # Replace with your desired directory
filename = "my_speech.wav"  # Name of the audio file

# Set the full path for the audio file
output_path = os.path.join(output_directory, filename)

print("Recording...")

# Record audio
audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2)
sd.wait()

# Save the audio to the specified directory
wavio.write(output_path, audio_data, sample_rate, sampwidth=3)

print(f"Audio saved as {output_path}")
