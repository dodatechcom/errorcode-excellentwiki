---
title: "[Solution] react-native Native Crash Android"
description: "Android native crash."
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

Android native crash.

## Common Causes

Wrong native code.

## How to Fix

Check Logcat.

## Example

```bash
adb logcat | grep -i crash
```
