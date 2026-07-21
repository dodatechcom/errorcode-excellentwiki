---
title: "[Solution] Flutter Theme Data Error"
description: "Theme not applying."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

Theme not applying.

## Common Causes

No Theme ancestor.

## How to Fix

Wrap with MaterialApp.

## Example

```dart
MaterialApp(theme: ThemeData(primarySwatch: Colors.blue))
```
