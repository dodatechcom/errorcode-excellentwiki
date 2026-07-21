---
title: "[Solution] React Native Dimensions Error"
description: "Wrong dimensions."
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

Wrong dimensions.

## Common Causes

Not using hook.

## How to Fix

Use useWindowDimensions.

## Example

```javascript
const { width, height } = useWindowDimensions();
```
