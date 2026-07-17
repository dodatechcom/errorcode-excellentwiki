---
title: "Animated node error"
description: "React Native throws an error when using the Animated API on an unmounted or invalid node"
frameworks: ["react-native"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when React Native's `Animated` API tries to operate on a node that has been detached or destroyed, typically after a component unmounts while an animation is still running.

## Common Causes

- Animation still running when component unmounts
- Animated node was stopped or detached prematurely
- Using `Animated.Value` in a conditional render without cleanup
- Old Animated API incompatibility with Reanimated 2+

## How to Fix

1. Stop animations on unmount:

```jsx
import { useEffect, useRef } from 'react';
import { Animated } from 'react-native';

function FadeIn() {
  const opacity = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    const animation = Animated.timing(opacity, {
      toValue: 1,
      duration: 500,
      useNativeDriver: true,
    });
    animation.start();

    return () => animation.stop(); // cleanup
  }, []);

  return <Animated.View style={{ opacity }} />;
}
```

2. Reset animated values when component mounts:

```jsx
useEffect(() => {
  opacity.setValue(0);
  Animated.timing(opacity, {
    toValue: 1,
    duration: 300,
    useNativeDriver: true,
  }).start();
}, []);
```

3. Use `useAnimatedStyle` from Reanimated for complex animations:

```jsx
import Animated, { useSharedValue, useAnimatedStyle, withTiming } from 'react-native-reanimated';

function AnimatedBox() {
  const offset = useSharedValue(0);

  const style = useAnimatedStyle(() => ({
    transform: [{ translateX: offset.value }],
  }));

  const handlePress = () => {
    offset.value = withTiming(offset.value === 0 ? 100 : 0);
  };

  return <Animated.View style={[styles.box, style]} />;
}
```

## Examples

```jsx
// Animation running when component unmounts
function Component() {
  const anim = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    Animated.loop(Animated.timing(anim, {
      toValue: 1, duration: 1000, useNativeDriver: true,
    })).start();
  }, []);
  // Loop continues after unmount — Animated node error
  return <Animated.View style={{ opacity: anim }} />;
}
```

```text
Invariant Violation: findHostComponent_DEPRECATED: Could not find the animated node
```

## Related Errors

- [State update error]({{< relref "/frameworks/react-native/state-error" >}})
