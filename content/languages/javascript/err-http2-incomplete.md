---
title: "[Solution] Node.js ERR_HTTP2_INCOMPLETE — HTTP/2 Incomplete Message Fix"
description: "Fix Node.js ERR_HTTP2_INCOMPLETE when an HTTP/2 message is incomplete. Handle partial frames and ensure complete message transmission."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Node.js ERR_HTTP2_INCOMPLETE — HTTP/2 Incomplete Message Fix

The `ERR_HTTP2_INCOMPLETE` error occurs when an HTTP/2 message is received incompletely. This can happen when a frame is truncated, when the connection closes before all data is received, or when the stream is reset mid-transfer.

## Description

Common ERR_HTTP2_INCOMPLETE messages include:

- `ERR_HTTP2_INCOMPLETE: Incomplete HTTP/2 message` — message not fully received.
- `Incomplete frame received` — frame was truncated.
- `Stream ended with incomplete data` — stream closed before all data arrived.

## Common Causes

```javascript
const http2 = require("node:http2");

// Cause 1: Connection closes during data transfer
const client = http2.connect("https://localhost:3000");
const req = client.request({ ":path": "/large-file" });
req.on("data", (chunk) => {
  // Connection may close before all data arrives
});

// Cause 2: Stream reset during transfer
const server = http2.createServer();
server.on("stream", (stream, headers) => {
  const data = Buffer.alloc(1024 * 1024);
  stream.write(data);
  stream.close(0x2); // INTERNAL_ERROR — incomplete
});

// Cause 3: Frame truncation
// Network issues cause frame to be cut short

// Cause 4: Buffer overflow
// Receive buffer overflows during large transfers
```

## Solutions

### Fix 1: Handle incomplete data gracefully

```javascript
const http2 = require("node:http2");

const client = http2.connect("https://localhost:3000");
const req = client.request({ ":path": "/api" });

let complete = false;
let data = "";

req.on("data", (chunk) => {
  data += chunk.toString();
});

req.on("end", () => {
  complete = true;
  console.log("Received complete response:", data);
});

req.on("error", (err) => {
  if (err.code === "ERR_HTTP2_INCOMPLETE") {
    console.error("Incomplete message, partial data:", data);
    if (data) {
      // Use partial data if available
      processPartialData(data);
    }
  }
});

function processPartialData(data) {
  console.log("Processing partial data:", data.length, "bytes");
}
```

### Fix 2: Implement retry for incomplete transfers

```javascript
const http2 = require("node:http2");

async function fetchWithRetry(client, path, maxRetries = 3) {
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      const data = await new Promise((resolve, reject) => {
        const req = client.request({ ":path": path });
        let body = "";

        req.on("data", (chunk) => (body += chunk));
        req.on("end", () => resolve(body));
        req.on("error", (err) => reject(err));
        req.end();
      });
      return data;
    } catch (err) {
      if (err.code === "ERR_HTTP2_INCOMPLETE" && attempt < maxRetries) {
        console.log(`Attempt ${attempt} incomplete, retrying...`);
        continue;
      }
      throw err;
    }
  }
}
```

### Fix 3: Validate frame completeness

```javascript
const http2 = require("node:http2");

const server = http2.createServer();
server.on("stream", (stream, headers) => {
  const data = Buffer.alloc(1024 * 1024, "x");
  let offset = 0;

  function writeChunk() {
    while (offset < data.length) {
      if (stream.destroyed) {
        console.error("Stream destroyed during write");
        return;
      }
      const chunk = data.slice(offset, offset + 65535);
      const ok = stream.write(chunk);
      offset += 65535;
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

### Fix 4: Set appropriate buffer sizes

```javascript
const http2 = require("node:http2");

const client = http2.connect("https://localhost:3000", {
  settings: {
    initialWindowSize: 1024 * 1024, // 1MB
    maxFrameSize: 16384,
  },
});

const req = client.request({
  ":path": "/large-data",
  ":method": "GET",
});

req.on("data", (chunk) => {
  // Data arrives in controlled chunks
});

req.on("error", (err) => {
  if (err.code === "ERR_HTTP2_INCOMPLETE") {
    console.error("Incomplete message received");
  }
});

req.end();
```

## Examples

```javascript
const http2 = require("node:http2");

// ERR_HTTP2_INCOMPLETE from premature stream close
const server = http2.createServer();
server.on("stream", (stream, headers) => {
  stream.respond({ ":status": 200 });

  const data = "Hello, World!";
  stream.write(data.slice(0, 5));
  stream.close(0x2); // Close before all data sent

  // Client receives ERR_HTTP2_INCOMPLETE
});

const client = http2.connect("https://localhost:3000");
const req = client.request({ ":path": "/api" });
let received = "";

req.on("data", (chunk) => (received += chunk));
req.on("error", (err) => {
  if (err.code === "ERR_HTTP2_INCOMPLETE") {
    console.error("Incomplete:", received);
  }
});
req.end();
```

## Related Errors

- [ERR_HTTP2_STREAM_ERROR]({{< relref "/languages/javascript/err-http2-stream-error" >}}) — HTTP/2 stream error.
- [ERR_HTTP2_RST_STREAM]({{< relref "/languages/javascript/err-http2-rst-stream" >}}) — stream reset by peer.
- [ERR_HTTP1_INSUFFICIENT]({{< relref "/languages/javascript/err-http1-insufficient" >}}) — insufficient data for HTTP/1.1.
- [ERR_HTTP2_FRAME_ERROR]({{< relref "/languages/javascript/err-http2-frame-error" >}}) — invalid frame received.
