---
title: "[Solution] Node.js ERR_HTTP2_STATUS_CODE — Invalid HTTP/2 Status Code Fix"
description: "Fix Node.js ERR_HTTP2_STATUS_CODE when an invalid status code is used in an HTTP/2 response. Ensure :status pseudo-header is valid."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["err-http2-status-code", "http2", "status-code", "pseudo-header", "nodejs"]
weight: 5
---

# Node.js ERR_HTTP2_STATUS_CODE — Invalid HTTP/2 Status Code Fix

The `ERR_HTTP2_STATUS_CODE` error occurs when an invalid status code is used in an HTTP/2 response via the `:status` pseudo-header. Status codes must be valid integers between 100 and 599.

## Description

Common ERR_HTTP2_STATUS_CODE messages include:

- `ERR_HTTP2_STATUS_CODE: Invalid status code` — :status is not a valid integer.
- `Invalid HTTP/2 status code` — status code outside valid range.
- `:status must be a numeric string` — pseudo-header value format is wrong.

## Common Causes

```javascript
const http2 = require("node:http2");

// Cause 1: Non-numeric :status value
const server = http2.createServer();
server.on("stream", (stream, headers) => {
  stream.respond({
    ":status": "ok", // string instead of number
    "content-type": "text/plain",
  });
});

// Cause 2: Float status code
stream.respond({
  ":status": 200.5, // not an integer
});

// Cause 3: Status code out of range
stream.respond({
  ":status": 999, // too high
});

// Cause 4: Missing :status pseudo-header
stream.respond({
  "content-type": "text/plain", // no :status
});
```

## Solutions

### Fix 1: Always use integer :status values

```javascript
const http2 = require("node:http2");

const server = http2.createServer();
server.on("stream", (stream, headers) => {
  stream.respond({
    ":status": 200, // integer
    "content-type": "application/json",
  });
  stream.end(JSON.stringify({ status: "ok" }));
});
```

### Fix 2: Validate status codes

```javascript
const http2 = require("node:http2");

function isValidStatusCode(code) {
  return Number.isInteger(code) && code >= 100 && code <= 599;
}

const server = http2.createServer();
server.on("stream", (stream, headers) => {
  const statusCode = parseInt(headers[":status"], 10);

  if (!isValidStatusCode(statusCode)) {
    stream.respond({
      ":status": 500,
      "content-type": "text/plain",
    });
    stream.end("Invalid status code");
    return;
  }

  stream.respond({
    ":status": statusCode,
    "content-type": "text/plain",
  });
  stream.end("OK");
});
```

### Fix 3: Ensure :status is always included

```javascript
const http2 = require("node:http2");

const server = http2.createServer();
server.on("stream", (stream, headers) => {
  const responseHeaders = {
    ":status": 200, // always include :status
    "content-type": "application/json",
  };
  stream.respond(responseHeaders);
  stream.end(JSON.stringify({ status: "ok" }));
});
```

### Fix 4: Handle invalid status in client

```javascript
const http2 = require("node:http2");

const client = http2.connect("https://localhost:3000");
const req = client.request({ ":path": "/api" });

req.on("response", (headers) => {
  const status = parseInt(headers[":status"], 10);
  if (isNaN(status) || status < 100 || status > 599) {
    console.error("Invalid status code received:", headers[":status"]);
    return;
  }
  console.log("Status:", status);
});

req.on("error", (err) => {
  if (err.code === "ERR_HTTP2_STATUS_CODE") {
    console.error("Invalid status code in response");
  }
});

req.end();
```

## Examples

```javascript
const http2 = require("node:http2");

// ERR_HTTP2_STATUS_CODE from string :status
const server = http2.createServer();
server.on("stream", (stream, headers) => {
  try {
    stream.respond({
      ":status": "200", // string — may cause error
      "content-type": "text/plain",
    });
  } catch (err) {
    console.error(err.code); // ERR_HTTP2_STATUS_CODE
  }
});
```

## Related Errors

- [ERR_HTTP2_HEADER_ERROR]({{< relref "/languages/javascript/err-http2-header-error" >}}) — invalid header format.
- [ERR_HTTP2_PSEUDO_HEADERS]({{< relref "/languages/javascript/err-http2-pseudo-headers" >}}) — invalid pseudo-headers.
- [ERR_HTTP1_STATUS_CODE]({{< relref "/languages/javascript/err-http1-status-code" >}}) — invalid HTTP/1.1 status code.
- [ERR_HTTP_INVALID_STATUS_CODE]({{< relref "/languages/javascript/err_http_invalid_status_code" >}}) — invalid status code.
