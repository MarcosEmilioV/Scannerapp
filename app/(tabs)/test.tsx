import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet } from 'react-native';

export default function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/hello') // Replace with your computer's IP
      .then(response => {
        console.log("RAW RESPONSE:", response)
        if (!response.ok) {
          throw new Error('Network response was not ok'); // if response wasn't accepted then throw error
        }
        return response.json(); //else if its accepted, return that response jsonified
      })
      .then(data => {console.log("DATA IS:", data); setData(data);})
      .catch(error => console.error('La cagaste:', error));
  }, []);

  return (
    <View style={styles.container}>
      <Text>{data ? data : 'Loading...'}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});
