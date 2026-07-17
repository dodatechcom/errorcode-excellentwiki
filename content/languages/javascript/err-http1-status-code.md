---
title: "[Solution] Node.js ERR_HTTP1_STATUS_CODE — Invalid HTTP/1.1 Status Code Fix"
description: "Fix Node.js ERR_HTTP1_STATUS_CODE when an invalid HTTP/1.1 status code is used. Ensure status codes are valid integers in the correct range."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Node.js ERR_HTTP1_STATUS_CODE — Invalid HTTP/1.1 Status Code Fix

The `ERR_HTTP1_STATUS_CODE` error occurs when an invalid HTTP/1.1 status code is used in a response. Status codes must be integers between 100 and 599.

## Description

Common ERR_HTTP1_STATUS_CODE messages include:

- `ERR_HTTP1_STATUS_CODE: Invalid status code` — status code is not a valid integer.
- `Invalid HTTP status code: NaN` — status code is not a number.
- `Status code out of range` — status code outside 100-599.

## Common Causes

```javascript
const http = require("node:http");

// Cause 1: Non-numeric status code
const server = http.createServer((req, res) => {
  res.writeHead("200"); // string instead of number
  res.end("OK");
});

// Cause 2: NaN status code
res.writeHead(parseInt("invalid")); // NaN

// Cause 3: Status code out of range
res.writeHead(999); // too high
res.writeHead(50); // too low for HTTP response

// Cause 4: Float status code
res.writeHead(200.5); // not an integer
```

## Solutions

### Fix 1: Validate status codes before use

```javascript
const http = require("node:http");

function isValidStatusCode(code) {
  return Number.isInteger(code) && code >= 100 && code <= 599;
}

function safeWriteHead(res, statusCode, headers) {
  if (!isValidStatusCode(statusCode)) {
    console.error(`Invalid status code: ${statusCode}`);
    statusCode = 500;
  }
  res.writeHead(statusCode, headers);
}

const server = http.createServer((req, res) => {
  safeWriteHead(res, 200, { "Content-Type": "text/plain" });
  res.end("OK");
});
```

### Fix 2: Use numeric status codes

```javascript
const http = require("node:http");

const server = http.createServer((req, res) => {
  // Always use numeric literals
  res.writeHead(200);
  res.writeHead(404);
  res.writeHead(500);
  res.end("OK");
});
```

### Fix 3: Ensure numeric conversion

```javascript
const http = require("node:http");

function toStatusCode(value) {
  const code = Number(value);
  if (!Number.isInteger(code) || code < 100 || code > 599) {
    return 500; // default to 500 if invalid
  }
  return code;
}

const server = http.createServer((req, res) => {
  const statusCode = toStatusCode(req.query.status || 200);
  res.writeHead(statusCode);
  res.end("OK");
});
```

### Fix 4: Handle status codes in Express.js

```javascript
const express = require("express");
const app = express();

app.get("/api", (req, res) => {
  const statusCode = parseInt(req.query.status, 10);

  if (!Number.isInteger(statusCode) || statusCode < 100 || statusCode > 599) {
    return res.status(400).json({ error: "Invalid status code" });
  }

  res.status(statusCode).json({ status: "ok" });
});

app.use((err, req, res, next) => {
  if (err.code === "ERR_HTTP1_STATUS_CODE") {
    res.status(500).json({ error: "Invalid status code used" });
  } else {
    next(err);
  }
});
```

## Examples

```javascript
const http = require("node:http");

// ERR_HTTP1_STATUS_CODE from invalid status
const server = http.createServer((req, res) => {
  try {
    res.writeHead("not-a-number"); // ERR_HTTP1_STATUS_CODE
  } catch (err) {
    console.error(err.code); // ERR_HTTP1_STATUS_CODE
    res.writeHead(500);
    res.end("Internal error");
  }
});

server.listen(3000);
```

## Related Errors

- [ERR_HTTP1_HEADER_PARSING]({{< relref "/languages/javascript/err-http1-header-parsing" >}}) — header parsing failed.
- [ERR_HTTP1_HEADER_RE_ASSIGNMENT]({{< relref "/languages/javascript/err-http1-header-re-assignment" >}}) — header re-assignment.
- [ERR_HTTP_INVALID_STATUS_CODE]({{< relref "/languages/javascript/err_http_invalid_status_code" >}}) — invalid status code.
- [ERR_HTTP_HEADERS_SENT]({{< relref "/languages/javascript/err_http_headers_sent" >}}) — headers already sent.
