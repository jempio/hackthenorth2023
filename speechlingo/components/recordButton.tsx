import React, { useState, useEffect } from 'react';
import { View, Text, TouchableOpacity } from 'react-native';
import AudioRecorderPlayer from 'react-native-audio-recorder-player';

const AudioRecorder: React.FC = () => {
  const audioRecorderPlayer = new AudioRecorderPlayer();
  const [isRecording, setIsRecording] = useState(false);
  const [audioPath, setAudioPath] = useState<string | null>(null);

  useEffect(() => {
    // Check for and request necessary permissions for audio recording here
  }, []);

  const startRecording = async () => {
    try {
      const path = await audioRecorderPlayer.startRecorder();
      setIsRecording(true);
      setAudioPath(path);
    } catch (error) {
      console.error('Error starting recording:', error);
    }
  };

  const stopRecording = async () => {
    try {
      const path = await audioRecorderPlayer.stopRecorder();
      setIsRecording(false);
      setAudioPath(path);
    } catch (error) {
      console.error('Error stopping recording:', error);
    }
  };

  return (
    <View>
      <TouchableOpacity
        onPress={isRecording ? stopRecording : startRecording}
        style={{
          backgroundColor: isRecording ? 'red' : 'green',
          width: 100,
          height: 100,
          borderRadius: 50,
          justifyContent: 'center',
          alignItems: 'center',
        }}
      >
        <Text style={{ color: 'white' }}>
          {isRecording ? 'Stop' : 'Record'}
        </Text>
      </TouchableOpacity>
      {audioPath && (
        <Text style={{ marginTop: 20 }}>
          Recorded audio file path: {audioPath}
        </Text>
      )}
    </View>
  );
};

export default AudioRecorder;