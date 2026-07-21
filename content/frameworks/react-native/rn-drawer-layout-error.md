---
title: "[Solution] React Native DrawerLayout/Menu navigation error"
description: "react-native DrawerLayoutAndroid or React Navigation Drawer freezes, overlaps content, or fails to close entirely on both platforms"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The DrawerLayout error occurs when the slide-open drawer intercepts touch events incorrectly or becomes stuck open. Using DrawerLayoutAndroid directly often causes position:absolute content to render behind the drawer.

## Common Causes

- DrawerLayoutAndroid imported from react-native but being used on iOS
- Missing gestureHandlerRootView when using React Navigation drawer
- drawerStyle or contentContainerStyle collision with absolute positioning
- Over-rendering due to component state updates inside the drawer navigation
- Android hardware acceleration conflicts with DrawerLayout
- nested ScrollViews inside the drawer body

## How to Fix

1. Use React Navigation drawer for cross-platform compatibility:

```javascript
import { createDrawerNavigator } from '@react-navigation/drawer';
import { GestureHandlerRootView } from 'react-native-gesture-handler';

const Drawer = createDrawerNavigator();

function App() {
  return (
    <GestureHandlerRootView style={{ flex: 1 }}>
      <NavigationContainer>
        <Drawer.Navigator>
          <Drawer.Screen name="Home" component={HomeScreen} />
        </Drawer.Navigator>
      </NavigationContainer>
    </GestureHandlerRootView>
  );
}
```

2. Close the drawer programmatically to avoid stuck state:

```javascript
navigation.closeDrawer();
```

## Examples

```javascript
// Error: DrawerLayoutAndroid freezes after orientation change
// Fix: override drawerLockMode
<DrawerNavigator
  drawerLockMode="unlocked"
/>
```

## Related Errors

- [React Navigation Error]({{< relref "/frameworks/react-native/rn-navigation-error" >}})
- [Gesture Handler Error]({{< relref "/frameworks/react-native/rn-gesture-handler-error" >}})
