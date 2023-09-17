import React, { useState } from 'react';
import { View, Text, StyleSheet } from 'react-native';
import ChatButton from './chatButton'; // Import the ChatButton component
import GameRules from './gameRules';
import handleChatRequest from './handleChatRequest'; // Import the handleChatRequest function

export default function FirstState() {
  const [response, setResponse] = useState('');

  const onRequest = async () => {
    try {
      const answer = await handleChatRequest();
      setResponse(answer);
    } catch (error) {
      // Handle errors if need
    }
  };

  return (
    <View>
      <Text style={styles.title}>Pronunciation Game</Text>
      <View style={styles.separator}/>
      <GameRules/>
      <ChatButton onRequest={onRequest} />
      {response && (
        <>
          <Text>{response}</Text>
        </>
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#f9f5ed',
    padding: '10%'
  },
  title: {
    fontSize: 30,
    fontWeight: 'bold',
    color: '#66283b',
  },
  separator: {
    marginVertical: 15,
    height: 1,
    width: '80%',
  },
});