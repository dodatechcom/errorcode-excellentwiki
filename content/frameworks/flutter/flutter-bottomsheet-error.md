---
title: "[Solution] Flutter BottomSheet Error"
description: "BottomSheet not showing."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

BottomSheet not showing.

## Common Causes

Wrong context.

## How to Fix

Use showModalBottomSheet.

## Example

```dart
showModalBottomSheet(context: context, builder: (_) => Container(child: Text('Hi')));
```
