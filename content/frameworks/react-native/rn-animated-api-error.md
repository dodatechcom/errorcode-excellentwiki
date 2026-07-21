---
title: "[Solution] React Native Animated API Error"
description: "Animated API not working."
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

Animated API not working.

## Common Causes

Wrong usage.

## How to Fix

Use Animated.Value.

## Example

```javascript
const opacity = new Animated.Value(0);
Animated.timing(opacity, { toValue: 1, duration: 500 }).start();
```
