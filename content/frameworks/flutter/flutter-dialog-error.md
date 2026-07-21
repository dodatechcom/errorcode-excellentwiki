---
title: "[Solution] Flutter Dialog Error"
description: "Dialog not showing."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

Dialog not showing.

## Common Causes

Wrong context.

## How to Fix

Use correct context.

## Example

```dart
showDialog(context: context, builder: (_) => AlertDialog(title: Text('T')));
```
