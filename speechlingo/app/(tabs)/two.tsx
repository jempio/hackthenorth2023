import { StyleSheet } from 'react-native';
import TextBox from '../../components/textComponent';
import EditScreenInfo from '../../components/EditScreenInfo';
import { Text, View } from '../../components/Themed';
import { LogBox } from 'react-native';

// Ignore specific warnings by adding a filter
LogBox.ignoreLogs([
  'Sending `Exponent.speakingStarted` with no listeners registered.',
  'Sending `Exponent.speakingWillSayNextString` with no listeners registered.',
  'Sending `Exponent.speakingDone` with no listeners registered.',
]);

// Enable LogBox (important to process the ignored warnings)
LogBox.ignoreAllLogs(true);

export default function TabTwoScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Tab Two</Text>
      <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />
      <EditScreenInfo path="app/(tabs)/two.tsx" />
      <TextBox/>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
  },
  separator: {
    marginVertical: 30,
    height: 1,
    width: '80%',
  },
});
