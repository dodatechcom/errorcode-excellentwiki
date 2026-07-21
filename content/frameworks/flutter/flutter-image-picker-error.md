---
title: "[Solution] flutter Image Picker Error"
description: "Image picker not working."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

Image picker not working.

## Common Causes

Permission not granted.

## How to Fix

Request permission.

## Example

```dart
final picker = ImagePicker();
final image = await picker.pickImage(source: ImageSource.gallery);
```
