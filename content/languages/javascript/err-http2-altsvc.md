---
title: "[Solution] Node.js ERR_HTTP2_ALTSVC — HTTP/2 Alt-Svc Error Fix"
description: "Fix Node.js ERR_HTTP2_ALTSVC when an HTTP/2 Alt-Svc header operation fails. Handle alternative service advertisements properly."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Node.js ERR_HTTP2_ALTSVC — HTTP/2 Alt-Svc Error Fix

The `ERR_HTTP2_ALTSVC` error occurs when an HTTP/2 Alt-Svc (Alternative Service) header operation fails. Alt-Svc headers advertise alternative endpoints for HTTP/2 services, and errors can occur when these headers are malformed or cannot be processed.

## Description

Common ERR_HTTP2_ALTSVC messages include:

- `ERR_HTTP2_ALTSVC: Alt-Svc error` — Alt-Svc header operation failed.
- `Invalid Alt-Svc header` — header format is invalid.
- `Cannot set Alt-Svc` — Alt-Svc cannot be set on the connection.

## Common Causes

```javascript
const http2 = require("node:http2");

// Cause 1: Invalid Alt-Svc header format
const server = http2.createServer();
server.on("stream", (stream, headers) => {
  stream.respond({
    ":status": 200,
    "alt-svc": "invalid-format", // malformed
  });
});

// Cause 2: Setting Alt-Svc on HTTP/1.1 connection
// Alt-Svc is an HTTP/2 concept

// Cause 3: Alt-Svc with invalid protocol
stream.respond({
  ":status": 200,
  "alt-svc": "h2=;ma=3600", // missing host
});

// Cause 4: Too many Alt-Svc entries
// Excessive alternative service advertisements
```

## Solutions

### Fix 1: Use valid Alt-Svc format

```javascript
const http2 = require("node:http2");

const server = http2.createServer();
server.on("stream", (stream, headers) => {
  stream.respond({
    ":status": 200,
    "content-type": "text/plain",
    // Correct format: prot-id "=" host ":" port [";ma=" max-age]
    "alt-svc": 'h2="alt.example.com:443";ma=3600',
  });
  stream.end("Hello");
});
```

### Fix 2: Validate Alt-Svc before sending

```javascript
const http2 = require("node:http2");

function isValidAltSvc(altSvc) {
  // Format: proto-id="host:port";ma=seconds
  const pattern = /^[a-z0-9-]+="[^"]+:\d+"(;ma=\d+)?$/;
  return pattern.test(altSvc);
}

function safeSetAltSvc(res, altSvc) {
  if (!isValidAltSvc(altSvc)) {
    console.error("Invalid Alt-Svc format:", altSvc);
    return false;
  }
  res.setHeader("alt-svc", altSvc);
  return true;
}

const server = http2.createServer();
server.on("stream", (stream, headers) => {
  const altSvc = 'h2="alt.example.com:443";ma=3600';
  safeSetAltSvc(stream, altSvc);
  stream.respond({ ":status": 200 });
  stream.end("OK");
});
```

### Fix 3: Handle Alt-Svc on client side

```javascript
const http2 = require("node:http2");

const client = http2.connect("https://example.com");

client.on("stream", (stream, headers) => {
  if (headers["alt-svc"]) {
    console.log("Alternative service available:", headers["alt-svc"]);
    // Optionally connect to the alternative service
  }
});
```

### Fix 4: Limit Alt-Svc entries

```javascript
const http2 = require("node:http2");

function formatAltSvcEntries(entries, maxEntries = 5) {
  const limited = entries.slice(0, maxEntries);
  return limited.join(", ");
}

const server = http2.createServer();
server.on("stream", (stream, headers) => {
  const entries = [
    'h2="alt1.example.com:443";ma=3600',
    'h2="alt2.example.com:443";ma=7200',
  ];

  stream.respond({
    ":status": 200,
    "alt-svc": formatAltSvcEntries(entries),
  });
  stream.end("OK");
});
```

## Examples

```javascript
const http2 = require("node:http2");

// ERR_HTTP2_ALTSVC from invalid format
const server = http2.createServer();
server.on("stream", (stream, headers) => {
  try {
    stream.respond({
      ":status": 200,
      "alt-svc": "h2=missing-quotes:443", // missing quotes
    });
  } catch (err) {
    if (err.code === "ERR_HTTP2_ALTSVC") {
      console.error("Invalid Alt-Svc header");
    }
  }
});
```

## Related Errors

- [ERR_HTTP2_HEADER_ERROR]({{< relref "/languages/javascript/err-http2-header-error" >}}) — invalid header format.
- [ERR_HTTP2_COMPRESS_HEADERS]({{< relref "/languages/javascript/err-http2-compress-headers" >}}) — header compression failed.
- [ERR_HTTP2_MAX_HEADERS]({{< relref "/languages/javascript/err-http2-max-headers" >}}) — too many headers.
- [ERR_HTTP2_SESSION]({{< relref "/languages/javascript/err-http2-session" >}}) — HTTP/2 session error.
