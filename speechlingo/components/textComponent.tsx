import React, { useState } from 'react';
import { StyleSheet, View, Text, SafeAreaView, TextInput, Button} from 'react-native';
import * as Speech from 'expo-speech';

function TextBox() {
  const [inputText, setInputText] = useState('');

  const speak = () => {
    const thingToSay = inputText;
    Speech.speak(thingToSay);
  };

  return (
    <SafeAreaView style={{flex:1}}>
      <View style={styles.container}>
        <TextInput
          value={inputText}
          onChangeText={(inputText) => setInputText(inputText)}
          placeholder={'Input something to hear!'}
          style={styles.input}
        />
        <Button title="Pronounce" onPress={speak} />
      </View>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    marginTop: 20,
    backgroundColor: '#ffffff',
  },
  input: {
    width: 250,
    height: 44,
    padding: 10,
    marginTop: 20,
    marginBottom: 10,
    backgroundColor: '#e8e8e8',
  },
});

export default TextBox;
