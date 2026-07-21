---
title: "[Solution] flutter SharedPreferences Error"
description: "Prefs not loading."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

Prefs not loading.

## Common Causes

Not initialized.

## How to Fix

Initialize.

## Example

```dart
final prefs = await SharedPreferences.getInstance();
prefs.setString('key', 'value');
```
