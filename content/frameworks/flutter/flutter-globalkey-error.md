---
title: "[Solution] Flutter  GlobalKey Error"
description: "GlobalKey not finding state."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

GlobalKey not finding state.

## Common Causes

Wrong usage.

## How to Fix

Use correctly.

## Example

```dart
final key = GlobalKey<FormState>();
Form(key: key, child: ...)
key.currentState?.validate();
```
