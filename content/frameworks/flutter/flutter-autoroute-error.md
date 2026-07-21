---
title: "[Solution] flutter AutoRoute Error"
description: "AutoRoute not routing."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

AutoRoute not routing.

## Common Causes

Wrong config.

## How to Fix

Configure generator.

## Example

```dart
@AutoRouterConfig()
class AppRouter extends $AppRouter {
  @override
  List<AutoRoute> get routes => [...];
}
```
