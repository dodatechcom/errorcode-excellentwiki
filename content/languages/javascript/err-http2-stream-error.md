---
title: "[Solution] Node.js ERR_HTTP2_STREAM_ERROR — HTTP/2 Stream Error Fix"
description: "Fix Node.js ERR_HTTP2_STREAM_ERROR when an HTTP/2 stream encounters an unrecoverable error. Handle stream errors and implement proper error recovery."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Node.js ERR_HTTP2_STREAM_ERROR — HTTP/2 Stream Error Fix

The `ERR_HTTP2_STREAM_ERROR` error occurs when an HTTP/2 stream encounters an unrecoverable error. This is typically the result of a protocol violation, internal error, or the stream being explicitly reset with an error code.

## Description

Common ERR_HTTP2_STREAM_ERROR messages include:

- `ERR_HTTP2_STREAM_ERROR: Stream error` — generic stream error.
- `Stream error with code 0x2` — internal error on the stream.
- `Stream was terminated with error` — stream terminated by peer.

## Common Causes

```javascript
const http2 = require("node:http2");

// Cause 1: Writing to a destroyed stream
const server = http2.createServer();
server.on("stream", (stream, headers) => {
  stream.destroy();
  stream.write("data"); // ERR_HTTP2_STREAM_ERROR

// Cause 2: Sending headers after stream is closed
  stream.close();
  stream.respond({ ":status": 200 }); // ERR_HTTP2_STREAM_ERROR

// Cause 3: Application error during stream processing
  throw new Error("Internal processing error");

// Cause 4: Peer sends invalid data causing stream error
});
```

## Solutions

### Fix 1: Check stream state before operations

```javascript
const http2 = require("node:http2");

const server = http2.createServer();
server.on("stream", (stream, headers) => {
  if (stream.destroyed || stream.closed) {
    return; // Don't operate on destroyed streams
  }

  stream.respond({ ":status": 200, "content-type": "text/plain" });
  stream.end("Hello, World!");
});
```

### Fix 2: Handle stream errors with try/catch

```javascript
const http2 = require("node:http2");

const server = http2.createServer();
server.on("stream", (stream, headers) => {
  stream.on("error", (err) => {
    if (err.code === "ERR_HTTP2_STREAM_ERROR") {
      console.error("Stream error:", err.message);
      // Don't re-throw, the stream is already gone
      return;
    }
    console.error("Other error:", err);
  });

  try {
    stream.respond({ ":status": 200 });
    stream.end("OK");
  } catch (err) {
    console.error("Failed to respond:", err.message);
  }
});
```

### Fix 3: Implement stream error recovery on client

```javascript
const http2 = require("node:http2");

const client = http2.connect("https://localhost:3000");

function makeRequest(path, retries = 2) {
  return new Promise((resolve, reject) => {
    const req = client.request({ ":path": path });

    req.on("response", (headers) => {
      let data = "";
      req.on("data", (chunk) => (data += chunk));
      req.on("end", () => resolve(data));
    });

    req.on("error", (err) => {
      if (err.code === "ERR_HTTP2_STREAM_ERROR" && retries > 0) {
        console.log("Stream error, retrying...");
        makeRequest(path, retries - 1).then(resolve).catch(reject);
      } else {
        reject(err);
      }
    });

    req.end();
  });
}
```

### Fix 4: Properly close streams on error

```javascript
const http2 = require("node:http2");

const server = http2.createServer();
server.on("stream", (stream, headers) => {
  stream.on("error", (err) => {
    console.error("Stream error:", err.code, err.message);
    if (!stream.destroyed && !stream.closed) {
      stream.close(0x2); // close with INTERNAL_ERROR code
    }
  });

  try {
    stream.respond({ ":status": 200 });
    stream.end("OK");
  } catch (err) {
    stream.close(0x2);
  }
});
```

## Examples

```javascript
const http2 = require("node:http2");

// ERR_HTTP2_STREAM_ERROR during data transfer
const client = http2.connect("https://localhost:3000");

const req = client.request({
  ":path": "/upload",
  ":method": "POST",
});

const largeData = Buffer.alloc(1024 * 1024, "x");
req.write(largeData);

req.on("error", (err) => {
  if (err.code === "ERR_HTTP2_STREAM_ERROR") {
    console.error("Stream error during upload:", err.message);
    // Retry or report failure
  }
});

req.end();
```

## Related Errors

- [ERR_HTTP2_RST_STREAM]({{< relref "/languages/javascript/err-http2-rst-stream" >}}) — stream reset by peer.
- [ERR_HTTP2_SESSION]({{< relref "/languages/javascript/err-http2-session" >}}) — HTTP/2 session error.
- [ERR_STREAM_DESTROYED]({{< relref "/languages/javascript/err_stream_destroyed" >}}) — stream destroyed.
- [ERR_HTTP2_STREAM]({{< relref "/languages/javascript/err-http2-stream" >}}) — HTTP/2 stream operation error.
