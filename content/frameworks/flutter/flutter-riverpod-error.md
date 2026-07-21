---
title: "[Solution] flutter Riverpod Error"
description: "Riverpod provider not found."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

Riverpod provider not found.

## Common Causes

Not wrapped.

## How to Fix

Wrap with ProviderScope.

## Example

```dart
ProviderScope(child: MyApp())
```
