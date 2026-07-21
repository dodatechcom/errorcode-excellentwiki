---
title: "[Solution] Flutter AnimationController Error"
description: "Controller not working."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

Controller not working.

## Common Causes

Wrong vsync.

## How to Fix

Use mixin.

## Example

```dart
late AnimationController ac;
@override
void initState() { ac = AnimationController(vsync: this, duration: Duration(seconds: 1)); }
```
