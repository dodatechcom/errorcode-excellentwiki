---
title: "[Solution] Node.js ERR_HTTP1_HEADER_RE_ASSIGNMENT — Header Re-Assignment Fix"
description: "Fix Node.js ERR_HTTP1_HEADER_RE_ASSIGNMENT when attempting to assign an HTTP header that has already been set. Use append for multiple values."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Node.js ERR_HTTP1_HEADER_RE_ASSIGNMENT — Header Re-Assignment Fix

The `ERR_HTTP1_HEADER_RE_ASSIGNMENT` error occurs when attempting to reassign an HTTP header that has already been set using `writeHead()`. HTTP/1.1 headers set via `writeHead()` cannot be overwritten directly.

## Description

Common ERR_HTTP1_HEADER_RE_ASSIGNMENT messages include:

- `ERR_HTTP1_HEADER_RE_ASSIGNMENT: Header already set` — header was already assigned.
- `Can't set headers after they are sent` — attempting to modify sent headers.
- `Header re-assignment` — trying to overwrite an existing header.

## Common Causes

```javascript
const http = require("node:http");

// Cause 1: Calling writeHead twice with same header
const server = http.createServer((req, res) => {
  res.writeHead(200, { "Content-Type": "text/plain" });
  res.writeHead(200, { "Content-Type": "application/json" }); // ERR_HTTP1_HEADER_RE_ASSIGNMENT
  res.end("OK");
});

// Cause 2: Setting header after writeHead
res.writeHead(200);
res.setHeader("Content-Type", "text/plain"); // ERR_HTTP1_HEADER_RE_ASSIGNMENT

// Cause 3: Multiple writeHead calls in conditional logic
server.on("request", (req, res) => {
  if (req.url === "/a") {
    res.writeHead(200, { "X-Type": "a" });
  }
  if (req.url === "/b") {
    res.writeHead(200, { "X-Type": "b" }); // ERR_HTTP1_HEADER_RE_ASSIGNMENT
  }
});
```

## Solutions

### Fix 1: Set all headers in a single writeHead call

```javascript
const http = require("node:http");

const server = http.createServer((req, res) => {
  // Combine all headers in one writeHead call
  res.writeHead(200, {
    "Content-Type": "application/json",
    "X-Custom": "value",
    "Cache-Control": "no-cache",
  });
  res.end(JSON.stringify({ status: "ok" }));
});
```

### Fix 2: Use setHeader before writeHead

```javascript
const http = require("node:http");

const server = http.createServer((req, res) => {
  // Set headers individually BEFORE writeHead
  res.setHeader("Content-Type", "text/plain");
  res.setHeader("X-Custom", "value");
  res.setHeader("Cache-Control", "no-cache");

  // writeHead sends all accumulated headers
  res.writeHead(200);
  res.end("Hello");
});
```

### Fix 3: Handle conditional responses properly

```javascript
const http = require("node:http");

const server = http.createServer((req, res) => {
  // Set default headers first
  const headers = { "Content-Type": "text/plain" };

  // Add conditional headers
  if (req.url === "/a") {
    headers["X-Type"] = "a";
  } else if (req.url === "/b") {
    headers["X-Type"] = "b";
  }

  // Single writeHead call with all headers
  res.writeHead(200, headers);
  res.end("OK");
});
```

### Fix 4: Use res.getHeader to check before setting

```javascript
const http = require("node:http");

function safeSetHeader(res, name, value) {
  const existing = res.getHeader(name);
  if (existing !== undefined) {
    // Header already exists — use append instead
    res.appendHeader(name, value);
  } else {
    res.setHeader(name, value);
  }
}

const server = http.createServer((req, res) => {
  safeSetHeader(res, "X-Custom", "first");
  safeSetHeader(res, "X-Custom", "second"); // appends instead of error
  res.writeHead(200);
  res.end("OK");
});
```

## Examples

```javascript
const http = require("node:http");

// ERR_HTTP1_HEADER_RE_ASSIGNMENT example
const server = http.createServer((req, res) => {
  res.writeHead(200, { "Content-Type": "text/plain" });

  // This will throw ERR_HTTP1_HEADER_RE_ASSIGNMENT
  try {
    res.writeHead(200, { "Content-Type": "application/json" });
  } catch (err) {
    console.error(err.code); // ERR_HTTP1_HEADER_RE_ASSIGNMENT
    // Use existing headers instead
  }

  res.end("Hello");
});
```

## Related Errors

- [ERR_HTTP1_HEADER_PARSING]({{< relref "/languages/javascript/err-http1-header-parsing" >}}) — header parsing failed.
- [ERR_HTTP1_STATUS_CODE]({{< relref "/languages/javascript/err-http1-status-code" >}}) — invalid status code.
- [ERR_HTTP_HEADERS_SENT]({{< relref "/languages/javascript/err_http_headers_sent" >}}) — headers already sent.
- [ERR_HTTP1_CONNECTION_CLOSED]({{< relref "/languages/javascript/err-http1-connection-closed" >}}) — connection closed early.
