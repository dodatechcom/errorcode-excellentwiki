---
title: "[Solution] ETIMEDOUT — Connection Timed Out in Node.js"
description: "Fix ETIMEDOUT when TCP connection takes too long. Increase timeout, check network, and verify DNS resolution."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# ETIMEDOUT — Connection Timed Out

TCP connection could not be established within the timeout.

## Fixes

```javascript
// Increase timeout in http request
const http = require('http');
const req = http.get(url, { timeout: 30000 }, (res) => {
  // ...
});

req.on('timeout', () => {
  req.destroy();
});
```

## Diagnose

```bash
timeout 5 curl -v https://target-server.com
nslookup target-server.com
```
