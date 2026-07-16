---
title: "[Solution] Node.js ERR_HTTP2_MAX_HEADERS — Too Many HTTP/2 Headers Fix"
description: "Fix Node.js ERR_HTTP2_MAX_HEADERS when the number of HTTP/2 headers exceeds the allowed limit. Reduce header count or increase limits."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["err-http2-max-headers", "http2", "headers", "limit", "nodejs"]
weight: 5
---

# Node.js ERR_HTTP2_MAX_HEADERS — Too Many HTTP/2 Headers Fix

The `ERR_HTTP2_MAX_HEADERS` error occurs when the number of headers in an HTTP/2 request or response exceeds the configured maximum. This is a protective limit to prevent resource exhaustion from excessive header data.

## Description

Common ERR_HTTP2_MAX_HEADERS messages include:

- `ERR_HTTP2_MAX_HEADERS: Maximum number of headers exceeded` — too many headers sent.
- `Header count limit exceeded` — header count over limit.
- `Headers size limit exceeded` — total header size too large.

## Common Causes

```javascript
const http2 = require("node:http2");

// Cause 1: Too many custom headers
const headers = { ":status": 200 };
for (let i = 0; i < 200; i++) {
  headers[`x-custom-${i}`] = `value-${i}`; // 200+ headers
}
stream.respond(headers); // may trigger ERR_HTTP2_MAX_HEADERS

// Cause 2: Large cookie headers
const bigCookie = "a".repeat(100000);
stream.respond({ "cookie": bigCookie });

// Cause 3: Many Set-Cookie headers
const cookies = [];
for (let i = 0; i < 50; i++) {
  cookies.push(`cookie${i}=value${i}`);
}

// Cause 4: Default maxHeaderListSize exceeded
// Default is typically 16384 bytes total
```

## Solutions

### Fix 1: Increase max header limits

```javascript
const http2 = require("node:http2");

const server = http2.createServer({
  settings: {
    maxHeaderListSize: 65536, // 64KB (default 16384)
  },
});

server.on("stream", (stream, headers) => {
  stream.respond({ ":status": 200 });
  stream.end("OK");
});
```

### Fix 2: Reduce number of headers

```javascript
const http2 = require("node:http2");

function bundleHeaders(headers, maxHeaders = 100) {
  const result = {};
  let count = 0;

  for (const [key, value] of Object.entries(headers)) {
    if (count >= maxHeaders) break;
    if (key.startsWith(":")) {
      result[key] = value; // always include pseudo-headers
    } else {
      result[key] = value;
      count++;
    }
  }

  return result;
}

const server = http2.createServer();
server.on("stream", (stream, headers) => {
  const responseHeaders = bundleHeaders({
    ":status": 200,
    "content-type": "application/json",
    ...generateCustomHeaders(),
  });
  stream.respond(responseHeaders);
  stream.end("OK");
});
```

### Fix 3: Use header compression effectively

```javascript
const http2 = require("node:http2");

// HPACK compression helps, but many headers still use more memory
// Combine related headers into fewer values

// Instead of many individual headers:
// x-meta-1: value1
// x-meta-2: value2
// x-meta-3: value3

// Use a single JSON header:
const meta = JSON.stringify({
  field1: "value1",
  field2: "value2",
  field3: "value3",
});

stream.respond({
  ":status": 200,
  "x-metadata": meta, // single header instead of many
});
```

### Fix 4: Validate header count on client

```javascript
const http2 = require("node:http2");

const client = http2.connect("https://localhost:3000", {
  settings: {
    maxHeaderListSize: 32768,
  },
});

function sendRequest(method, path, headers = {}) {
  const MAX_HEADERS = 50;
  const headerCount = Object.keys(headers).length;

  if (headerCount > MAX_HEADERS) {
    throw new Error(`Too many headers: ${headerCount} > ${MAX_HEADERS}`);
  }

  const req = client.request({
    ":path": path,
    ":method": method,
    ...headers,
  });
  return req;
}
```

## Examples

```javascript
const http2 = require("node:http2");

// ERR_HTTP2_MAX_HEADERS from excessive headers
const client = http2.connect("https://localhost:3000");

const headers = { ":path": "/api" };
for (let i = 0; i < 300; i++) {
  headers[`x-header-${i}`] = `value-${i}`;
}

const req = client.request(headers);

req.on("error", (err) => {
  if (err.code === "ERR_HTTP2_MAX_HEADERS") {
    console.error("Too many headers sent");
  }
});

req.end();
```

## Related Errors

- [ERR_HTTP2_HEADER_ERROR]({{< relref "/languages/javascript/err-http2-header-error" >}}) — invalid header format.
- [ERR_HTTP2_COMPRESS_HEADERS]({{< relref "/languages/javascript/err-http2-compress-headers" >}}) — header compression failed.
- [ERR_HTTP2_PSEUDO_HEADERS]({{< relref "/languages/javascript/err-http2-pseudo-headers" >}}) — invalid pseudo-headers.
- [ERR_HTTP2_FRAME_ERROR]({{< relref "/languages/javascript/err-http2-frame-error" >}}) — invalid frame received.
