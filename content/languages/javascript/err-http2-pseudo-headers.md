---
title: "[Solution] Node.js ERR_HTTP2_PSEUDO_HEADERS — Invalid Pseudo-Headers Fix"
description: "Fix Node.js ERR_HTTP2_PSEUDO_HEADERS when invalid or misplaced pseudo-headers are used in HTTP/2. Follow HTTP/2 pseudo-header rules."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Node.js ERR_HTTP2_PSEUDO_HEADERS — Invalid Pseudo-Headers Fix

The `ERR_HTTP2_PSEUDO_HEADERS` error occurs when pseudo-headers (headers starting with `:`) are used incorrectly in HTTP/2. Pseudo-headers must come before regular headers and cannot be used in responses in certain contexts.

## Description

Common ERR_HTTP2_PSEUDO_HEADERS messages include:

- `ERR_HTTP2_PSEUDO_HEADERS: Pseudo-header not allowed` — invalid pseudo-header usage.
- `Pseudo-header after regular header` — wrong header ordering.
- `Invalid pseudo-header in response` — pseudo-header not allowed in response.

## Common Causes

```javascript
const http2 = require("node:http2");

// Cause 1: Pseudo-headers mixed with regular headers
stream.respond({
  "content-type": "text/plain", // regular header first
  ":status": 200, // pseudo-header after — error
});

// Cause 2: Client sending response pseudo-headers
const req = client.request({ ":path": "/api" });
req.respond({ ":status": 200 }); // client can't respond

// Cause 3: Invalid pseudo-header name
stream.respond({
  ":status": 200,
  ":invalid-pseudo": "value", // not a valid pseudo-header
});

// Cause 4: Pseudo-header in trailers
stream.addTrailers({
  ":status": "200", // pseudo-headers not allowed in trailers
});
```

## Solutions

### Fix 1: Send pseudo-headers first in responses

```javascript
const http2 = require("node:http2");

const server = http2.createServer();
server.on("stream", (stream, headers) => {
  // Pseudo-headers must come first
  stream.respond({
    ":status": 200, // pseudo-header first
    "content-type": "application/json", // regular headers after
    "x-request-id": "abc123",
  });
  stream.end(JSON.stringify({ status: "ok" }));
});
```

### Fix 2: Use valid pseudo-headers only

```javascript
const http2 = require("node:http2");

// Valid request pseudo-headers: :method, :path, :scheme, :authority
// Valid response pseudo-headers: :status

const client = http2.connect("https://localhost:3000");
const req = client.request({
  ":method": "GET", // valid
  ":path": "/api", // valid
  ":scheme": "https", // valid
  ":authority": "localhost:3000", // valid
});

req.on("response", (headers) => {
  console.log("Status:", headers[":status"]); // valid response pseudo-header
});
```

### Fix 3: Validate pseudo-headers before sending

```javascript
const http2 = require("node:http2");

const VALID_REQUEST_PSEUDO = new Set([":method", ":path", ":scheme", ":authority"]);
const VALID_RESPONSE_PSEUDO = new Set([":status"]);

function validatePseudoHeaders(headers, isRequest) {
  const validSet = isRequest ? VALID_REQUEST_PSEUDO : VALID_RESPONSE_PSEUDO;
  let seenRegular = false;

  for (const key of Object.keys(headers)) {
    if (key.startsWith(":")) {
      if (seenRegular) {
        throw new Error(`Pseudo-header ${key} after regular header`);
      }
      if (!validSet.has(key)) {
        throw new Error(`Invalid pseudo-header: ${key}`);
      }
    } else {
      seenRegular = true;
    }
  }
}

// Validate before responding
const responseHeaders = {
  ":status": 200,
  "content-type": "text/plain",
};
validatePseudoHeaders(responseHeaders, false);
stream.respond(responseHeaders);
```

### Fix 4: Don't use pseudo-headers in trailers

```javascript
const http2 = require("node:http2");

const server = http2.createServer();
server.on("stream", (stream, headers) => {
  stream.respond({ ":status": 200 });

  // Send trailers without pseudo-headers
  stream.addTrailers({
    "x-checksum": "abc123", // regular header only
    // Don't include ":status" in trailers
  });

  stream.end("Hello");
});
```

## Examples

```javascript
const http2 = require("node:http2");

// ERR_HTTP2_PSEUDO_HEADERS from wrong ordering
const server = http2.createServer();
server.on("stream", (stream, headers) => {
  try {
    // Wrong: pseudo-header after regular headers
    stream.respond({
      "content-type": "text/plain",
      ":status": 200,
    });
  } catch (err) {
    console.error(err.code); // ERR_HTTP2_PSEUDO_HEADERS

    // Correct: pseudo-headers first
    stream.respond({
      ":status": 200,
      "content-type": "text/plain",
    });
  }
  stream.end("Hello");
});
```

## Related Errors

- [ERR_HTTP2_HEADER_ERROR]({{< relref "/languages/javascript/err-http2-header-error" >}}) — invalid header format.
- [ERR_HTTP2_COMPRESS_HEADERS]({{< relref "/languages/javascript/err-http2-compress-headers" >}}) — header compression failed.
- [ERR_HTTP2_MAX_HEADERS]({{< relref "/languages/javascript/err-http2-max-headers" >}}) — too many headers.
- [ERR_HTTP2_FRAME_ERROR]({{< relref "/languages/javascript/err-http2-frame-error" >}}) — invalid frame received.
