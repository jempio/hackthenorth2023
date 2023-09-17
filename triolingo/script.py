import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchaudio

import numpy as np
from torch.nn.utils.rnn import pad_sequence

from scores_data import scores_data

import os

train = []

class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 96, 11, stride=4)
        self.pool = nn.MaxPool2d(3, 2)
        self.conv2 = nn.Conv2d(96, 256, 5, padding=2)
        self.conv3 = nn.Conv2d(256, 384, 3, padding=1)
        self.conv4 = nn.Conv2d(384, 384, 3, padding=1)
        self.conv5 = nn.Conv2d(384, 256, 3, padding=1)
        self.fc1 = nn.Linear(9216, 4096)
        self.fc2 = nn.Linear(4096, 1000)
        self.fc3 = nn.Linear(1000, 1)
    
    def forward(self, x):
        # print(x.size())
        # x = F.relu(self.conv(x))
        x = self.pool(F.relu(self.conv1(x)))
        # print(x.size())
        x = self.pool(F.relu(self.conv2(x)))
        # print(x.size())
        x = F.relu(self.conv3(x))
        # print(x.size())
        x = F.relu(self.conv4(x))
        # print(x.size())
        x = self.pool(F.relu(self.conv5(x)))
        # print(x.size())
        x = x.view(-1, 9216)
        # print(x.size())
        x = F.relu(self.fc1(x))
        # print(x.size())
        x = F.relu(self.fc2(x))
        # print(x.size())
        x = self.fc3(x)
        # print(x.size())
        return x
    
def inference(wav_file_path):
    model = torch.load('test_model_epoch-2.pt')
    print(model.eval())
    waveform, _ = torchaudio.load(wav_file_path)
    audio_spectagram = torchaudio.transforms.Spectrogram()(waveform).long()
    print(audio_spectagram.shape[2])
    t = audio_spectagram[:,:,:201]
    t = t.squeeze()
    t = np.pad(t, (0, 26), 'constant')

    t = torch.from_numpy(t)
    t = t.float()
    t = t.reshape((1, 227, 227))
    # train = [t, scores_data["000010069"]["total"]]
    # train_loader = torch.utils.data.DataLoader(train, batch_size=1, shuffle=True)
    
    pred = model.forward(t)
    prediction = torch.mean(pred)
    
    
    return prediction.item()

if __name__ =="__main__":
    
    SPEECH_FILE = "/Users/shivansh/Personal/University/Hackathons/hackthenorth/hackthenorth2023/TRACKS_NEW/000930151/000930151.WAV"
    s_file = "/Users/shivansh/Personal/University/Hackathons/hackthenorth/hackthenorth2023/users_speech/my_speech3.wav"
    print(inference(SPEECH_FILE))