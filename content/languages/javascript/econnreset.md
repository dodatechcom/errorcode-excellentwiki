---
title: "[Solution] ECONNRESET — Connection Reset by Peer in Node.js"
description: "Fix ECONNRESET when a connection is forcibly closed by the remote server. Implement retries and handle timeouts."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# ECONNRESET — Connection Reset by Peer

The remote server closed the connection unexpectedly.

## Causes

- Server restarted or went down
- Proxy timeout
- Keep-alive timeout
- Load balancer terminated the connection

## Fix

```javascript
const http = require('http');
const agent = new http.Agent({ keepAlive: true, maxSockets: 10 });

// Add retry logic
async function fetchWithRetry(url, retries = 3) {
  for (let i = 0; i < retries; i++) {
    try {
      const res = await fetch(url, { agent });
      return await res.json();
    } catch (err) {
      if (i === retries - 1) throw err;
      await new Promise(r => setTimeout(r, 1000 * (i + 1)));
    }
  }
}
```
