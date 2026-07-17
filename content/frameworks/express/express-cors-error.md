---
title: "[Solution] Express CORS Error — CORS error"
description: "Fix Express CORS errors. Resolve Cross-Origin Resource Sharing issues."
frameworks: ["express"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

An Express CORS error occurs when the browser blocks cross-origin requests due to missing or incorrect CORS headers from the server.

## Common Causes

- CORS headers not set on the server
- Origin not in the allowed list
- Preflight (OPTIONS) request not handled
- Credentials mode with wildcard origin
- Wrong HTTP methods in Access-Control-Allow-Methods

## How to Fix

### Install and Configure CORS Middleware

```javascript
const cors = require('cors');
app.use(cors());
```

### Configure Specific Origins

```javascript
app.use(cors({
  origin: 'http://localhost:3000',
  methods: ['GET', 'POST', 'PUT', 'DELETE'],
  credentials: true,
}));
```

### Handle Preflight Requests

```javascript
app.options('*', cors());
```

### Set Headers Manually

```javascript
app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', 'http://localhost:3000');
  res.header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
  res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization');
  next();
});
```

## Examples

```javascript
// Example 1: CORS blocked
// Access to XMLHttpRequest blocked by CORS policy
// Fix: app.use(cors())

// Example 2: Credentials with wildcard
cors({ origin: '*', credentials: true })
// Fix: use specific origin
cors({ origin: 'https://example.com', credentials: true })
```

## Related Errors

- [Express Middleware Error]({{< relref "/frameworks/express/express-middleware-error" >}}) — middleware error
- [Express JWT Error]({{< relref "/frameworks/express/express-jwt-error" >}}) — JWT verification error
