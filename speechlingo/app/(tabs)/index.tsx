import React, { useState } from 'react';
import { View, Text, StyleSheet } from 'react-native';
import ChatButton from '../../components/chatButton'; // Import the ChatButton component
//import GameRules from '../../components/gameRules';
import handleChatRequest from '../../components/handleChatRequest'; // Import the handleChatRequest function

export default function TabOneScreen() {
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
    <View style={styles.container}>
      <Text style={styles.title}>Pronunciation Game</Text>
      <View
        style={styles.separator}
      />
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
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#66283b',
  },
  separator: {
    marginVertical: 30,
    height: 1,
    width: '80%',
  },
});

