---
title: "[Solution] Flutter BottomNavigationBar Error"
description: "Nav not switching."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

Nav not switching.

## Common Causes

Wrong index.

## How to Fix

Handle index.

## Example

```dart
BottomNavigationBar(currentIndex: _i, onTap: (i) => setState(() => _i = i))
```
