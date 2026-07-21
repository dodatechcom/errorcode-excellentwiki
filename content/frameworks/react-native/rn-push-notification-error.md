---
title: "[Solution] React Native Push Notification Error"
description: "Notifications not received."
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

Notifications not received.

## Common Causes

Token not registered.

## How to Fix

Register.

## Example

```javascript
const t = await messaging().getToken();
```
