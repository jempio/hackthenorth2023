import React, { useState } from 'react';
import { View, Text, StyleSheet } from 'react-native';
import FirstState from '../../components/firstState';

export default function TabOneScreen() {
  const [response, setResponse] = useState('');

  return (
    <View style={styles.container}>
      <FirstState/>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#f9f5ed',
    padding: '10%',
  },
});

