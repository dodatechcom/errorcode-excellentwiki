---
title: "[Solution] Flutter Asset Image Not Found"
description: "Asset not loading."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

Asset not loading.

## Common Causes

Wrong path.

## How to Fix

Check pubspec.

## Example

```yaml
flutter:
  assets:
    - assets/images/
```
```dart
Image.asset('assets/images/logo.png')
```
