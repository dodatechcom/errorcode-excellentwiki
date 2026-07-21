---
title: "[Solution] Flutter ListView Unbounded Error"
description: "ListView unbounded."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

ListView unbounded.

## Common Causes

Inside Column.

## How to Fix

Use shrinkWrap.

## Example

```dart
ListView(shrinkWrap: true, children: [...])
```
