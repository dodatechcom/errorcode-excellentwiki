---
title: "[Solution] Flutter ClipRRect Error"
description: "ClipRRect not clipping."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

ClipRRect not clipping.

## Common Causes

Wrong usage.

## How to Fix

Wrap child.

## Example

```dart
ClipRRect(borderRadius: BorderRadius.circular(20), child: Image.network(url))
```
