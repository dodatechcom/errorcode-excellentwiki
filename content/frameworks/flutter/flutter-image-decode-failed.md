---
title: "[Solution] Flutter Image Decode Failed"
description: "Image cannot decode."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

Image cannot decode.

## Common Causes

Wrong format.

## How to Fix

Check format.

## Example

```dart
Image.network('url', errorBuilder: (_, __, ___) => Icon(Icons.error))
```
