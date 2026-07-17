---
title: "[Solution] Node.js ERR_HTTP2_FRAME_ERROR — HTTP/2 Frame Error Fix"
description: "Fix Node.js ERR_HTTP2_FRAME_ERROR when an invalid or malformed HTTP/2 frame is received. Ensure proper frame construction and handling."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Node.js ERR_HTTP2_FRAME_ERROR — HTTP/2 Frame Error Fix

The `ERR_HTTP2_FRAME_ERROR` error occurs when an invalid or malformed HTTP/2 frame is received or sent. This indicates a violation of the HTTP/2 frame format specification.

## Description

Common ERR_HTTP2_FRAME_ERROR messages include:

- `ERR_HTTP2_FRAME_ERROR: Invalid frame` — frame structure is invalid.
- `Frame error for stream` — specific stream frame is malformed.
- `Error sending frame` — frame encoding failed.

## Common Causes

```javascript
const http2 = require("node:http2");

// Cause 1: Invalid frame payload
// Sending malformed DATA or HEADERS frames

// Cause 2: Frame size exceeds MAX_FRAME_SIZE
const client = http2.connect("https://localhost:3000");
const req = client.request({ ":path": "/api" });
const oversizedPayload = Buffer.alloc(16 * 1024 * 1024 + 1); // exceeds MAX_FRAME_SIZE
req.write(oversizedPayload);

// Cause 3: Invalid frame type
// Sending undefined frame types

// Cause 4: Frame sent on wrong stream state
// Sending HEADERS on a half-closed stream
```

## Solutions

### Fix 1: Respect MAX_FRAME_SIZE

```javascript
const http2 = require("node:http2");

const server = http2.createServer({
  settings: {
    maxFrameSize: 16384, // 16KB default, can be 16384-16777215
  },
});

server.on("stream", (stream, headers) => {
  const data = Buffer.alloc(1024, "x");
  let offset = 0;

  function writeChunk() {
    while (offset < data.length) {
      const chunk = data.slice(offset, offset + 16384);
      const ok = stream.write(chunk);
      offset += 16384;
      if (!ok) {
        stream.once("drain", writeChunk);
        return;
      }
    }
    stream.end();
  }

  stream.respond({ ":status": 200 });
  writeChunk();
});
```

### Fix 2: Validate frame content before sending

```javascript
const http2 = require("node:http2");

function validateFrameData(data, maxFrameSize) {
  if (!Buffer.isBuffer(data)) {
    throw new Error("Frame data must be a Buffer");
  }
  if (data.length > maxFrameSize) {
    throw new Error(`Frame size ${data.length} exceeds max ${maxFrameSize}`);
  }
  return true;
}

const client = http2.connect("https://localhost:3000");
const req = client.request({ ":path": "/upload", ":method": "POST" });

const data = Buffer.alloc(1024, "x");
if (validateFrameData(data, 16384)) {
  req.write(data);
}
req.end();
```

### Fix 3: Handle frame errors gracefully

```javascript
const http2 = require("node:http2");

const server = http2.createServer();
server.on("stream", (stream, headers) => {
  stream.on("error", (err) => {
    if (err.code === "ERR_HTTP2_FRAME_ERROR") {
      console.error("Frame error on stream", stream.id, ":", err.message);
      try {
        stream.close();
      } catch {}
    }
  });

  stream.respond({ ":status": 200 });
  stream.end("OK");
});
```

### Fix 4: Configure session-level settings

```javascript
const http2 = require("node:http2");

const client = http2.connect("https://localhost:3000", {
  settings: {
    maxFrameSize: 16384,
    headerTableSize: 4096,
    enablePush: false,
  },
});

client.on("remoteSettings", (settings) => {
  console.log("Remote max frame size:", settings.maxFrameSize);
});
```

## Examples

```javascript
const http2 = require("node:http2");

// ERR_HTTP2_FRAME_ERROR with oversized payload
const client = http2.connect("https://localhost:3000");
const req = client.request({ ":path": "/api", ":method": "POST" });

// Data larger than MAX_FRAME_SIZE
const data = Buffer.alloc(17 * 1024 * 1024); // 17MB > 16MB default
req.write(data);

req.on("error", (err) => {
  if (err.code === "ERR_HTTP2_FRAME_ERROR") {
    console.error("Frame error: data too large");
  }
});
```

## Related Errors

- [ERR_HTTP2_COMPRESS_HEADERS]({{< relref "/languages/javascript/err-http2-compress-headers" >}}) — header compression failed.
- [ERR_HTTP2_FLOW_CONTROL_ERROR]({{< relref "/languages/javascript/err-http2-flow-control-error" >}}) — flow control violation.
- [ERR_HTTP2_STREAM_ERROR]({{< relref "/languages/javascript/err-http2-stream-error" >}}) — HTTP/2 stream error.
- [ERR_HTTP2_HEADER_ERROR]({{< relref "/languages/javascript/err-http2-header-error" >}}) — invalid HTTP/2 header.
