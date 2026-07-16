---
title: "[Solution] JavaScript TypeError: Failed to fetch — Network Error Fix"
description: "Fix JavaScript TypeError: Failed to fetch network error. Handle CORS, check network connectivity, validate URLs, and implement retry logic."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
tags: ["failed-to-fetch", "network-error", "fetch", "cors", "connectivity"]
weight: 5
---

# TypeError: Failed to fetch

A `TypeError: Failed to fetch` is thrown when the `fetch()` API cannot complete a network request. The error is intentionally vague for security reasons — it doesn't reveal whether the failure was due to network issues, CORS, DNS resolution, or server errors. The actual cause must be investigated through other means.

## Description

`Failed to fetch` is a blanket error that covers many network-level failures. Browsers intentionally hide the real reason to prevent information leakage. Common underlying causes:

- Network is offline or unreachable
- CORS policy blocking the request (most common in development)
- DNS resolution failure
- SSL/TLS certificate errors
- Server not running or wrong URL
- Request blocked by browser extension or firewall

## Common Causes

```javascript
// Cause 1: CORS policy blocking request
fetch("https://api.otherdomain.com/data")
    .then(res => res.json())
    .catch(err => console.error(err));  // TypeError: Failed to fetch (CORS)

// Cause 2: Network is offline
// Turn off Wi-Fi, then:
fetch("/api/data")
    .catch(err => console.error(err));  // TypeError: Failed to fetch

// Cause 3: Wrong URL or server not running
fetch("http://localhost:9999/api")
    .catch(err => console.error(err));  // TypeError: Failed to fetch

// Cause 4: Mixed content (HTTP on HTTPS page)
// On https://example.com:
fetch("http://api.example.com/data")
    .catch(err => console.error(err));  // TypeError: Failed to fetch

// Cause 5: Redirect to a CORS-incompatible URL
fetch("https://api.example.com/redirect-to-cors-blocked-url")
    .catch(err => console.error(err));
```

## How to Fix

### Fix 1: Check if it's a CORS issue first

```bash
# Test the URL directly with curl to see the actual response
curl -I -X OPTIONS https://api.example.com/data \
  -H "Origin: http://localhost:3000" \
  -H "Access-Control-Request-Method: GET"

# Look for Access-Control-Allow-Origin header in response
```

```javascript
// Add CORS headers on your server (Node.js/Express)
const cors = require("cors");
app.use(cors({
    origin: ["http://localhost:3000"],
    methods: ["GET", "POST", "PUT", "DELETE"],
}));
```

### Fix 2: Add detailed error logging

```javascript
// Wrong — generic error message
try {
    const res = await fetch("/api/data");
    const data = await res.json();
} catch (err) {
    console.error(err);  // Just "Failed to fetch"
}

// Correct — log useful context
try {
    const res = await fetch("/api/data", {
        method: "GET",
        headers: { "Content-Type": "application/json" },
    });
    if (!res.ok) {
        throw new Error(`HTTP ${res.status}: ${res.statusText}`);
    }
    const data = await res.json();
} catch (err) {
    console.error("Fetch failed:", {
        message: err.message,
        name: err.name,
        stack: err.stack,
    });
}
```

### Fix 3: Implement retry with exponential backoff

```javascript
async function fetchWithRetry(url, options = {}, maxRetries = 3) {
    for (let attempt = 1; attempt <= maxRetries; attempt++) {
        try {
            const response = await fetch(url, options);
            if (!response.ok) {
                throw new Error(`HTTP ${response.status}`);
            }
            return response;
        } catch (err) {
            if (attempt === maxRetries) throw err;
            const delay = Math.min(1000 * Math.pow(2, attempt), 10000);
            console.warn(`Retry ${attempt}/${maxRetries} after ${delay}ms: ${err.message}`);
            await new Promise(resolve => setTimeout(resolve, delay));
        }
    }
}

// Usage
const data = await fetchWithRetry("/api/data").then(r => r.json());
```

### Fix 4: Use a proxy in development

```javascript
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

// package.json (Create React App)
{
    "proxy": "http://localhost:8080"
}
```

### Fix 5: Check for mixed content issues

```javascript
// Wrong — HTTP request from HTTPS page
fetch("http://api.example.com/data");  // Blocked: mixed content

// Correct — use HTTPS
fetch("https://api.example.com/data");

// Or use protocol-relative URL
fetch("//api.example.com/data");
```

## Examples

This error commonly occurs when:

- Making API calls from `localhost:3000` to a backend on a different port without CORS
- Testing in an environment without network access
- The backend server isn't running or is on the wrong port
- A service worker intercepts and fails the request

## Related Errors

- [CORS Error](cors-error) — specific CORS policy violation message
- [Uncaught (in promise) TypeError](uncaught-promise) — unhandled rejection from Failed to fetch
- [DOMException](dom-exception) — related security context errors
