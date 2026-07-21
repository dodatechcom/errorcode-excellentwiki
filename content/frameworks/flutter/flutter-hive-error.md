---
title: "[Solution] flutter Hive Error"
description: "Hive box not opening."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

Hive box not opening.

## Common Causes

Not initialized.

## How to Fix

Initialize Hive.

## Example

```dart
await Hive.initFlutter();
await Hive.openBox('myBox');
```
