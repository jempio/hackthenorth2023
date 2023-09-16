import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import matplotlib.pyplot as plt
from torchvision import datasets, transforms
import torchaudio


def main():
    torch.random.manual_seed(0)
    device = torch.device("mps")
        
    # bundle = torchaudio.pipelines.WAV2VEC2_ASR_BASE_960H
    bundle = torchaudio.pipelines.WAV2VEC2_XLSR_300M

    model = bundle.get_model().to(device)

    torchaudio.set_audio_backend("sox_io")
    
    path = "/Users/shivansh/Personal/University/Hackathons/hackthenorth/hackthenorth2023/TRACK/000010011/segment_1.wav"
    test_waveform, test_sample_rate = torchaudio.load(path, format="wav")

    
    if test_sample_rate != bundle.sample_rate:
        test_waveform = torchaudio.functional.resample(test_waveform, test_sample_rate, bundle.sample_rate)

if __name__ == "__main__":
    main()
