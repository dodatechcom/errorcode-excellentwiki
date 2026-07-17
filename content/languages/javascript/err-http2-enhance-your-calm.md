---
title: "[Solution] Node.js ERR_HTTP2_ENHANCE_YOUR_CALM — HTTP/2 Calm Enhancement Fix"
description: "Fix Node.js ERR_HTTP2_ENHANCE_YOUR_CALM when an HTTP/2 peer sends too many frames or exceeds rate limits. Implement proper flow control."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Node.js ERR_HTTP2_ENHANCE_YOUR_CALM — HTTP/2 Calm Enhancement Fix

The `ERR_HTTP2_ENHANCE_YOUR_CALM` error occurs when an HTTP/2 peer is sending too many frames or exceeding the rate limits defined in the HTTP/2 specification. This is a protective mechanism to prevent resource exhaustion.

## Description

Common ERR_HTTP2_ENHANCE_YOUR_CALM messages include:

- `ERR_HTTP2_ENHANCE_YOUR_CALM: Enhance your calm` — peer exceeded frame rate limits.
- `Too many PING frames` — excessive PING frames sent.
- `Too many SETTINGS frames` — excessive SETTINGS frames sent.

## Common Causes

```javascript
const http2 = require("node:http2");

// Cause 1: Sending too many PING frames rapidly
const client = http2.connect("https://localhost:3000");
for (let i = 0; i < 1000; i++) {
  client.ping(); // may trigger ERR_HTTP2_ENHANCE_YOUR_CALM
}

// Cause 2: Sending SETTINGS changes too frequently
const client2 = http2.connect("https://localhost:3000");
client2.settings({ maxConcurrentStreams: 10 });
client2.settings({ maxConcurrentStreams: 20 });
client2.settings({ maxConcurrentStreams: 30 }); // too many changes

// Cause 3: Opening too many streams simultaneously
const client3 = http2.connect("https://localhost:3000");
for (let i = 0; i < 100; i++) {
  client3.request({ ":path": "/" }); // exceeds MAX_CONCURRENT_STREAMS
}

// Cause 4: Sending data without respecting flow control
// Not waiting for WINDOW_UPDATE frames
```

## Solutions

### Fix 1: Rate-limit PING frames

```javascript
const http2 = require("node:http2");

const client = http2.connect("https://localhost:3000");

let lastPing = 0;
const PING_INTERVAL = 10000; // 10 seconds minimum

function safePing() {
  const now = Date.now();
  if (now - lastPing < PING_INTERVAL) {
    console.warn("Ping rate limited");
    return;
  }
  lastPing = now;
  client.ping((err) => {
    if (err) {
      console.error("Ping failed:", err.message);
    }
  });
}

setInterval(safePing, PING_INTERVAL);
```

### Fix 2: Respect MAX_CONCURRENT_STREAMS

```javascript
const http2 = require("node:http2");

const client = http2.connect("https://localhost:3000");

const MAX_STREAMS = 100;
let activeStreams = 0;

function createRequest(path) {
  if (activeStreams >= MAX_STREAMS) {
    console.warn("Max concurrent streams reached, queuing request");
    return;
  }
  activeStreams++;
  const req = client.request({ ":path": path });
  req.on("response", () => {
    activeStreams--;
  });
  req.on("error", () => {
    activeStreams--;
  });
  req.end();
}
```

### Fix 3: Limit SETTINGS changes

```javascript
const http2 = require("node:http2");

const client = http2.connect("https://localhost:3000");

let lastSettings = 0;
const SETTINGS_INTERVAL = 5000; // 5 seconds minimum

function applySettings(newSettings) {
  const now = Date.now();
  if (now - lastSettings < SETTINGS_INTERVAL) {
    console.warn("Settings change rate limited");
    return;
  }
  lastSettings = now;
  client.settings(newSettings);
}
```

### Fix 4: Implement proper flow control

```javascript
const http2 = require("node:http2");

const server = http2.createServer();
server.on("stream", (stream, headers) => {
  stream.respond({ ":status": 200 });

  const data = Buffer.alloc(1024 * 1024, "x"); // 1MB
  let offset = 0;

  function writeChunk() {
    while (offset < data.length) {
      const allowed = stream.write(data.slice(offset, offset + 1024));
      offset += 1024;
      if (!allowed) {
        stream.once("drain", writeChunk);
        return;
      }
    }
    stream.end();
  }

  writeChunk();
});
```

## Examples

```javascript
const http2 = require("node:http2");

// ERR_HTTP2_ENHANCE_YOUR_CALM from rapid PINGs
const client = http2.connect("https://localhost:3000");

client.on("error", (err) => {
  if (err.code === "ERR_HTTP2_ENHANCE_YOUR_CALM") {
    console.error("Peer sent too many frames");
    client.close();
  }
});

// Aggressive pinging
setInterval(() => {
  client.ping();
}, 10); // too frequent
```

## Related Errors

- [ERR_HTTP2_FLOW_CONTROL_ERROR]({{< relref "/languages/javascript/err-http2-flow-control-error" >}}) — flow control violation.
- [ERR_HTTP2_STREAM_ERROR]({{< relref "/languages/javascript/err-http2-stream-error" >}}) — HTTP/2 stream error.
- [ERR_HTTP2_SESSION]({{< relref "/languages/javascript/err-http2-session" >}}) — HTTP/2 session error.
- [ERR_HTTP2_MAX_HEADERS]({{< relref "/languages/javascript/err-http2-max-headers" >}}) — too many headers.
