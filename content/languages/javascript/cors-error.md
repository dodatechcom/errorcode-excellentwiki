---
title: "[Solution] JavaScript CORS Error — Blocked by CORS Policy Fix"
description: "Fix JavaScript CORS (Cross-Origin Resource Sharing) errors. Configure Access-Control-Allow-Origin headers on server and use proxies for development."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
tags: ["cors", "cross-origin", "blocked", "access-control"]
weight: 100
---

# CORS Error — Blocked by CORS Policy Fix

A CORS (Cross-Origin Resource Sharing) error is thrown when the browser blocks a JavaScript request to a different origin (domain, port, or protocol) because the server did not return the required `Access-Control-Allow-*` headers. CORS is enforced by the browser only — it does not affect server-to-server requests.

## Description

Common CORS error messages include:

- `Access to XMLHttpRequest at 'https://api.example.com' from origin 'http://localhost:3000' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.`
- `Response to preflight request does not pass access control check: It does not have HTTP ok status.`
- `Access to fetch at 'https://api.example.com' from origin 'http://localhost:3000' has been blocked by CORS policy: The status code of the response is not ok (403).`

Browsers send a `OPTIONS` preflight request for non-simple requests. The server must respond with the correct CORS headers for both the preflight and the actual request.

## Common Causes

```javascript
// Cause 1: Server does not return Access-Control-Allow-Origin header
fetch("https://api.example.com/data")
    .then(res => res.json())
    .then(data => console.log(data))
    .catch(err => console.error(err));  // CORS error in browser console

// Cause 2: Server only allows specific origins and your origin is not included
// Server sends: Access-Control-Allow-Origin: https://production.example.com
// But you are on: http://localhost:3000

// Cause 3: Missing headers for non-simple requests
// Browser sends preflight OPTIONS but server returns 404 or 405

// Cause 4: Credentials mode mismatch
fetch("https://api.example.com/data", {
    credentials: "include",  // sends cookies
    // but server does not send Access-Control-Allow-Credentials: true
});

// Cause 5: Server returns wrong Content-Type for preflight
// Server responds to OPTIONS with Content-Type: text/html instead of 204
```

## Solutions

### Fix 1: Configure CORS headers on Express (Node.js)

```javascript
// Wrong - no CORS headers, browser blocks the response
const express = require("express");
const app = express();

app.get("/api/data", (req, res) => {
    res.json({ message: "hello" });
});

app.listen(3000);

// Correct - use the cors middleware
const express = require("express");
const cors = require("cors");
const app = express();

// Allow all origins (development only)
app.use(cors());

// Or configure specific origins
app.use(cors({
    origin: ["http://localhost:3000", "https://myapp.com"],
    methods: ["GET", "POST", "PUT", "DELETE"],
    allowedHeaders: ["Content-Type", "Authorization"],
    credentials: true,
}));

app.get("/api/data", (req, res) => {
    res.json({ message: "hello" });
});

app.listen(3000);
```

```bash
npm install cors
```

### Fix 2: Set CORS headers manually without middleware

```javascript
// Express without the cors package
app.use((req, res, next) => {
    res.header("Access-Control-Allow-Origin", "http://localhost:3000");
    res.header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS");
    res.header("Access-Control-Allow-Headers", "Content-Type, Authorization");

    if (req.method === "OPTIONS") {
        return res.sendStatus(204);  // respond to preflight
    }
    next();
});
```

### Fix 3: Use a development proxy instead of enabling CORS

```javascript
// package.json - proxy field (Create React App)
{
    "proxy": "http://localhost:8080"
}

// vite.config.js
export default {
    server: {
        proxy: {
            "/api": {
                target: "http://localhost:8080",
                changeOrigin: true,
            },
        },
    },
};
```

```bash
# Or use http-proxy-middleware in custom server setup
npm install http-proxy-middleware
```

### Fix 4: Configure CORS in Flask (Python backend)

```python
# Wrong - no CORS headers
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/data")
def data():
    return jsonify({"message": "hello"})

# Correct - use flask-cors
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])

@app.route("/api/data")
def data():
    return jsonify({"message": "hello"})
```

```bash
pip install flask-cors
```

### Fix 5: Fix credentials mode with correct headers

```javascript
// Wrong - browser sends cookies but server rejects them
fetch("https://api.example.com/data", {
    credentials: "include",
});

// Server must respond with both:
// Access-Control-Allow-Origin: http://localhost:3000  (must be specific, not *)
// Access-Control-Allow-Credentials: true
```

```javascript
// Server-side (Express) - correct for credentials
app.use(cors({
    origin: "http://localhost:3000",  // specific origin required
    credentials: true,                // Access-Control-Allow-Credentials: true
}));
```

### Fix 6: Use mode: 'cors' explicitly in fetch

```javascript
// Fetch defaults to 'same-origin' mode - cross-origin requests need explicit mode
fetch("https://api.example.com/data", {
    mode: "cors",
    headers: {
        "Content-Type": "application/json",
    },
});
```

## Debugging Checklist

```bash
# Test CORS headers directly with curl
curl -I -X OPTIONS https://api.example.com/data \
  -H "Origin: http://localhost:3000" \
  -H "Access-Control-Request-Method: GET"

# Look for these headers in the response:
# Access-Control-Allow-Origin: http://localhost:3000
# Access-Control-Allow-Methods: GET, POST, PUT, DELETE
# Access-Control-Allow-Headers: Content-Type, Authorization
```

- Open browser DevTools, Network tab, and look at the failing request headers.
- Check both the preflight (OPTIONS) and the actual (GET/POST) response.
- Verify the `Origin` header the browser sends matches what the server expects.
- Remember: CORS is enforced by browsers, not by curl, Postman, or server-to-server calls.

## Related Errors

- [TypeError (Failed to fetch)](typeerror) — network failure without CORS headers.
- [ERR_BLOCKED_BY_RESPONSE](#) — browser blocked due to X-Frame-Options or CORB.
- [403 Forbidden](#) — server explicitly rejects the request (not a CORS issue).
