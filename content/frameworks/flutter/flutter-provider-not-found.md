---
title: "[Solution] Flutter Provider Not Found"
description: "Provider not in tree."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

Provider not in tree.

## Common Causes

No Provider ancestor.

## How to Fix

Wrap with Provider.

## Example

```dart
ChangeNotifierProvider(create: (_) => MyModel(), child: MyApp())
```
