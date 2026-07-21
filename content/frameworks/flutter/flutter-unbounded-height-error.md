---
title: "[Solution] Flutter Unbounded Height Error"
description: "Widget has unbounded height."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

Widget has unbounded height.

## Common Causes

Column without constraints.

## How to Fix

Use Expanded.

## Example

```dart
Column(children: [Expanded(child: ListView(...))])
```
