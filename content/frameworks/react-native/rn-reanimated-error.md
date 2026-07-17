---
title: "Reanimated - shared value error"
description: "React Native Reanimated throws an error when accessing shared values incorrectly or from the wrong thread"
frameworks: ["react-native"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

A Reanimated shared value error occurs when you try to access or modify a `SharedValue` outside of a worklet, or when the shared value is accessed before being properly initialized. Reanimated requires that certain operations run on the UI thread via worklets.

## Common Causes

- Reading shared value outside a worklet or render
- Mutating shared value from the JS thread incorrectly
- Forgetting to add `'worklet'` directive to animated callbacks
- Accessing shared value before `useSharedValue` completes initialization
- Passing non-serializable values to shared values

## How to Fix

1. Only modify shared values inside worklets or event handlers:

```javascript
import Animated, { useSharedValue, useAnimatedStyle, withSpring } from 'react-native-reanimated';

const opacity = useSharedValue(0);

const handlePress = () => {
  'worklet';
  opacity.value = withSpring(1);
};

const animatedStyle = useAnimatedStyle(() => {
  return { opacity: opacity.value };
});
```

2. Initialize shared values with proper defaults:

```javascript
const translateX = useSharedValue(0); // initialize before use
```

3. Use `useAnimatedReaction` for reactive animations:

```javascript
import Animated, {
  useSharedValue,
  useAnimatedReaction,
  useAnimatedStyle,
  withTiming,
} from 'react-native-reanimated';

const scrollY = useSharedValue(0);

useAnimatedReaction(
  () => scrollY.value,
  (result) => {
    headerOpacity.value = result > 100 ? withTiming(1) : withTiming(0);
  }
);
```

4. Ensure Reanimated plugin is in `babel.config.js`:

```javascript
module.exports = {
  plugins: ['react-native-reanimated/plugin'],
};
```

## Examples

```javascript
// Error: Reading shared value outside worklet
const scale = useSharedValue(1);
console.log(scale.value); // may cause issues in production

// Fix: read in animated style
const style = useAnimatedStyle(() => ({
  transform: [{ scale: scale.value }],
}));
```

## Related Errors

- [Animation error]({{< relref "/frameworks/react-native/animation-error" >}})
- [Fast Refresh error]({{< relref "/frameworks/react-native/rn-fast-refresh-error" >}})
