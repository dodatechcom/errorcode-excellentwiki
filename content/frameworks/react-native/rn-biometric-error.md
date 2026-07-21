---
title: "[Solution] react-native Biometric Error"
description: "Biometric auth failing."
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

Biometric auth failing.

## Common Causes

Not available.

## How to Fix

Check availability.

## Example

```javascript
import * as LocalAuthentication from 'expo-local-authentication';
const hasHardware = await LocalAuthentication.hasHardwareAsync();
```
