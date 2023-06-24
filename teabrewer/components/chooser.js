import React from 'react';
import { View, ScrollView, Text } from 'react-native';


const ScrollOptionsPage = () => {
    return (
      <View style={{ flex: 1 }}>
        <ScrollView>
          <View style={{ height: 200, backgroundColor: 'lightblue' }}>
            <Text style={{ fontSize: 20, textAlign: 'center', paddingVertical: 20 }}>Flavors</Text>
          </View>
          <View style={{ height: 200, backgroundColor: 'lightgreen' }}>
            <Text style={{ fontSize: 20, textAlign: 'center', paddingVertical: 20 }}>Capacity</Text>
          </View>
        </ScrollView>
      </View>
    );
  };
  

  export default ScrollOptionsPage;
