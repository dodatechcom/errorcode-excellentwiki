---
title: "[Solution] Flutter Scaffold.of Error"
description: "Scaffold.of not finding."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

Scaffold.of not finding.

## Common Causes

Wrong context.

## How to Fix

Use ScaffoldMessenger.

## Example

```dart
ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('Hi')));
```
