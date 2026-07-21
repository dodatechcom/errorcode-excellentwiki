---
title: "[Solution] Flutter FutureBuilder Error"
description: "FutureBuilder rebuilding."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

FutureBuilder rebuilding.

## Common Causes

New future on rebuild.

## How to Fix

Cache the future.

## Example

```dart
final future = useMemoized(() => fetchData());
FutureBuilder(future: future, builder: (_, s) => ...)
```
