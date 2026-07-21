---
title: "[Solution] Flutter Context Not Mounted Error"
description: "Context after unmount."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

Context after unmount.

## Common Causes

Async gap.

## How to Fix

Check mounted.

## Example

```dart
if (mounted) Navigator.of(context).pop();
```
