---
title: "[Solution] Flutter Navigator Push Error"
description: "Navigator push not working."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

Navigator push not working.

## Common Causes

Wrong route.

## How to Fix

Use MaterialPageRoute.

## Example

```dart
Navigator.push(context, MaterialPageRoute(builder: (_) => DetailPage()));
```
