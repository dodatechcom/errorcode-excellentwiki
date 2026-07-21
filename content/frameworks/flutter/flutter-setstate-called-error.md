---
title: "[Solution] Flutter setState Called Error"
description: "setState after dispose."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

setState after dispose.

## Common Causes

Calling on unmounted.

## How to Fix

Check mounted.

## Example

```dart
if (mounted) setState(() {});
```
