---
title: "[Solution] Node.js ERR_HTTP2_SOCKET — HTTP/2 Socket Error Fix"
description: "Fix Node.js ERR_HTTP2_SOCKET when an HTTP/2 socket operation fails. Handle socket-level errors in HTTP/2 connections."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Node.js ERR_HTTP2_SOCKET — HTTP/2 Socket Error Fix

The `ERR_HTTP2_SOCKET` error occurs when a socket-level operation fails in an HTTP/2 connection. This can happen when the underlying TCP socket encounters issues during HTTP/2 communication.

## Description

Common ERR_HTTP2_SOCKET messages include:

- `ERR_HTTP2_SOCKET: Socket error` — socket operation failed.
- `Socket is not writable` — attempting to write to a non-writable socket.
- `Socket has been destroyed` — using a destroyed socket.

## Common Causes

```javascript
const http2 = require("node:http2");

// Cause 1: Writing to a destroyed socket
const client = http2.connect("https://localhost:3000");
client.socket.destroy();
client.request({ ":path": "/api" }); // ERR_HTTP2_SOCKET

// Cause 2: Socket timeout
// Underlying socket times out during data transfer

// Cause 3: Network interruption
// Physical connection lost during HTTP/2 session

// Cause 4: Socket not ready
// Attempting to use socket before connection is established
```

## Solutions

### Fix 1: Monitor socket state

```javascript
const http2 = require("node:http2");

const client = http2.connect("https://localhost:3000");

client.on("socket", (socket) => {
  socket.on("error", (err) => {
    console.error("Socket error:", err.message);
  });

  socket.on("close", () => {
    console.log("Socket closed");
  });

  socket.on("timeout", () => {
    console.warn("Socket timed out");
    socket.destroy();
  });
});
```

### Fix 2: Set appropriate socket options

```javascript
const http2 = require("node:http2");

const client = http2.connect("https://localhost:3000", {
  socket: {
    timeout: 60000, // 60 second timeout
  },
});

// Access the underlying socket
client.on("connect", () => {
  const socket = client.socket;
  socket.setTimeout(60000);
  socket.keepAlive(true, 30000);
});
```

### Fix 3: Handle socket errors gracefully

```javascript
const http2 = require("node:http2");

const client = http2.connect("https://localhost:3000");

client.on("error", (err) => {
  if (err.code === "ERR_HTTP2_SOCKET") {
    console.error("Socket error occurred:", err.message);
    // Reconnect if needed
  }
});

client.on("close", () => {
  console.log("HTTP/2 session closed");
  // Reconnect logic here
});

const req = client.request({ ":path": "/api" });
req.on("error", (err) => {
  if (err.code === "ERR_HTTP2_SOCKET") {
    console.error("Request failed due to socket error");
  }
});
req.end();
```

### Fix 4: Implement socket reconnection

```javascript
const http2 = require("node:http2");

class ReliableHttp2Client {
  constructor(origin) {
    this.origin = origin;
    this.client = null;
    this.connect();
  }

  connect() {
    this.client = http2.connect(this.origin);

    this.client.on("error", (err) => {
      console.error("Client error:", err.code);
      if (err.code === "ERR_HTTP2_SOCKET") {
        this.reconnect();
      }
    });

    this.client.on("close", () => {
      this.reconnect();
    });
  }

  reconnect() {
    setTimeout(() => {
      console.log("Reconnecting...");
      this.connect();
    }, 1000);
  }

  request(headers) {
    return this.client.request(headers);
  }
}
```

## Examples

```javascript
const http2 = require("node:http2");

// ERR_HTTP2_SOCKET from socket destruction
const client = http2.connect("https://localhost:3000");

client.on("connect", () => {
  // Destroy the underlying socket
  client.socket.destroy();

  // Attempting to use the client after socket destruction
  try {
    const req = client.request({ ":path": "/api" });
  } catch (err) {
    console.error(err.code); // ERR_HTTP2_SOCKET
  }
});
```

## Related Errors

- [ERR_HTTP2_SESSION]({{< relref "/languages/javascript/err-http2-session" >}}) — HTTP/2 session error.
- [ERR_SOCKET_DESTROYED]({{< relref "/languages/javascript/err_socket_destroyed" >}}) — socket already destroyed.
- [ERR_SOCKET_TIMEOUT]({{< relref "/languages/javascript/ERR_SOCKET_TIMEOUT" >}}) — socket timed out.
- [ERR_CONNECTION_RESET]({{< relref "/languages/javascript/err-connection-reset" >}}) — connection was reset.
