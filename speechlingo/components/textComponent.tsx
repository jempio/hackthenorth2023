import React, { useState } from 'react';
import { StyleSheet, View, Text, SafeAreaView, TextInput } from 'react-native';

const TextBox: React.FC = () => {
  const [userName, setUserName] = useState<string>('');

  return (
    <TextInput
      value={userName}
      onChangeText={(userName) => setUserName(userName)}
      placeholder={'UserName'}
      style={styles.input}
    />
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
