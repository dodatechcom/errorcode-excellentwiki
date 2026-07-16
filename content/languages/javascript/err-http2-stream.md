---
title: "[Solution] Node.js ERR_HTTP2_STREAM — HTTP/2 Stream Operation Error Fix"
description: "Fix Node.js ERR_HTTP2_STREAM when an HTTP/2 stream operation fails. Handle stream lifecycle errors and ensure proper stream management."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["err-http2-stream", "http2", "stream", "operation", "nodejs"]
weight: 5
---

# Node.js ERR_HTTP2_STREAM — HTTP/2 Stream Operation Error Fix

The `ERR_HTTP2_STREAM` error occurs when an operation on an HTTP/2 stream fails. This can happen when trying to perform operations on a stream that is in an invalid state, such as writing to a closed stream or reading from a destroyed stream.

## Description

Common ERR_HTTP2_STREAM messages include:

- `ERR_HTTP2_STREAM: Stream error` — stream operation failed.
- `Stream is not open` — attempting to write to a closed stream.
- `Stream has been destroyed` — using a destroyed stream.
- `Stream is not readable` — trying to read from a non-readable stream.

## Common Causes

```javascript
const http2 = require("node:http2");

// Cause 1: Writing to a closed stream
const server = http2.createServer();
server.on("stream", (stream, headers) => {
  stream.respond({ ":status": 200 });
  stream.end("Hello");
  stream.write("More data"); // ERR_HTTP2_STREAM — stream already ended
});

// Cause 2: Using stream after destroy
stream.destroy();
stream.respond({ ":status": 200 }); // ERR_HTTP2_STREAM

// Cause 3: Double-ending a stream
stream.end("first");
stream.end("second"); // ERR_HTTP2_STREAM

// Cause 4: Writing to a half-closed stream
```

## Solutions

### Fix 1: Check stream state before operations

```javascript
const http2 = require("node:http2");

const server = http2.createServer();
server.on("stream", (stream, headers) => {
  if (stream.destroyed || stream.closed) {
    return;
  }

  if (!stream.writable) {
    return;
  }

  stream.respond({ ":status": 200 });
  stream.end("Hello");
});
```

### Fix 2: Track stream state manually

```javascript
const http2 = require("node:http2");

const server = http2.createServer();
server.on("stream", (stream, headers) => {
  let finished = false;

  stream.on("close", () => { finished = true; });
  stream.on("finish", () => { finished = true; });

  function safeWrite(data) {
    if (finished || stream.destroyed) {
      return false;
    }
    return stream.write(data);
  }

  function safeEnd(data) {
    if (finished || stream.destroyed) {
      return false;
    }
    stream.end(data);
    finished = true;
    return true;
  }

  stream.respond({ ":status": 200 });
  safeEnd("Hello");
});
```

### Fix 3: Use once to prevent double operations

```javascript
const http2 = require("node:http2");

const client = http2.connect("https://localhost:3000");
const req = client.request({ ":path": "/api" });

req.once("response", (headers) => {
  console.log("Status:", headers[":status"]);
});

req.once("end", () => {
  console.log("Stream ended");
});

req.once("error", (err) => {
  if (err.code === "ERR_HTTP2_STREAM") {
    console.error("Stream operation failed");
  }
});

req.end();
```

### Fix 4: Implement proper error handling

```javascript
const http2 = require("node:http2");

const server = http2.createServer();
server.on("stream", (stream, headers) => {
  stream.on("error", (err) => {
    if (err.code === "ERR_HTTP2_STREAM") {
      console.error("Stream operation error:", err.message);
    }
  });

  try {
    stream.respond({ ":status": 200, "content-type": "text/plain" });
    stream.end("Hello, World!");
  } catch (err) {
    if (err.code === "ERR_HTTP2_STREAM") {
      console.error("Failed to write to stream");
    }
  }
});
```

## Examples

```javascript
const http2 = require("node:http2");

// ERR_HTTP2_STREAM from double-ending
const client = http2.connect("https://localhost:3000");
const req = client.request({ ":path": "/api" });

req.end("first");
try {
  req.end("second"); // ERR_HTTP2_STREAM
} catch (err) {
  console.error(err.code); // ERR_HTTP2_STREAM
}
```

## Related Errors

- [ERR_HTTP2_STREAM_ERROR]({{< relref "/languages/javascript/err-http2-stream-error" >}}) — unrecoverable stream error.
- [ERR_HTTP2_RST_STREAM]({{< relref "/languages/javascript/err-http2-rst-stream" >}}) — stream reset by peer.
- [ERR_STREAM_DESTROYED]({{< relref "/languages/javascript/err_stream_destroyed" >}}) — stream destroyed.
- [ERR_HTTP2_SESSION]({{< relref "/languages/javascript/err-http2-session" >}}) — HTTP/2 session error.
