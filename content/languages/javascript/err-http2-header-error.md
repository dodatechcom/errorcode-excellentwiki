---
title: "[Solution] Node.js ERR_HTTP2_HEADER_ERROR — HTTP/2 Header Error Fix"
description: "Fix Node.js ERR_HTTP2_HEADER_ERROR when invalid headers are sent in an HTTP/2 connection. Follow HTTP/2 header rules and constraints."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Node.js ERR_HTTP2_HEADER_ERROR — HTTP/2 Header Error Fix

The `ERR_HTTP2_HEADER_ERROR` error occurs when invalid headers are sent over an HTTP/2 connection. HTTP/2 has stricter header rules than HTTP/1.1, including case-insensitive header names and specific requirements for pseudo-headers.

## Description

Common ERR_HTTP2_HEADER_ERROR messages include:

- `ERR_HTTP2_HEADER_ERROR: Invalid header name` — header name violates HTTP/2 rules.
- `Invalid header value` — header value contains invalid characters.
- `Pseudo-header in regular header position` — pseudo-headers mixed with regular headers.

## Common Causes

```javascript
const http2 = require("node:http2");

// Cause 1: Invalid header characters
const client = http2.connect("https://localhost:3000");
const req = client.request({
  ":path": "/api",
  "x-data": "value\u0000invalid", // null byte
});

// Cause 2: Pseudo-headers after regular headers
stream.respond({
  "content-type": "application/json", // regular header first
  ":status": 200, // pseudo-header after — error
});

// Cause 3: Uppercase header names
stream.respond({
  ":status": 200,
  "Content-Type": "text/plain", // should be lowercase
});

// Cause 4: Empty header value when required
stream.respond({
  ":status": 200,
  "authorization": "", // empty value
});
```

## Solutions

### Fix 1: Use lowercase header names

```javascript
const http2 = require("node:http2");

const server = http2.createServer();
server.on("stream", (stream, headers) => {
  stream.respond({
    ":status": 200,
    "content-type": "application/json", // lowercase
    "x-request-id": "abc123", // lowercase
    "cache-control": "no-cache", // lowercase
  });
  stream.end(JSON.stringify({ status: "ok" }));
});
```

### Fix 2: Send pseudo-headers first

```javascript
const http2 = require("node:http2");

const client = http2.connect("https://localhost:3000");

// Correct order: pseudo-headers first, then regular headers
const req = client.request({
  ":path": "/api", // pseudo-header first
  ":method": "GET", // pseudo-header first
  ":authority": "localhost:3000", // pseudo-header first
  "accept": "application/json", // regular header after
  "authorization": "Bearer token123", // regular header after
});

req.on("response", (headers) => {
  console.log("Response headers:", headers);
});
req.end();
```

### Fix 3: Sanitize header values

```javascript
const http2 = require("node:http2");

function sanitizeHttp2Headers(headers) {
  const sanitized = {};
  for (const [key, value] of Object.entries(headers)) {
    if (typeof value !== "string") continue;
    // Remove control characters
    const cleanValue = value.replace(/[\x00-\x08\x0a-\x1f\x7f]/g, "");
    if (cleanValue.length === 0) continue;
    sanitized[key.toLowerCase()] = cleanValue;
  }
  return sanitized;
}

const server = http2.createServer();
server.on("stream", (stream, headers) => {
  const responseHeaders = sanitizeHttp2Headers({
    ":status": 200,
    "content-type": "application/json",
    "x-data": headers["x-data"],
  });
  stream.respond(responseHeaders);
  stream.end("OK");
});
```

### Fix 4: Handle header errors on client

```javascript
const http2 = require("node:http2");

const client = http2.connect("https://localhost:3000");
const req = client.request({ ":path": "/api" });

req.on("error", (err) => {
  if (err.code === "ERR_HTTP2_HEADER_ERROR") {
    console.error("Header error:", err.message);
    // Fix the headers and retry
  }
});

req.end();
```

## Examples

```javascript
const http2 = require("node:http2");

// ERR_HTTP2_HEADER_ERROR from mixed header types
const server = http2.createServer();
server.on("stream", (stream, headers) => {
  // Wrong: pseudo-header after regular headers
  try {
    stream.respond({
      "content-type": "text/plain",
      ":status": 200,
    });
  } catch (err) {
    console.error(err.code); // ERR_HTTP2_HEADER_ERROR
  }

  // Correct: pseudo-headers first
  stream.respond({
    ":status": 200,
    "content-type": "text/plain",
  });
  stream.end("Hello");
});
```

## Related Errors

- [ERR_HTTP2_PSEUDO_HEADERS]({{< relref "/languages/javascript/err-http2-pseudo-headers" >}}) — invalid pseudo-headers.
- [ERR_HTTP2_COMPRESS_HEADERS]({{< relref "/languages/javascript/err-http2-compress-headers" >}}) — header compression failed.
- [ERR_HTTP2_MAX_HEADERS]({{< relref "/languages/javascript/err-http2-max-headers" >}}) — too many headers.
- [ERR_HTTP2_FRAME_ERROR]({{< relref "/languages/javascript/err-http2-frame-error" >}}) — invalid frame received.
