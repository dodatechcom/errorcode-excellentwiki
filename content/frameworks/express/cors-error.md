---
title: "CORS policy error"
description: "Express returns a CORS error when the request origin is not in the allowed list"
frameworks: ["express"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when a browser blocks a cross-origin request because the Express server's CORS policy does not allow the requesting origin. This is enforced by the browser, not the server.

## Common Causes

- Origin not included in `Access-Control-Allow-Origin` header
- Preflight OPTIONS request not handled
- Credentials mode (`withCredentials`) used with wildcard `*` origin
- Missing required CORS headers in the response

## How to Fix

1. Use the `cors` middleware with explicit origins:

```javascript
const cors = require('cors');

app.use(cors({
  origin: ['http://localhost:3000', 'https://myapp.com'],
  credentials: true
}));
```

2. Handle preflight OPTIONS requests:

```javascript
app.options('/api/data', cors());
```

3. Set per-route CORS configuration:

```javascript
app.get('/api/public', cors({ origin: '*' }), (req, res) => {
  res.json({ data: 'public' });
});
```

4. Allow credentials with specific origins (not `*`):

```javascript
app.use(cors({
  origin: 'https://myapp.com',
  credentials: true,
  methods: ['GET', 'POST', 'PUT', 'DELETE']
}));
```

## Examples

```javascript
// Client at http://localhost:3000
fetch('http://localhost:5000/api/data', {
  credentials: 'include'
})
// Blocked by CORS policy: No 'Access-Control-Allow-Origin' header
```

```text
Access to fetch at 'http://localhost:5000/api/data' from origin 'http://localhost:3000'
has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present
```

## Related Errors

- [Error: Cannot set headers after they are sent]({{< relref "/frameworks/express/cannot-set-headers" >}})
