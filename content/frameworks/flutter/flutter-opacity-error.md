---
title: "[Solution] Flutter Opacity Error"
description: "Opacity widget causing perf issues."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

Opacity widget causing perf issues.

## Common Causes

Using for hiding.

## How to Fix

Use Visibility instead.

## Example

```dart
Visibility(visible: show, child: widget)
```
