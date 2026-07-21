---
title: "[Solution] Flutter Navigator Not Found"
description: "Navigator unavailable."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

Navigator unavailable.

## Common Causes

No ancestor.

## How to Fix

Ensure MaterialApp.

## Example

```dart
Navigator.of(context).push(MaterialPageRoute(builder: (_) => Next()));
```
