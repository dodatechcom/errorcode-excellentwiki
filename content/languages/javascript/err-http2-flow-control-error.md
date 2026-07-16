---
title: "[Solution] Node.js ERR_HTTP2_FLOW_CONTROL_ERROR — HTTP/2 Flow Control Fix"
description: "Fix Node.js ERR_HTTP2_FLOW_CONTROL_ERROR when HTTP/2 flow control window is exceeded. Implement proper flow control in HTTP/2 streams."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["err-http2-flow-control-error", "http2", "flow-control", "nodejs"]
weight: 5
---

# Node.js ERR_HTTP2_FLOW_CONTROL_ERROR — HTTP/2 Flow Control Fix

The `ERR_HTTP2_FLOW_CONTROL_ERROR` error occurs when an HTTP/2 peer violates the flow control protocol by sending more data than the flow control window allows. This is a protocol-level error that indicates improper data transmission.

## Description

Common ERR_HTTP2_FLOW_CONTROL_ERROR messages include:

- `ERR_HTTP2_FLOW_CONTROL_ERROR: Flow control error` — window size exceeded.
- `Flow control error for stream` — per-stream flow control violation.

## Common Causes

```javascript
const http2 = require("node:http2");

// Cause 1: Sending data without checking window size
const client = http2.connect("https://localhost:3000");
const req = client.request({ ":path": "/upload", ":method": "POST" });
const hugeBuffer = Buffer.alloc(10 * 1024 * 1024); // 10MB
req.write(hugeBuffer); // may exceed flow control window

// Cause 2: Ignoring stream events
const server = http2.createServer();
server.on("stream", (stream, headers) => {
  const data = Buffer.alloc(1024 * 1024);
  stream.write(data); // not checking if stream is writable
  stream.end(data);
});

// Cause 3: Window size too small
// Default window is 65535 bytes, large transfers need more

// Cause 4: Not sending WINDOW_UPDATE frames
// Server must send WINDOW_UPDATE to allow more data
```

## Solutions

### Fix 1: Respect stream writable state

```javascript
const http2 = require("node:http2");

const server = http2.createServer();
server.on("stream", (stream, headers) => {
  stream.respond({ ":status": 200, "content-type": "application/octet-stream" });

  const data = Buffer.alloc(1024 * 1024, "x");
  let offset = 0;

  function writeChunk() {
    while (offset < data.length) {
      if (!stream.destroyed && stream.writable) {
        const ok = stream.write(data.slice(offset, Math.min(offset + 65535, data.length)));
        offset += 65535;
        if (!ok) {
          stream.once("drain", writeChunk);
          return;
        }
      } else {
        return;
      }
    }
    stream.end();
  }

  writeChunk();
});
```

### Fix 2: Configure appropriate window sizes

```javascript
const http2 = require("node:http2");

const server = http2.createServer({
  settings: {
    initialWindowSize: 1024 * 1024, // 1MB per stream
    sessionWindowSize: 1024 * 1024 * 10, // 10MB total
  },
});

server.on("stream", (stream, headers) => {
  stream.respond({ ":status": 200 });
  stream.end("Hello");
});
```

### Fix 3: Handle backpressure properly

```javascript
const http2 = require("node:http2");

const client = http2.connect("https://localhost:3000");

const req = client.request({
  ":path": "/upload",
  ":method": "POST",
  "content-type": "application/octet-stream",
});

const largeFile = Buffer.alloc(5 * 1024 * 1024, "x");

function writeWithBackpressure(buffer) {
  return new Promise((resolve, reject) => {
    const chunkSize = 65535;
    let offset = 0;

    function writeNext() {
      while (offset < buffer.length) {
        const ok = req.write(buffer.slice(offset, offset + chunkSize));
        offset += chunkSize;
        if (!ok) {
          req.once("drain", writeNext);
          return;
        }
      }
      resolve();
    }

    writeNext();
  });
}

writeWithBackpressure(largeFile).then(() => req.end());
```

### Fix 4: Monitor stream state

```javascript
const http2 = require("node:http2");

const server = http2.createServer();
server.on("stream", (stream, headers) => {
  stream.on("error", (err) => {
    if (err.code === "ERR_HTTP2_FLOW_CONTROL_ERROR") {
      console.error("Flow control error on stream", stream.id);
      stream.close();
    }
  });

  stream.respond({ ":status": 200 });
  stream.end("OK");
});
```

## Examples

```javascript
const http2 = require("node:http2");

// ERR_HTTP2_FLOW_CONTROL_ERROR from ignoring flow control
const client = http2.connect("https://localhost:3000");

const req = client.request({ ":path": "/upload", ":method": "POST" });

// Writing too much data without respecting flow control
const data = Buffer.alloc(100 * 1024 * 1024); // 100MB
req.write(data); // may trigger ERR_HTTP2_FLOW_CONTROL_ERROR

req.on("error", (err) => {
  if (err.code === "ERR_HTTP2_FLOW_CONTROL_ERROR") {
    console.error("Flow control window exceeded");
  }
});
```

## Related Errors

- [ERR_HTTP2_ENHANCE_YOUR_CALM]({{< relref "/languages/javascript/err-http2-enhance-your-calm" >}}) — rate limit exceeded.
- [ERR_HTTP2_STREAM_ERROR]({{< relref "/languages/javascript/err-http2-stream-error" >}}) — HTTP/2 stream error.
- [ERR_HTTP2_SESSION]({{< relref "/languages/javascript/err-http2-session" >}}) — HTTP/2 session error.
- [ERR_HTTP2_FRAME_ERROR]({{< relref "/languages/javascript/err-http2-frame-error" >}}) — invalid frame received.
