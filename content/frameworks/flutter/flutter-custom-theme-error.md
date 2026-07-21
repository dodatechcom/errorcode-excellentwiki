---
title: "[Solution] Flutter Custom Theme Error"
description: "Custom theme not working."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

Custom theme not working.

## Common Causes

Wrong extension.

## How to Fix

Use ThemeExtension.

## Example

```dart
class MyColors extends ThemeExtension<MyColors> {
  final Color primary;
  MyColors({required this.primary});
}
```
