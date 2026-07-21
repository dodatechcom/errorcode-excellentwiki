---
title: "[Solution] Flutter GridView Error"
description: "GridView not laying out."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

GridView not laying out.

## Common Causes

Wrong delegate.

## How to Fix

Use SliverGridDelegate.

## Example

```dart
GridView.builder(
  gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(crossAxisCount: 2),
  itemBuilder: (_, i) => Card(child: Text(items[i])),
)
```
