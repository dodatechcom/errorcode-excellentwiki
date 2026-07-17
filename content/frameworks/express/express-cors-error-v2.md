---
title: "CORS: No Access-Control-Allow-Origin Header"
description: "Fix Express CORS errors when browsers block cross-origin requests due to missing or misconfigured CORS headers."
frameworks: ["express.js"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["cors", "access-control", "origin", "browser", "express"]
weight: 5
---

## What This Error Means

When a browser makes a cross-origin request (e.g., from `localhost:3000` to `localhost:8080`), the server must respond with an `Access-Control-Allow-Origin` header. Without it, the browser blocks the response. This is not a server error but a browser security policy enforced by the Same-Origin Policy.

## Common Causes

- CORS middleware is not installed or not registered
- CORS middleware is registered after the routes it should protect
- Origin is restricted and does not match the requesting domain
- Preflight `OPTIONS` request is not handled
- Credentials mode requires specific CORS configuration

## How to Fix

### Install and Enable CORS Middleware

```javascript
const cors = require('cors');

// Allow all origins (development only)
app.use(cors());

// Allow specific origins (production)
app.use(cors({
  origin: ['https://yourdomain.com', 'https://app.yourdomain.com'],
  methods: ['GET', 'POST', 'PUT', 'DELETE'],
  credentials: true
}));
```

### Register CORS Before Routes

```javascript
const cors = require('cors');

app.use(cors()); // Must come before routes
app.use(express.json());

app.get('/api/data', (req, res) => {
  res.json({ data: 'success' });
});
```

### Handle Preflight Requests

```javascript
app.options('*', cors()); // Enable preflight for all routes

// Or manually handle OPTIONS
app.options('/api/data', (req, res) => {
  res.header('Access-Control-Allow-Origin', 'https://yourdomain.com');
  res.header('Access-Control-Allow-Methods', 'GET,POST,PUT,DELETE');
  res.header('Access-Control-Allow-Headers', 'Content-Type,Authorization');
  res.sendStatus(204);
});
```

### Configure Credentials Properly

```javascript
app.use(cors({
  origin: 'https://yourdomain.com',
  credentials: true // Required for cookies/auth headers
}));
```

## Related Errors

- [Express 404 Route Not Found]({{< relref "/frameworks/express/express-404-error-v2" >}}) — undefined route
- [Express JWT Error]({{< relref "/frameworks/express/express-jwt-error-v2" >}}) — authentication failure
