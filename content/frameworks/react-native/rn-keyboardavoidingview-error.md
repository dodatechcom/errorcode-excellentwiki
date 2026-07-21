---
title: "[Solution] React Native KeyboardAvoidingView Error"
description: "Keyboard covering input."
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

Keyboard covering input.

## Common Causes

Wrong behavior.

## How to Fix

Use correct.

## Example

```javascript
<KeyboardAvoidingView behavior={Platform.OS === 'ios' ? 'padding' : 'height'}>
```
