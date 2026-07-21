---
title: "[Solution] Flutter AnimatedContainer Error"
description: "AnimatedContainer not animating."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

AnimatedContainer not animating.

## Common Causes

Duration not set.

## How to Fix

Set duration.

## Example

```dart
AnimatedContainer(duration: Duration(milliseconds: 300), width: w, height: h)
```
