---
title: "[Solution] flutter Package Info Error"
description: "Package info not loading."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

Package info not loading.

## Common Causes

Not available.

## How to Fix

Use PackageInfo.

## Example

```dart
final info = await PackageInfo.fromPlatform();
print(info.version);
```
