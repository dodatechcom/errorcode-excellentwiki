---
title: "[Solution] flutter Local Auth Error"
description: "Biometric auth not working."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

Biometric auth not working.

## Common Causes

Not available.

## How to Fix

Check availability.

## Example

```dart
final auth = LocalAuthentication();
final canAuth = await auth.canCheckBiometrics;
```
