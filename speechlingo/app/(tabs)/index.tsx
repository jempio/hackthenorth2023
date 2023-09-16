<<<<<<< Updated upstream
import { StyleSheet } from 'react-native';
import RecordButton from '../../components/recordButton';

import EditScreenInfo from '../../components/EditScreenInfo';
import { Text, View } from '../../components/Themed';
=======
import React, { useState } from 'react';
import { View, Text, StyleSheet } from 'react-native';
import ChatButton from '../../components/chatButton'; // Import the ChatButton component
import handleChatRequest from '../../components/handleChatRequest'; // Import the handleChatRequest function
import RecordButton from '../../components/recordButton'; // Import the RecordButton component
import TextComponent from '../../components/textComponent'; // Import the RecordButton component
>>>>>>> Stashed changes

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
<<<<<<< Updated upstream
      <Text style={styles.title}>Tab One</Text>
      <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />
      <EditScreenInfo path="app/(tabs)/index.tsx" />
      <RecordButton />
=======
      <Text style={styles.title}>Pronunciation Scorer</Text>
      <View
        style={styles.separator}
      />
      <ChatButton onRequest={onRequest} />
      {response && (
        <>
          <Text>Response:</Text>
          <Text>{response}</Text>
        </>
      )}
>>>>>>> Stashed changes
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

