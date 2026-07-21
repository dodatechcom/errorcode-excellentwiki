---
title: "[Solution] Flutter SnackBar Error"
description: "SnackBar not showing."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

SnackBar not showing.

## Common Causes

Wrong usage.

## How to Fix

Use ScaffoldMessenger.

## Example

```dart
ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('Done')));
```
