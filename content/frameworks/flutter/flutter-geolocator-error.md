---
title: "[Solution] flutter Geolocator Error"
description: "Location not working."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

Location not working.

## Common Causes

Permission denied.

## How to Fix

Request permission.

## Example

```dart
LocationPermission permission = await Geolocator.requestPermission();
```
