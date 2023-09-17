<<<<<<< HEAD
import { StyleSheet } from 'react-native';
import RecordButton from '../../components/recording';

import EditScreenInfo from '../../components/EditScreenInfo';
import { Text, View } from '../../components/Themed';
=======
import React, { useState } from 'react';
import { View, Text, StyleSheet } from 'react-native';
import FirstState from '../../components/firstState';
>>>>>>> 6a6b4850e8d3bf4b40554d28e61be1cff30adf44


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

