---
title: "[Solution] Node.js ERR_HTTP1_HEADER_PARSING — HTTP/1.1 Header Parsing Fix"
description: "Fix Node.js ERR_HTTP1_HEADER_PARSING when HTTP/1.1 headers cannot be parsed. Ensure headers follow HTTP/1.1 syntax rules."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["err-http1-header-parsing", "http", "headers", "parser", "nodejs"]
weight: 5
---

# Node.js ERR_HTTP1_HEADER_PARSING — HTTP/1.1 Header Parsing Fix

The `ERR_HTTP1_HEADER_PARSING` error occurs when the HTTP/1.1 parser encounters headers that cannot be parsed. This can happen when headers contain invalid characters, malformed values, or violate HTTP/1.1 syntax rules.

## Description

Common ERR_HTTP1_HEADER_PARSING messages include:

- `ERR_HTTP1_HEADER_PARSING: Header parsing failed` — header syntax is invalid.
- `Invalid header value` — header contains invalid characters.
- `Malformed header` — header line doesn't follow HTTP/1.1 format.

## Common Causes

```javascript
const http = require("node:http");

// Cause 1: Invalid characters in header values
const server = http.createServer((req, res) => {
  res.writeHead(200, {
    "X-Custom": "value\u0000invalid", // null byte
  });
  res.end("OK");
});

// Cause 2: Missing colon in header
// Raw HTTP: "InvalidHeader" — no colon separator

// Cause 3: Header value with line breaks
res.writeHead(200, {
  "X-Data": "line1\r\nline2", // CRLF in value
});

// Cause 4: Oversized header line
const hugeHeader = "x".repeat(8000);
res.writeHead(200, { [hugeHeader]: "value" });
```

## Solutions

### Fix 1: Validate header values

```javascript
const http = require("node:http");

function isValidHeaderValue(value) {
  if (typeof value !== "string") return false;
  // HTTP/1.1 headers must not contain control characters
  // except for space and tab
  return !/[\x00-\x08\x0a-\x1f\x7f]/.test(value);
}

function safeWriteHead(res, statusCode, headers) {
  const sanitized = {};
  for (const [key, value] of Object.entries(headers)) {
    if (isValidHeaderValue(value)) {
      sanitized[key] = value;
    }
  }
  res.writeHead(statusCode, sanitized);
}

const server = http.createServer((req, res) => {
  safeWriteHead(res, 200, {
    "Content-Type": "application/json",
    "X-Data": req.headers["x-data"] || "default",
  });
  res.end("OK");
});
```

### Fix 2: Sanitize incoming headers

```javascript
const http = require("node:http");

function sanitizeHeaders(headers) {
  const sanitized = {};
  for (const [key, value] of Object.entries(headers)) {
    if (typeof value === "string") {
      // Remove control characters except space/tab
      sanitized[key] = value.replace(/[\x00-\x08\x0a-\x1f\x7f]/g, "");
    }
  }
  return sanitized;
}

const server = http.createServer((req, res) => {
  const cleanHeaders = sanitizeHeaders(req.headers);
  console.log("Sanitized headers:", cleanHeaders);
  res.writeHead(200, { "Content-Type": "text/plain" });
  res.end("OK");
});
```

### Fix 3: Set header size limits

```javascript
const http = require("node:http");

const server = http.createServer({
  maxHeaderSize: 8192, // 8KB max header size
});

server.on("clientError", (err, socket) => {
  if (err.code === "ERR_HTTP1_HEADER_PARSING") {
    console.error("Header parsing failed:", err.message);
    socket.end("HTTP/1.1 400 Bad Request\r\n\r\n");
    return;
  }
  socket.end("HTTP/1.1 400 Bad Request\r\n\r\n");
});

server.listen(3000);
```

### Fix 4: Handle parser errors on client

```javascript
const http = require("node:http");

const req = http.get("http://localhost:3000", (res) => {
  res.on("data", (chunk) => {});
  res.on("end", () => {});
});

req.on("error", (err) => {
  if (err.code === "ERR_HTTP1_HEADER_PARSING") {
    console.error("Failed to parse server response headers");
  }
});
```

## Examples

```javascript
const http = require("node:http");

// ERR_HTTP1_HEADER_PARSING from invalid header characters
const server = http.createServer((req, res) => {
  // Simulating a client sending malformed headers
  console.log("Received headers:", req.headers);
  res.writeHead(200, { "Content-Type": "text/plain" });
  res.end("OK");
});

server.on("clientError", (err, socket) => {
  if (err.code === "ERR_HTTP1_HEADER_PARSING") {
    console.error("Client sent invalid headers");
    socket.end("HTTP/1.1 400 Bad Request\r\n\r\n");
  }
});
```

## Related Errors

- [ERR_HTTP1_CONNECTION_CLOSED]({{< relref "/languages/javascript/err-http1-connection-closed" >}}) — connection closed early.
- [ERR_HTTP1_INSUFFICIENT]({{< relref "/languages/javascript/err-http1-insufficient" >}}) — insufficient data.
- [ERR_HTTP1_STATUS_CODE]({{< relref "/languages/javascript/err-http1-status-code" >}}) — invalid status code.
- [ERR_HTTP1_HEADER_RE_ASSIGNMENT]({{< relref "/languages/javascript/err-http1-header-re-assignment" >}}) — header re-assignment.
