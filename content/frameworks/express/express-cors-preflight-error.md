---
title: "[Solution] Express CORS Preflight Error"
description: "Fix Express CORS preflight errors when OPTIONS requests are not handled before route handlers."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

A CORS preflight error in Express occurs when the browser sends an OPTIONS request to check CORS permissions but the server does not handle it, causing the actual request to be blocked.

## Common Causes

- OPTIONS method not handled by any route
- `cors` middleware not applied before route definitions
- Custom middleware chain does not include OPTIONS handling
- Preflight response missing required headers
- Non-simple request triggers preflight but route does not support OPTIONS

## How to Fix

1. Apply the `cors` middleware before all routes:

```javascript
const cors = require('cors');

app.use(cors({
  origin: 'https://myapp.com',
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
  allowedHeaders: ['Content-Type', 'Authorization', 'X-Requested-With'],
  credentials: true
}));
```

2. Handle OPTIONS requests explicitly for specific routes:

```javascript
app.options('/api/data', cors());

app.route('/api/data')
  .get((req, res) => res.json({ data: 'get' }))
  .post((req, res) => res.json({ data: 'post' }));
```

3. Add a catch-all OPTIONS handler:

```javascript
app.options('*', cors());

// Or manual handler
app.options('*', (req, res) => {
  res.set({
    'Access-Control-Allow-Origin': 'https://myapp.com',
    'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    'Access-Control-Max-Age': '86400'
  });
  res.sendStatus(204);
});
```

## Examples

```javascript
// Bug: no OPTIONS handling
app.post('/api/data', (req, res) => {
  res.json({ received: req.body });
});

// Browser sends preflight OPTIONS /api/data
// Server returns 404 -- actual POST is blocked

// Fixed: cors() handles OPTIONS automatically
app.use(cors({ origin: 'https://myapp.com' }));
app.post('/api/data', (req, res) => {
  res.json({ received: req.body });
});
```

```text
Access to XMLHttpRequest at 'http://localhost:5000/api/data' from origin
'https://myapp.com' has been blocked by CORS policy: Method POST is not
allowed by Access-Control-Allow-Methods in preflight response.
```
