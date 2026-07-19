---
title: "[Solution] ERR_SOCKET_CLOSED_BEFORE_CONNECTION — Socket Error Fix"
description: "Fix ERR_SOCKET_CLOSED_BEFORE_CONNECTION when a socket is destroyed before connecting."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# ERR_SOCKET_CLOSED Before Connection

A socket was destroyed before the connection was established.

## Causes

- Request aborted by client
- Timeout mechanism fired
- Server closed connection immediately

```javascript
// Ensure proper error handling
const http = require('http');
const req = http.get(url, (res) => { ... });
req.on('error', (err) => {
  console.error('Request failed:', err.message);
});
```
