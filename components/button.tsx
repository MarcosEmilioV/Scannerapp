import {View, Text, Pressable} from "react-native";

type Props = {
    label: string;
    onPress? : () => void;  
}

export default function Button({label, onPress}: Props) {
    return (
        <View>
            <Pressable></Pressable>
        </View>
    )
}