---
title: "[Solution] Vercel CORS Error"
description: "Fix Vercel CORS errors when cross-origin requests are blocked by the server."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vercel CORS Error

Vercel API routes block cross-origin requests due to missing CORS headers.

```
Access to fetch from origin has been blocked by CORS policy
```

## Common Causes

- CORS headers not set in API response
- Preflight OPTIONS request not handled
- Origin not in allowed list
- Credentials not supported with wildcard origin
- Headers missing from response

## How to Fix

### Add CORS Headers

```javascript
// pages/api/cors.js
export default function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');

  if (req.method === 'OPTIONS') {
    res.status(200).end();
    return;
  }

  res.status(200).json({ message: 'OK' });
}
```

### Create CORS Middleware

```javascript
// lib/cors.js
export function setCorsHeaders(res, origin = '*') {
  res.setHeader('Access-Control-Allow-Origin', origin);
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');
  res.setHeader('Access-Control-Max-Age', '86400');
}

export default function cors(handler) {
  return async (req, res) => {
    setCorsHeaders(res, req.headers.origin);
    if (req.method === 'OPTIONS') {
      return res.status(200).end();
    }
    return handler(req, res);
  };
}
```

### Restrict Origin

```javascript
const allowedOrigins = ['https://app.example.com'];

export default function handler(req, res) {
  const origin = req.headers.origin;
  if (allowedOrigins.includes(origin)) {
    res.setHeader('Access-Control-Allow-Origin', origin);
  }
  // ...
}
```

## Examples

```javascript
// Using with credentials
res.setHeader('Access-Control-Allow-Origin', 'https://app.example.com');
res.setHeader('Access-Control-Allow-Credentials', 'true');
// Note: Cannot use '*' with credentials
```
