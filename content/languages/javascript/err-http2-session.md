---
title: "[Solution] Node.js ERR_HTTP2_SESSION — HTTP/2 Session Error Fix"
description: "Fix Node.js ERR_HTTP2_SESSION when an HTTP/2 session encounters an unrecoverable error. Handle session lifecycle and errors properly."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["err-http2-session", "http2", "session", "connection", "nodejs"]
weight: 5
---

# Node.js ERR_HTTP2_SESSION — HTTP/2 Session Error Fix

The `ERR_HTTP2_SESSION` error occurs when an HTTP/2 session encounters an unrecoverable error. This can happen when the session is in an invalid state or when protocol-level operations fail.

## Description

Common ERR_HTTP2_SESSION messages include:

- `ERR_HTTP2_SESSION: Session error` — generic session-level error.
- `Session has been destroyed` — attempting to use a destroyed session.
- `Session is not active` — operation on inactive session.

## Common Causes

```javascript
const http2 = require("node:http2");

// Cause 1: Using a destroyed session
const client = http2.connect("https://localhost:3000");
client.destroy();
client.request({ ":path": "/api" }); // ERR_HTTP2_SESSION

// Cause 2: Session error during handshake
const client2 = http2.connect("https://localhost:3000");
// Server rejects the connection

// Cause 3: Sending data after session close
client.close();
client.request({ ":path": "/api" }); // ERR_HTTP2_SESSION

// Cause 4: Concurrent modification of session settings
client.settings({ maxConcurrentStreams: 100 });
client.settings({ maxConcurrentStreams: 200 });
```

## Solutions

### Fix 1: Check session state before use

```javascript
const http2 = require("node:http2");

const client = http2.connect("https://localhost:3000");

function safeRequest(client, headers) {
  if (client.destroyed || client.closed) {
    throw new Error("Session is not available");
  }
  return client.request(headers);
}

const req = safeRequest(client, { ":path": "/api" });
req.on("response", (headers) => {
  console.log("Status:", headers[":status"]);
});
req.end();
```

### Fix 2: Handle session errors gracefully

```javascript
const http2 = require("node:http2");

const client = http2.connect("https://localhost:3000");

client.on("error", (err) => {
  if (err.code === "ERR_HTTP2_SESSION") {
    console.error("Session error:", err.message);
    // Reconnect if needed
  }
});

client.on("close", () => {
  console.log("Session closed");
});

client.on("connect", () => {
  console.log("Session connected");
});
```

### Fix 3: Implement session reconnection

```javascript
const http2 = require("node:http2");

class Http2Client {
  constructor(origin) {
    this.origin = origin;
    this.client = null;
    this.connect();
  }

  connect() {
    this.client = http2.connect(this.origin);

    this.client.on("error", (err) => {
      if (err.code === "ERR_HTTP2_SESSION") {
        console.error("Session error, reconnecting...");
        setTimeout(() => this.connect(), 1000);
      }
    });

    this.client.on("close", () => {
      console.log("Session closed, reconnecting...");
      setTimeout(() => this.connect(), 1000);
    });
  }

  request(headers) {
    if (!this.client || this.client.destroyed) {
      throw new Error("Client not connected");
    }
    return this.client.request(headers);
  }
}

const apiClient = new Http2Client("https://api.example.com");
```

### Fix 4: Properly close sessions

```javascript
const http2 = require("node:http2");

const client = http2.connect("https://localhost:3000");

// Graceful shutdown
process.on("SIGTERM", () => {
  console.log("Closing HTTP/2 session...");
  client.close(() => {
    console.log("Session closed gracefully");
    process.exit(0);
  });
});

// Send requests
const req = client.request({ ":path": "/api" });
req.on("response", (headers) => {
  let data = "";
  req.on("data", (chunk) => (data += chunk));
  req.on("end", () => console.log(data));
});
req.end();
```

## Examples

```javascript
const http2 = require("node:http2");

// ERR_HTTP2_SESSION from using destroyed client
const client = http2.connect("https://localhost:3000");

client.on("error", (err) => {
  if (err.code === "ERR_HTTP2_SESSION") {
    console.error("Cannot use session:", err.message);
  }
});

// Destroy the session
client.destroy();

// Attempting to use destroyed session
try {
  const req = client.request({ ":path": "/api" });
} catch (err) {
  console.error(err.code); // ERR_HTTP2_SESSION
}
```

## Related Errors

- [ERR_HTTP2_STREAM_ERROR]({{< relref "/languages/javascript/err-http2-stream-error" >}}) — HTTP/2 stream error.
- [ERR_HTTP2_RST_STREAM]({{< relref "/languages/javascript/err-http2-rst-stream" >}}) — stream reset by peer.
- [ERR_CONNECTION_RESET]({{< relref "/languages/javascript/err-connection-reset" >}}) — connection was reset.
- [ERR_SOCKET_DESTROYED]({{< relref "/languages/javascript/err_socket_destroyed" >}}) — socket already destroyed.
