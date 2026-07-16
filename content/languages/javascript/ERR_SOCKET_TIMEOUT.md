---
title: "[Solution] Node.js ERR_SOCKET_TIMEOUT — Socket Timeout Fix"
description: "Fix Node.js ERR_SOCKET_TIMEOUT by increasing timeout values, checking server health, using keep-alive connections, and proper error handling."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
tags: ["err-socket-timeout", "timeout", "network", "keep-alive", "nodejs"]
weight: 85
---

# Node.js ERR_SOCKET_TIMEOUT — Socket Timeout Fix

The `ERR_SOCKET_TIMEOUT` error in Node.js occurs when a socket connection does not receive a response within the configured timeout period. This commonly happens with HTTP requests to slow APIs, database connections, or during network instability. The default socket timeout in Node.js is 120 seconds (2 minutes), but many servers close idle connections sooner.

## Common Causes

```javascript
// Cause 1: Default http/https agent timeout too short
const http = require("http");
http.get("http://slow-server.example.com/large-data", (res) => {
    res.on("data", () => {});
});  // ERR_SOCKET_TIMEOUT after 120s

// Cause 2: Fetch with no AbortController timeout
const response = await fetch("https://api.example.com/data");  // no timeout set

// Cause 3: Too many concurrent connections exhausting the socket pool
for (let i = 0; i < 1000; i++) {
    fetch("https://api.example.com/item/" + i);  // socket pool exhausted
}

// Cause 4: Server closes idle connections before client timeout
const agent = new http.Agent({ keepAlive: false });  // no keep-alive

// Cause 5: DNS resolution delays
const response = await fetch("http://internal-service.local:8080");  // slow DNS
```

## Solutions

### Fix 1: Increase socket timeout for long-running requests

```javascript
// Wrong — no timeout configuration
const http = require("http");
http.get("http://api.example.com/large-export", (res) => {
    // may time out on large responses
});

// Correct — set appropriate timeout
const http = require("http");
const req = http.get("http://api.example.com/large-export", (res) => {
    res.on("data", (chunk) => { /* process data */ });
    res.on("end", () => { /* done */ });
});
req.setTimeout(300000, () => {  // 5 minutes
    req.destroy(new Error("Request timed out after 5 minutes"));
});
```

### Fix 2: Use AbortController with fetch for controlled timeouts

```javascript
// Wrong — no timeout on fetch
async function fetchData(url) {
    const response = await fetch(url);
    return response.json();
}

// Correct — abort after timeout
async function fetchData(url, timeoutMs = 30000) {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), timeoutMs);

    try {
        const response = await fetch(url, { signal: controller.signal });
        clearTimeout(timeoutId);
        return await response.json();
    } catch (err) {
        clearTimeout(timeoutId);
        if (err.name === "AbortError") {
            throw new Error(`Request to ${url} timed out after ${timeoutMs}ms`);
        }
        throw err;
    }
}
```

### Fix 3: Configure keep-alive agent for repeated connections

```javascript
// Wrong — default agent creates a new connection each time
const response = await fetch("https://api.example.com/data");

// Correct — use a keep-alive agent
const https = require("https");
const agent = new https.Agent({
    keepAlive: true,
    keepAliveMsecs: 30000,
    maxSockets: 50,
    maxFreeSockets: 10,
    timeout: 60000,
});

const response = await fetch("https://api.example.com/data", {
    agent,
});
```

### Fix 4: Implement retry with exponential backoff

```javascript
// Correct — retry on socket timeout
async function fetchWithRetry(url, options = {}, retries = 3) {
    const { timeoutMs = 30000, backoffMs = 1000, ...fetchOptions } = options;

    for (let attempt = 0; attempt <= retries; attempt++) {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), timeoutMs);

        try {
            const response = await fetch(url, {
                ...fetchOptions,
                signal: controller.signal,
            });
            clearTimeout(timeoutId);
            return response;
        } catch (err) {
            clearTimeout(timeoutId);
            if (err.name === "AbortError" && attempt < retries) {
                const delay = backoffMs * Math.pow(2, attempt);
                console.warn(`Attempt ${attempt + 1} timed out, retrying in ${delay}ms...`);
                await new Promise(r => setTimeout(r, delay));
                continue;
            }
            throw err;
        }
    }
}

// Usage
const data = await fetchWithRetry("https://api.example.com/slow-endpoint", {
    timeoutMs: 60000,
    retries: 3,
});
```

### Fix 5: Set global default timeout for http/https agents

```javascript
// Set global defaults for all outgoing connections
const http = require("http");
const https = require("https");

http.globalAgent.timeout = 60000;       // 60 seconds
http.globalAgent.keepAlive = true;
https.globalAgent.timeout = 60000;
https.globalAgent.keepAlive = true;

// For individual requests, override with a custom agent
const agent = new https.Agent({
    timeout: 120000,  // 2 minutes for this specific request
    rejectUnauthorized: true,
});
```

### Fix 6: Monitor and log socket timeout events

```javascript
// Track timeout events for debugging
const agent = new https.Agent({
    keepAlive: true,
    timeout: 30000,
});

agent.on("timeout", (socket) => {
    console.error("Socket timeout event:", {
        remoteAddress: socket.remoteAddress,
        remotePort: socket.remotePort,
    });
});

agent.on("free", (socket) => {
    // connection was released back to the pool
});
```

## Quick Reference

| Scenario | Recommended Timeout |
|---|---|
| Simple API calls | 10-30 seconds |
| Large data downloads | 5-10 minutes |
| WebSocket connections | Use ping/pong, not socket timeout |
| Database queries | 30-60 seconds |
| File uploads | 5-15 minutes depending on size |

## Prevention Tips

- Always set timeouts on HTTP requests — never rely on the default 120 seconds.
- Use `AbortController` with `fetch()` for modern timeout handling.
- Use keep-alive agents for services with repeated connections.
- Implement retry logic with exponential backoff for transient network failures.
- Monitor socket timeout events to identify slow endpoints.

## Related Errors

- [ERR_MODULE_NOT_FOUND](ERR_MODULE_NOT_FOUND) — Node.js module resolution error.
- [TypeError](typeerror) — value is not the expected type.
- [RangeError](rangeerror) — value outside valid range.
