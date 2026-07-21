---
title: "[Solution] Flutter dispose Called Error"
description: "dispose not cleaning up."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

dispose not cleaning up.

## Common Causes

Missing dispose.

## How to Fix

Dispose controllers.

## Example

```dart
@override
void dispose() { _c.dispose(); super.dispose(); }
```
