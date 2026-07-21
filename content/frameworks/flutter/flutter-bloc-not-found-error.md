---
title: "[Solution] Flutter Bloc Not Found Error"
description: "BlocProvider not found."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

BlocProvider not found.

## Common Causes

No ancestor.

## How to Fix

Wrap with BlocProvider.

## Example

```dart
BlocProvider(create: (_) => MyBloc(), child: MyApp())
```
