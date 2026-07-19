---
title: "[Solution] Socket Hang Up — ERR_SOCKET_HANG_UP Fix"
description: "Fix ERR_SOCKET_HANG_UP when the server closes the connection before a response is received."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Socket Hang Up

The server closed the TCP socket before sending a response.

## Causes

- Server timeout
- Request body too large
- Server crashed during processing

## Fix

```javascript
// Use AbortController with timeout
const controller = new AbortController();
setTimeout(() => controller.abort(), 30000);

const res = await fetch(url, { signal: controller.signal });
```
