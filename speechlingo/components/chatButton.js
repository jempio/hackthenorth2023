import React, { useState } from 'react';
import { TouchableOpacity, Text, StyleSheet } from 'react-native';

const ChatButton = ({ onRequest }) => {
  const [buttonVisible, setButtonVisible] = useState(true);

  const handlePress = async () => {
    await onRequest();
    setButtonVisible(false);
  };

  return (
    <>
      {buttonVisible ? (
        <TouchableOpacity style={styles.button} onPress={handlePress}>
          <Text style={styles.buttonText} >Generate Sentence</Text>
        </TouchableOpacity>
      ) : null}
    </>
  );
};


const styles = StyleSheet.create({
  button: {
    backgroundColor: '#007bff',
    padding: 10,
    borderRadius: 20,
    alignItems: 'center',
    justifyContent: 'center',
    marginTop: 20,
  },
  buttonText: {
    color: '#ffffff',
    fontSize: 16,
    fontWeight: 'bold',
  },
});

export default ChatButton;
