---
title: "[Solution] Fetch Failed — ERR_CONNECTION_REFUSED in Browser"
description: "Fix FetchError when fetch() fails with ERR_CONNECTION_REFUSED. Check server is running and CORS config."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Fetch Failed — Connection Refused

```javascript
fetch('http://localhost:3000/api')
  .catch(err => {
    // TypeError: Failed to fetch
    console.error('Connection refused:', err.message);
  });
```

## Causes

1. Server not running on that port
2. CORS blocking the request
3. Mixed content (HTTPS page → HTTP request)
4. Network proxy intercepting

## Fix

```javascript
// Verify server is running
const res = await fetch('http://localhost:3000/api');
if (!res.ok) throw new Error(`HTTP ${res.status}`);
```
