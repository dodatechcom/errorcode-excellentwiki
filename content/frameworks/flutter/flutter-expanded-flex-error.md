---
title: "[Solution] Flutter Expanded Flex Error"
description: "Expanded in wrong parent."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

Expanded in wrong parent.

## Common Causes

Not in Row/Column/Flex.

## How to Fix

Use in correct parent.

## Example

```dart
Row(children: [Expanded(child: Widget())])
```
