---
title: "[Solution] Node.js ERR_HTTP2_COMPRESS_HEADERS — HTTP/2 Header Compression Fix"
description: "Fix Node.js ERR_HTTP2_COMPRESS_HEADERS when HTTP/2 header compression fails. Ensure headers are valid and compressible."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["err-http2-compress-headers", "http2", "headers", "compression", "nodejs"]
weight: 5
---

# Node.js ERR_HTTP2_COMPRESS_HEADERS — HTTP/2 Header Compression Fix

The `ERR_HTTP2_COMPRESS_HEADERS` error occurs when HTTP/2 header compression fails. This can happen when headers contain invalid values, are too large, or cannot be compressed by the HPACK algorithm used in HTTP/2.

## Description

Common ERR_HTTP2_COMPRESS_HEADERS messages include:

- `ERR_HTTP2_COMPRESS_HEADERS: failed to compress headers` — HPACK compression failed.
- `Header compression failed` — headers could not be encoded.

## Common Causes

```javascript
const http2 = require("node:http2");

// Cause 1: Invalid header values containing null bytes
const server = http2.createServer();
server.on("stream", (stream, headers) => {
  stream.respond({
    ":status": 200,
    "x-data": "value\u0000invalid", // null byte in header
  });
});

// Cause 2: Headers too large to compress
const hugeValue = "x".repeat(1024 * 1024);
stream.respond({ "x-huge": hugeValue }); // may fail

// Cause 3: Invalid header name
stream.respond({ "": "value" }); // empty header name

// Cause 4: Sending headers after stream is closed
stream.close();
stream.respond({ ":status": 200 }); // ERR_HTTP2_COMPRESS_HEADERS
```

## Solutions

### Fix 1: Sanitize header values

```javascript
const http2 = require("node:http2");

function sanitizeHeaders(headers) {
  const sanitized = {};
  for (const [key, value] of Object.entries(headers)) {
    if (typeof value === "string") {
      // Remove null bytes and control characters
      sanitized[key] = value.replace(/[\x00-\x1f\x7f]/g, "");
    } else if (typeof value === "number") {
      sanitized[key] = String(value);
    }
  }
  return sanitized;
}

const server = http2.createServer();
server.on("stream", (stream, headers) => {
  const responseHeaders = sanitizeHeaders({
    ":status": 200,
    "content-type": "application/json",
  });
  stream.respond(responseHeaders);
  stream.end(JSON.stringify({ status: "ok" }));
});
```

### Fix 2: Limit header sizes

```javascript
const http2 = require("node:http2");

const server = http2.createServer({
  maxHeaderSize: 8192, // default 16KB
});

server.on("stream", (stream, headers) => {
  // Validate header sizes before sending
  const MAX_HEADER_VALUE_SIZE = 8192;
  for (const [key, value] of Object.entries(headers)) {
    if (typeof value === "string" && value.length > MAX_HEADER_VALUE_SIZE) {
      stream.respond({ ":status": 431 });
      stream.end("Header too large");
      return;
    }
  }
  stream.respond({ ":status": 200 });
  stream.end("OK");
});
```

### Fix 3: Ensure stream is open before sending headers

```javascript
const http2 = require("node:http2");

const client = http2.connect("https://localhost:3000");

const req = client.request({ ":path": "/api" });

req.on("response", (headers) => {
  console.log("Status:", headers[":status"]);
});

req.on("error", (err) => {
  if (err.code === "ERR_HTTP2_COMPRESS_HEADERS") {
    console.error("Stream may be closed");
  }
});

req.end();
```

### Fix 4: Use stream error handling

```javascript
const http2 = require("node:http2");

const server = http2.createServer();
server.on("stream", (stream, headers) => {
  stream.on("error", (err) => {
    if (err.code === "ERR_HTTP2_COMPRESS_HEADERS") {
      console.error("Header compression failed:", err.message);
      try {
        stream.close();
      } catch {}
    }
  });

  try {
    stream.respond({ ":status": 200, "content-type": "text/plain" });
    stream.end("Hello, World!");
  } catch (err) {
    console.error("Failed to send headers:", err.message);
  }
});
```

## Examples

```javascript
const http2 = require("node:http2");

// ERR_HTTP2_COMPRESS_HEADERS example
const client = http2.connect("https://localhost:3000");

const req = client.request({
  ":path": "/api",
  ":method": "POST",
  "content-type": "application/json",
  "x-request-data": "value\u0000invalid", // may cause compression failure
});

req.on("error", (err) => {
  if (err.code === "ERR_HTTP2_COMPRESS_HEADERS") {
    console.error("Failed to compress request headers");
  }
});

req.end();
```

## Related Errors

- [ERR_HTTP2_HEADER_ERROR]({{< relref "/languages/javascript/err-http2-header-error" >}}) — invalid HTTP/2 header.
- [ERR_HTTP2_MAX_HEADERS]({{< relref "/languages/javascript/err-http2-max-headers" >}}) — too many headers.
- [ERR_HTTP2_PSEUDO_HEADERS]({{< relref "/languages/javascript/err-http2-pseudo-headers" >}}) — invalid pseudo-headers.
- [ERR_HTTP2_STREAM_ERROR]({{< relref "/languages/javascript/err-http2-stream-error" >}}) — HTTP/2 stream error.
