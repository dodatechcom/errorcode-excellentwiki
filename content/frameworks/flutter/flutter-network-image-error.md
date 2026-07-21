---
title: "[Solution] Flutter Network Image Error"
description: "Network image not loading."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

Network image not loading.

## Common Causes

Wrong URL.

## How to Fix

Check URL.

## Example

```dart
Image.network('https://example.com/image.png',
  errorBuilder: (_, __, ___) => Icon(Icons.error))
```
