---
title: "[Solution] React Native Permissions Error"
description: "Permissions not granted."
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

Permissions not granted.

## Common Causes

Not requested.

## How to Fix

Request permission.

## Example

```javascript
const { status } = await Permissions.askAsync(Permissions.CAMERA);
```
