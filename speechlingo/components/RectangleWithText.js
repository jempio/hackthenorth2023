import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

const RectangleWithText = ({ text }) => {
  return (
    <View style={styles.rectangle}>
      <Text style={styles.text}>{text}</Text>
      <Text style={styles.body}>You will be given a sentence to say and your score will be based on your pronunciation</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  rectangle: {
    width: '100%',              // Set the width of the rectangle
    height: 100,             // Set the height of the rectangle
    backgroundColor: '#dfbebc', // Set the background color
    justifyContent: 'center', // Center text vertically
    alignItems: 'center',    // Center text horizontally
    borderRadius: 10,        // Add rounded corners
    padding: 10,
  },
  text: {
    color: '#7A3D37',          // Set text color
    fontSize: 18,            // Set text font size
    fontWeight: 'bold',      // Set text font weight
  },
  body: {
    color: '#7A3D37',          // Set text color
    fontSize: 13,            // Set text font size
  },
});

export default RectangleWithText;