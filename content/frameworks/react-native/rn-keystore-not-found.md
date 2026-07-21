---
title: "[Solution] React Native Keystore Not Found"
description: "Release keystore missing."
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

Release keystore missing.

## Common Causes

Wrong path.

## How to Fix

Check path.

## Example

```bash
keytool -list -v -keystore release.keystore
```
