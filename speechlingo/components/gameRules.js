import React from 'react';
import { View, StyleSheet } from 'react-native';
import RectangleWithText from './RectangleWithText'; // Import the component

const GameRules = () => {
  return (
    <View style={styles.container}>
      <RectangleWithText text="Rules:" />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    alignItems: 'center',
  },
});

export default GameRules;