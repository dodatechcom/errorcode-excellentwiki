---
title: "[Solution] flutter Permission Handler Error"
description: "Permission not granted."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

Permission not granted.

## Common Causes

Not requested.

## How to Fix

Request.

## Example

```dart
final status = await Permission.camera.request();
if (status.isGranted) { /* proceed */ }
```
