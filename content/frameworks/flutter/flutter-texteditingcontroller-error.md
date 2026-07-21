---
title: "[Solution] Flutter TextEditingController Error"
description: "Controller not disposing."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

Controller not disposing.

## Common Causes

Missing dispose.

## How to Fix

Dispose controller.

## Example

```dart
final tc = TextEditingController();
@override
void dispose() { tc.dispose(); super.dispose(); }
```
