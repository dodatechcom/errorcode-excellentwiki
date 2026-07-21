---
title: "[Solution] react-native Networking Error Timeout"
description: "Network request timing out."
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

Network request timing out.

## Common Causes

Server too slow.

## How to Fix

Increase timeout.

## Example

```javascript
const controller = new AbortController();
setTimeout(() => controller.abort(), 10000);
const r = await fetch(url, { signal: controller.signal });
```
