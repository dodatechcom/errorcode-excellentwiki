---
title: "[Solution] Flutter MediaQuery Padding Error"
description: "Safe area not working."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

Safe area not working.

## Common Causes

Not using padding.

## How to Fix

Use MediaQuery.padding.

## Example

```dart
final padding = MediaQuery.of(context).padding;
SafeArea(child: content)
```
