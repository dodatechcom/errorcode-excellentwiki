---
title: "[Solution] Node.js ERR_SOCKET_DESTROYED — Socket Destroyed Fix"
description: "Fix Node.js ERR_SOCKET_DESTROYED when writing to a destroyed socket. Handle connection lifecycle, check socket state, and manage connection pools."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Node.js ERR_SOCKET_DESTROYED — Socket Destroyed Fix

The `ERR_SOCKET_DESTROYED` error occurs when attempting to write data to a TCP socket that has already been destroyed. This happens when the connection has been closed, timed out, or forcefully terminated before all pending writes complete.

## Description

Common ERR_SOCKET_DESTROYED messages include:

- `Error [ERR_SOCKET_DESTROYED]: socket was destroyed` — writing to a closed socket.
- `Error [ERR_SOCKET_DESTROYED]: Cannot write after socket was destroyed` — post-destroy write attempt.
- `Error: This socket has been ended by the other party` — remote end closed the connection.

## Common Causes

```javascript
const net = require("net");

// Cause 1: Writing to a socket after it was destroyed by an error
const socket = net.createConnection({ host: "example.com", port: 80 });
socket.on("error", () => socket.destroy());
socket.write("GET / HTTP/1.1\r\nHost: example.com\r\n\r\n");
// If error occurs, subsequent writes trigger ERR_SOCKET_DESTROYED

// Cause 2: Connection timeout destroying the socket
const client = new net.Socket();
client.setTimeout(5000);
client.on("timeout", () => {
  client.destroy();  // timeout destroys socket
});
// Any write after timeout = ERR_SOCKET_DESTROYED

// Cause 3: Server closes connection while data is pending
// Client sends data, server closes before write completes

// Cause 4: Concurrent writes to the same socket
socket.write(data1);
socket.write(data2);  // if socket was destroyed between writes
```

## Solutions

### Fix 1: Check socket state before writing

```javascript
const net = require("net");

function safeSocketWrite(socket, data) {
  if (socket.destroyed) {
    console.error("Socket is destroyed — cannot write");
    return false;
  }

  if (!socket.writable) {
    console.error("Socket is not writable");
    return false;
  }

  return socket.write(data);
}
```

### Fix 2: Handle errors before destroying the socket

```javascript
const net = require("net");

const socket = net.createConnection({ host: "example.com", port: 80 });

socket.on("connect", () => {
  socket.write("GET / HTTP/1.1\r\nHost: example.com\r\n\r\n");
});

socket.on("data", (data) => {
  console.log("Received:", data.toString());
  // Process data before any potential destroy
});

socket.on("error", (err) => {
  console.error("Socket error:", err.message);
  // Don't destroy here if writes are still pending
  // Let the error propagate to the caller
});

socket.on("close", () => {
  console.log("Socket closed");
});
```

### Fix 3: Use connection pooling for HTTP requests

```javascript
const http = require("http");
const https = require("https");

// Use the built-in agent for connection pooling
const agent = new http.Agent({
  keepAlive: true,
  maxSockets: 10,
  timeout: 30000,
});

async function fetchWithRetry(url, retries = 3) {
  for (let i = 0; i < retries; i++) {
    try {
      return await new Promise((resolve, reject) => {
        const protocol = url.startsWith("https") ? https : http;
        const req = protocol.get(url, { agent }, (res) => {
          let data = "";
          res.on("data", (chunk) => (data += chunk));
          res.on("end", () => resolve(data));
        });
        req.on("error", reject);
        req.setTimeout(10000, () => {
          req.destroy();
          reject(new Error("Request timeout"));
        });
      });
    } catch (err) {
      if (err.message.includes("destroyed") && i < retries - 1) {
        console.log(`Retry ${i + 1} after socket destroy`);
        continue;
      }
      throw err;
    }
  }
}
```

### Fix 4: Graceful shutdown with pending writes

```javascript
const net = require("net");

class SafeConnection {
  constructor(host, port) {
    this.socket = net.createConnection({ host, port });
    this.pendingWrites = [];
    this.destroying = false;

    this.socket.on("error", (err) => {
      console.error("Connection error:", err.message);
    });

    this.socket.on("close", () => {
      console.log("Connection closed");
    });
  }

  write(data) {
    if (this.destroying || this.socket.destroyed) {
      console.warn("Cannot write — connection is closing");
      return false;
    }
    return this.socket.write(data);
  }

  async shutdown() {
    this.destroying = true;
    return new Promise((resolve) => {
      this.socket.end(() => resolve());
    });
  }
}
```

## Examples

```javascript
// ERR_SOCKET_DESTROYED in a proxy server
const net = require("net");

const server = net.createServer((clientSocket) => {
  const targetSocket = net.createConnection({ host: "target.com", port: 80 });

  clientSocket.pipe(targetSocket);
  targetSocket.pipe(clientSocket);

  // Handle premature disconnection
  clientSocket.on("error", () => {
    if (!targetSocket.destroyed) {
      targetSocket.destroy();  // clean up the target
    }
  });

  targetSocket.on("error", () => {
    if (!clientSocket.destroyed) {
      clientSocket.destroy();  // clean up the client
    }
  });
});

server.listen(8080);
```

## Related Errors

- [ERR_STREAM_DESTROYED]({{< relref "/languages/javascript/err_stream_destroyed" >}}) — generic stream already destroyed.
- [ERR_SOCKET_TIMEOUT]({{< relref "/languages/javascript/ERR_SOCKET_TIMEOUT" >}}) — socket connection timed out.
- [InvalidStateError]({{< relref "/languages/javascript/invalidstateerror" >}}) — object is not in the required state.
- [AbortError]({{< relref "/languages/javascript/aborterror" >}}) — operation was intentionally cancelled.
