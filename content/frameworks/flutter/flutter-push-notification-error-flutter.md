---
title: "[Solution] flutter Push Notification Error Flutter"
description: "Notifications not received."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

Notifications not received.

## Common Causes

Not configured.

## How to Fix

Configure Firebase.

## Example

```dart
FirebaseMessaging messaging = FirebaseMessaging.instance;
await messaging.requestPermission();
```
