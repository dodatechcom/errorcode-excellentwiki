---
title: "[Solution] React Native Platform Specific Code"
description: "Platform code not working."
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

Platform code not working.

## Common Causes

Wrong Platform check.

## How to Fix

Use Platform.OS.

## Example

```javascript
import { Platform } from 'react-native';
const isIOS = Platform.OS === 'ios';
```
