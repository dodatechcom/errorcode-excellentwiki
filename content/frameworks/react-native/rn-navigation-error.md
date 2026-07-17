---
title: "React Navigation - screen not found"
description: "React Navigation throws an error when navigating to a screen that is not registered in the navigator"
frameworks: ["react-native"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["react-navigation", "navigation", "screen", "navigator", "routing"]
weight: 5
---

The "screen not found" error in React Navigation occurs when you try to navigate to a route name that does not exist in any of your registered navigators. This can also happen when screen names are mistyped or when nested navigators are not properly linked.

## Common Causes

- Screen name typo in `navigation.navigate()`
- Screen not registered in the navigator's `screens` prop
- Nested navigator screens not defined in the parent
- Dynamic route names that evaluate to undefined
- Navigator ref used before initialization

## How to Fix

1. Verify all screen names match their registration:

```javascript
<Stack.Navigator>
  <Stack.Screen name="Home" component={HomeScreen} />
  <Stack.Screen name="Profile" component={ProfileScreen} />
  <Stack.Screen name="Settings" component={SettingsScreen} />
</Stack.Navigator>

// Navigate using exact registered names
navigation.navigate('Profile'); // correct
// navigation.navigate('ProfileScreen'); // wrong
```

2. Use TypeScript to enforce valid route names:

```typescript
type RootStackParamList = {
  Home: undefined;
  Profile: { userId: string };
  Settings: undefined;
};

const navigation = useNavigation<NativeStackNavigationProp<RootStackParamList>>();

navigation.navigate('Profile', { userId: '123' }); // type-safe
```

3. List all registered screens for debugging:

```javascript
const debuggingNavRef = useNavigationContainerRef();

useEffect(() => {
  console.log('Current routes:', debuggingNavRef?.getRootState()?.routes);
}, []);
```

4. Handle navigation errors with a fallback:

```javascript
const safeNavigate = (name, params) => {
  try {
    navigation.navigate(name, params);
  } catch {
    navigation.navigate('Home');
  }
};
```

## Examples

```javascript
// Error: The action 'NAVIGATE' with payload {"name":"Setting"} was not handled
navigation.navigate('Setting'); // typo: should be 'Settings'

// Correct
navigation.navigate('Settings');
```

## Related Errors

- [RedBox error]({{< relref "/frameworks/react-native/rn-redbox-error-v2" >}})
- [Storage error]({{< relref "/frameworks/react-native/rn-storage-error" >}})
