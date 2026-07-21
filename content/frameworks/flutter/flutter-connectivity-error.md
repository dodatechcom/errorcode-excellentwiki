---
title: "[Solution] flutter Connectivity Error"
description: "No internet detected."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

No internet detected.

## Common Causes

Not checking.

## How to Fix

Check connectivity.

## Example

```dart
final result = await Connectivity().checkConnectivity();
if (result == ConnectivityResult.none) { /* no internet */ }
```
