---
title: "[Solution] flutter Camera Error"
description: "Camera not initializing."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

Camera not initializing.

## Common Causes

Permission denied.

## How to Fix

Request permission.

## Example

```dart
final controller = CameraController(cameras[0], ResolutionPreset.high);
await controller.initialize();
```
