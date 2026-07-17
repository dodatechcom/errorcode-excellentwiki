---
title: "[Solution] Node.js ERR_CONNECTION_RESET — Connection Reset Fix"
description: "Fix Node.js ERR_CONNECTION_RESET when an existing connection is forcibly closed by the remote server. Handle connection reset errors gracefully."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Node.js ERR_CONNECTION_RESET — Connection Reset Fix

The `ERR_CONNECTION_RESET` error occurs when an established TCP connection is forcibly closed by the remote peer. This typically happens when the server crashes, restarts, or actively terminates the connection.

## Description

Common ERR_CONNECTION_RESET messages include:

- `read ECONNRESET` — connection was reset while reading data.
- `write ECONNRESET` — connection was reset while writing data.
- `Connection reset by peer` — remote server closed the connection unexpectedly.

## Common Causes

```javascript
const net = require("node:net");

// Cause 1: Server crashes during request
// Client receives ECONNRESET when server process dies

// Cause 2: Server closes connection prematurely
const server = net.createServer((socket) => {
  socket.end("partial response"); // closes immediately
  // Client may get ECONNRESET
});

// Cause 3: Keep-alive timeout mismatch
// Server closes connection before client finishes

// Cause 4: Network interruption
// Physical network disruption causes reset
```

## Solutions

### Fix 1: Implement retry logic with backoff

```javascript
async function fetchWithRetry(url, maxRetries = 3) {
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      const response = await fetch(url);
      return await response.json();
    } catch (err) {
      if (err.code === "ECONNRESET" && attempt < maxRetries) {
        const delay = Math.min(1000 * 2 ** (attempt - 1), 10000);
        console.log(`Attempt ${attempt} failed, retrying in ${delay}ms...`);
        await new Promise((r) => setTimeout(r, delay));
        continue;
      }
      throw err;
    }
  }
}
```

### Fix 2: Set appropriate keep-alive timeouts

```javascript
const http = require("node:http");

const server = http.createServer((req, res) => {
  res.end("Hello");
});

// Set keep-alive timeout to match client expectations
server.keepAliveTimeout = 65000; // 65 seconds
server.headersTimeout = 66000;

server.listen(3000);
```

### Fix 3: Handle partial responses gracefully

```javascript
const net = require("node:net");

const client = net.createConnection({ port: 3000, host: "localhost" });

let data = "";

client.on("data", (chunk) => {
  data += chunk.toString();
});

client.on("end", () => {
  console.log("Connection closed normally:", data);
});

client.on("error", (err) => {
  if (err.code === "ECONNRESET") {
    console.error("Connection reset, partial data:", data);
    // Use whatever data was received before the reset
  } else {
    console.error("Connection error:", err.message);
  }
});
```

### Fix 4: Use HTTP agent with keep-alive

```javascript
const http = require("node:http");

const agent = new http.Agent({
  keepAlive: true,
  keepAliveMsecs: 30000,
  maxSockets: 10,
  maxFreeSockets: 5,
});

const req = http.get("http://localhost:3000/api", { agent }, (res) => {
  let data = "";
  res.on("data", (chunk) => (data += chunk));
  res.on("end", () => console.log(data));
});

req.on("error", (err) => {
  if (err.code === "ECONNRESET") {
    console.error("Connection was reset by server");
  }
});
```

## Examples

```javascript
const http = require("node:http");

// ERR_CONNECTION_RESET during long-running request
const server = http.createServer((req, res) => {
  // Simulate slow response
  setTimeout(() => {
    res.end("Hello"); // client may have disconnected
  }, 60000);
});

server.on("clientError", (err, socket) => {
  if (err.code === "ECONNRESET") {
    console.error("Client connection was reset");
  }
  socket.end("HTTP/1.1 400 Bad Request\r\n\r\n");
});
```

## Related Errors

- [ERR_CONNECTION_REFUSED]({{< relref "/languages/javascript/err-connection-refused" >}}) — server refused connection.
- [ERR_SOCKET_TIMEOUT]({{< relref "/languages/javascript/ERR_SOCKET_TIMEOUT" >}}) — socket timed out.
- [ERR_STREAM_DESTROYED]({{< relref "/languages/javascript/err_stream_destroyed" >}}) — stream already destroyed.
- [ERR_SOCKET_DESTROYED]({{< relref "/languages/javascript/err_socket_destroyed" >}}) — socket already destroyed.
