import os
import shutil

# Main function to process the audio files for each speaker
def process_speakers(input_folder, output_parent_folder):
    for speaker_folder in os.listdir(input_folder):
        speaker_path = os.path.join(input_folder, speaker_folder)

        if os.path.isdir(speaker_path):
            for audio_file in os.listdir(speaker_path):
                if audio_file.endswith(".WAV"):  # Adjust the file extension as needed
                    audio_path = os.path.join(speaker_path, audio_file)
                    
                    # Create a folder with the same name as the audio file (without extension)
                    track_folder_name = os.path.splitext(audio_file)[0]
                    track_folder = os.path.join(output_parent_folder, track_folder_name)
                    os.makedirs(track_folder, exist_ok=True)

                    # Copy the entire audio file to the new folder
                    shutil.copy(audio_path, track_folder)

if __name__ == "__main__":
    input_folder = "WAVE"
    output_parent_folder = "TRACKS"
    os.makedirs(output_parent_folder, exist_ok=True)
    process_speakers(input_folder, output_parent_folder)
