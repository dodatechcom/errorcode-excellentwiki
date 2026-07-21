---
title: "[Solution] Flutter Positioned Outside Error"
description: "Positioned outside Stack."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

Positioned outside Stack.

## Common Causes

Not in Stack.

## How to Fix

Use inside Stack.

## Example

```dart
Stack(children: [Positioned(top: 10, child: Text('Hi'))])
```
