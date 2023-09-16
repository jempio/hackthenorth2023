from pydub import AudioSegment
import os

# Function to split audio track into one-second segments
def split_audio(input_audio, output_folder):
    audio = AudioSegment.from_file(input_audio)
    segment_duration = 1000  # 1 second in milliseconds

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Split the audio into one-second segments
    for i, start_time in enumerate(range(0, len(audio), segment_duration)):
        segment = audio[start_time:start_time + segment_duration]
        segment.export(os.path.join(output_folder, f"segment_{i+1}.wav"), format="wav")

# Main function to process the audio files for each speaker
def process_speakers(input_folder, output_folder):
    for speaker_folder in os.listdir(input_folder):
        speaker_path = os.path.join(input_folder, speaker_folder)

        if os.path.isdir(speaker_path):
            for audio_file in os.listdir(speaker_path):
                if audio_file.endswith(".WAV"):  # Adjust the file extension as needed
                    audio_path = os.path.join(speaker_path, audio_file)
                    track_folder = os.path.join(output_folder, os.path.splitext(audio_file)[0])

                    # Split the audio and save the segments in the new folder
                    split_audio(audio_path, track_folder)

if __name__ == "__main__":
    input_folder = "WAVE"
    output_folder = "TRACK"
    os.makedirs(output_folder, exist_ok=True)
    process_speakers(input_folder, output_folder)