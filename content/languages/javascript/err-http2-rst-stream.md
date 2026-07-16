---
title: "[Solution] Node.js ERR_HTTP2_RST_STREAM — HTTP/2 RST_STREAM Fix"
description: "Fix Node.js ERR_HTTP2_RST_STREAM when an HTTP/2 stream is reset. Handle stream reset errors and implement proper stream lifecycle management."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["err-http2-rst-stream", "http2", "stream", "reset", "nodejs"]
weight: 5
---

# Node.js ERR_HTTP2_RST_STREAM — HTTP/2 RST_STREAM Fix

The `ERR_HTTP2_RST_STREAM` error occurs when an HTTP/2 stream receives a RST_STREAM frame, which abruptly terminates the stream. This can be sent by either the client or server to cancel a stream.

## Description

Common ERR_HTTP2_RST_STREAM messages include:

- `ERR_HTTP2_RST_STREAM: Stream was reset` — remote peer sent RST_STREAM.
- `Stream closed with error code` — stream terminated with specific error code.
- `Stream was reset by client` — client cancelled the stream.

## Common Causes

```javascript
const http2 = require("node:http2");

// Cause 1: Client cancels request
const client = http2.connect("https://localhost:3000");
const req = client.request({ ":path": "/slow-api" });
req.close(0); // cancel with NO_ERROR code

// Cause 2: Server closes stream prematurely
const server = http2.createServer();
server.on("stream", (stream, headers) => {
  stream.close(0); // close with NO_ERROR before responding
});

// Cause 3: Application error during stream processing
server.on("stream", (stream, headers) => {
  throw new Error("Processing error"); // stream gets reset
});

// Cause 4: Stream timeout
const req = client.request({ ":path": "/timeout" });
setTimeout(() => req.close(0), 100); // timeout triggers reset
```

## Solutions

### Fix 1: Handle stream reset gracefully

```javascript
const http2 = require("node:http2");

const server = http2.createServer();
server.on("stream", (stream, headers) => {
  let responseSent = false;

  stream.on("error", (err) => {
    if (err.code === "ERR_HTTP2_RST_STREAM" || err.code === "ERR_HTTP2_STREAM_CLOSED") {
      console.log("Stream was reset, cleaning up");
      return;
    }
    console.error("Stream error:", err.message);
  });

  stream.respond({ ":status": 200 });
  responseSent = true;
  stream.end("Hello");
});
```

### Fix 2: Use proper error codes when closing streams

```javascript
const http2 = require("node:http2");

const server = http2.createServer();
server.on("stream", (stream, headers) => {
  // NO_ERROR (0x0) — stream cancelled without error
  // PROTOCOL_ERROR (0x1) — protocol violation
  // INTERNAL_ERROR (0x2) — internal error
  // REFUSED_STREAM (0x7) — try again later
  // CANCEL (0x8) — client cancelled
  // ENHANCE_YOUR_CALM (0xb) — slow down

  try {
    stream.respond({ ":status": 200 });
    stream.end("OK");
  } catch (err) {
    // Use appropriate error code
    stream.close(0x2); // INTERNAL_ERROR
  }
});
```

### Fix 3: Implement stream cancellation on client

```javascript
const http2 = require("node:http2");

const client = http2.connect("https://localhost:3000");

const req = client.request({ ":path": "/api" });

// Set a timeout to cancel slow requests
const timeout = setTimeout(() => {
  req.close(0x8); // CANCEL
  console.log("Request timed out, stream cancelled");
}, 5000);

req.on("response", (headers) => {
  clearTimeout(timeout);
  console.log("Response received");
});

req.on("error", (err) => {
  clearTimeout(timeout);
  if (err.code === "ERR_HTTP2_RST_STREAM") {
    console.log("Stream was reset by server");
  }
});

req.end();
```

### Fix 4: Handle stream lifecycle properly

```javascript
const http2 = require("node:http2");

const client = http2.connect("https://localhost:3000");

function makeRequest(path) {
  return new Promise((resolve, reject) => {
    const req = client.request({ ":path": path });

    req.on("response", (headers) => {
      let data = "";
      req.on("data", (chunk) => (data += chunk));
      req.on("end", () => resolve(data));
    });

    req.on("error", (err) => {
      if (err.code === "ERR_HTTP2_RST_STREAM") {
        reject(new Error("Stream was reset"));
      } else {
        reject(err);
      }
    });

    req.end();
  });
}
```

## Examples

```javascript
const http2 = require("node:http2");

// ERR_HTTP2_RST_STREAM when client cancels
const server = http2.createServer();
server.on("stream", (stream, headers) => {
  // Simulate slow processing
  setTimeout(() => {
    stream.respond({ ":status": 200 });
    stream.end("Delayed response");
  }, 10000);
});

const client = http2.connect("https://localhost:3000");

const req = client.request({ ":path": "/slow" });

// Cancel after 1 second
setTimeout(() => {
  req.close(0x8); // CANCEL
}, 1000);

req.on("error", (err) => {
  if (err.code === "ERR_HTTP2_RST_STREAM") {
    console.log("Request was cancelled");
  }
});
```

## Related Errors

- [ERR_HTTP2_STREAM_ERROR]({{< relref "/languages/javascript/err-http2-stream-error" >}}) — HTTP/2 stream error.
- [ERR_HTTP2_SESSION]({{< relref "/languages/javascript/err-http2-session" >}}) — HTTP/2 session error.
- [ERR_HTTP2_STREAM_CLOSED]({{< relref "/languages/javascript/err-http2-stream" >}}) — stream already closed.
- [ERR_STREAM_DESTROYED]({{< relref "/languages/javascript/err_stream_destroyed" >}}) — stream destroyed.
