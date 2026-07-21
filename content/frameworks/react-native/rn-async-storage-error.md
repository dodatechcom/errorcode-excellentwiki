---
title: "[Solution] React Native Async Storage Error"
description: "AsyncStorage not storing."
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

AsyncStorage not storing.

## Common Causes

Not stringified.

## How to Fix

Stringify data.

## Example

```javascript
await AsyncStorage.setItem('k', JSON.stringify(d));
```
