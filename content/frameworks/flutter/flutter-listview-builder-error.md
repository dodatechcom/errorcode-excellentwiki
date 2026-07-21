---
title: "[Solution] Flutter ListView.builder Error"
description: "ListView.builder not building."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

ListView.builder not building.

## Common Causes

Wrong itemCount.

## How to Fix

Set itemCount.

## Example

```dart
ListView.builder(
  itemCount: items.length,
  itemBuilder: (ctx, i) => Text(items[i]),
)
```
