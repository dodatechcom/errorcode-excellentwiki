---
title: "[Solution] react-native Animated Scroll Error"
description: "Scroll animation not working."
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

Scroll animation not working.

## Common Causes

Wrong usage.

## How to Fix

Use Animated.ScrollView.

## Example

```javascript
import Animated, { useAnimatedScrollHandler } from 'react-native-reanimated';
const scrollHandler = useAnimatedScrollHandler({ onScroll: (e) => { /* handle */ } });
<Animated.ScrollView onScroll={scrollHandler} />
```
