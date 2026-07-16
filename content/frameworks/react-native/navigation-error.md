---
title: "Navigation error"
description: "React Navigation throws an error when navigating between screens with invalid parameters or configuration"
frameworks: ["react-native"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["navigation", "react-navigation", "screen", "params"]
weight: 5
---

This error occurs when React Navigation encounters a problem navigating to a screen, such as missing required parameters, unregistered screen names, or incorrect navigator configuration.

## Common Causes

- Navigating to a screen name that is not registered in the navigator
- Missing required parameters for a route
- Navigator structure mismatch (e.g. Stack vs Tab)
- Using `navigation.navigate` before the navigator is ready

## How to Fix

1. Ensure screen names match exactly:

```jsx
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

const Stack = createStackNavigator();

function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="Details" component={DetailsScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
```

2. Pass required parameters:

```jsx
// Navigate with params
navigation.navigate('Details', { itemId: 42, title: 'Item Details' });

// Receive params
function DetailsScreen({ route }) {
  const { itemId, title } = route.params;
  return <Text>{title} - {itemId}</Text>;
}
```

3. Handle undefined params safely:

```jsx
function DetailsScreen({ route }) {
  const itemId = route.params?.itemId ?? 0;
  const title = route.params?.title ?? 'No Title';
  return <Text>{title}</Text>;
}
```

## Examples

```jsx
// Navigating to a non-existent screen
navigation.navigate('Settingss'); // typo
// The action 'NAVIGATE' with payload {"name":"Settingss"} was not handled
```

```text
Error: The action 'NAVIGATE' with payload {"name":"Settingss"} was not handled by any navigator.
```

## Related Errors

- [State update error]({{< relref "/frameworks/react-native/state-error" >}})
