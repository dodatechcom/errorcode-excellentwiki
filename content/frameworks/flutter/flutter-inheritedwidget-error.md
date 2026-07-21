---
title: "[Solution] Flutter InheritedWidget Error"
description: "InheritedWidget not passing data."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

InheritedWidget not passing data.

## Common Causes

Wrong implementation.

## How to Fix

Use of(context).

## Example

```dart
final data = MyInherited.of(context).myData;
```
