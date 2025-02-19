import { Tabs } from "expo-router";
import Ionicons from '@expo/vector-icons/Ionicons';
import "C:/Users/Lenovo/scannerapp/global.css";

export default function RootLayout() {
  return (
    <Tabs>
      <Tabs.Screen name = 'index' options = {{
        title: "Home",
        tabBarIcon: ({color, focused, size}) => (
          <Ionicons name= {focused ? "information-circle": "information-circle-outline"} color= 'red' size = {24}></Ionicons>
        ),
      }}>
            </Tabs.Screen>
      <Tabs.Screen name = 'records' options = {{
        title: "My Receipts",
        tabBarIcon: ({color, focused, size}) => (
          <Ionicons name= {focused ? "information-circle": "information-circle-outline"} color= 'red' size = {24}></Ionicons>
        ),
      }}>
      </Tabs.Screen>
      <Tabs.Screen name = 'spreadsheets' options = {{
        title: "Expenses",
        tabBarIcon: ({color, focused, size}) => (
          <Ionicons name= {focused ? "information-circle": "information-circle-outline"} color= 'red' size = {24}></Ionicons>
        ),
      }}>
      </Tabs.Screen>
    </Tabs>
  );
}
  
