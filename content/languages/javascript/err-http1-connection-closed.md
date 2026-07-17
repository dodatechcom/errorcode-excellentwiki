---
title: "[Solution] Node.js ERR_HTTP1_CONNECTION_CLOSED — HTTP/1.1 Connection Closed Fix"
description: "Fix Node.js ERR_HTTP1_CONNECTION_CLOSED when an HTTP/1.1 connection is closed before a complete response is received. Handle premature connection closure."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Node.js ERR_HTTP1_CONNECTION_CLOSED — HTTP/1.1 Connection Closed Fix

The `ERR_HTTP1_CONNECTION_CLOSED` error occurs when an HTTP/1.1 connection is closed before the complete response is received. This can happen when the server terminates the connection prematurely or when the client disconnects.

## Description

Common ERR_HTTP1_CONNECTION_CLOSED messages include:

- `ERR_HTTP1_CONNECTION_CLOSED: Connection closed before complete response` — server closed connection early.
- `Socket hang up` — connection terminated by peer.
- `aborted` — request was aborted before completion.

## Common Causes

```javascript
const http = require("node:http");

// Cause 1: Server closes connection before responding
const server = http.createServer((req, res) => {
  res.socket.destroy(); // closes before response sent
});

// Cause 2: Client disconnects during response
const req = http.get("http://localhost:3000/slow", (res) => {
  // client aborts before response completes
});
req.abort();

// Cause 3: Keep-alive timeout triggers closure
// Server closes idle connections before client sends next request

// Cause 4: Server crashes during response
const server2 = http.createServer((req, res) => {
  process.exit(0); // server dies mid-response
});
```

## Solutions

### Fix 1: Handle client disconnection gracefully

```javascript
const http = require("node:http");

const server = http.createServer((req, res) => {
  req.on("close", () => {
    if (!res.writableFinished) {
      console.log("Client disconnected before response completed");
      // Clean up resources
    }
  });

  // Check if connection is still open before writing
  if (!req.destroyed) {
    res.writeHead(200, { "Content-Type": "text/plain" });
    res.end("Hello");
  }
});
```

### Fix 2: Implement proper keep-alive handling

```javascript
const http = require("node:http");

const server = http.createServer((req, res) => {
  res.writeHead(200, {
    "Content-Type": "text/plain",
    "Connection": "keep-alive",
    "Keep-Alive": "timeout=5, max=100",
  });
  res.end("Hello");
});

// Set server keep-alive timeout
server.keepAliveTimeout = 5000; // 5 seconds
```

### Fix 3: Use connection state checks

```javascript
const http = require("node:http");

function safeWriteResponse(res, data) {
  if (res.destroyed || res.writableEnded) {
    return false;
  }
  try {
    res.writeHead(200, { "Content-Type": "text/plain" });
    res.end(data);
    return true;
  } catch (err) {
    if (err.code === "ERR_HTTP1_CONNECTION_CLOSED") {
      console.error("Connection was closed before response could be sent");
    }
    return false;
  }
}

const server = http.createServer((req, res) => {
  safeWriteResponse(res, "Hello");
});
```

### Fix 4: Handle client-side errors

```javascript
const http = require("node:http");

function makeRequest(url) {
  return new Promise((resolve, reject) => {
    const req = http.get(url, (res) => {
      let data = "";
      res.on("data", (chunk) => (data += chunk));
      res.on("end", () => resolve(data));
    });

    req.on("error", (err) => {
      if (err.code === "ERR_HTTP1_CONNECTION_CLOSED") {
        reject(new Error("Connection closed before response received"));
      } else {
        reject(err);
      }
    });

    req.on("timeout", () => {
      req.destroy();
      reject(new Error("Request timed out"));
    });
  });
}
```

## Examples

```javascript
const http = require("node:http");

// ERR_HTTP1_CONNECTION_CLOSED when server closes early
const server = http.createServer((req, res) => {
  // Simulate early closure
  setTimeout(() => {
    res.socket.destroy();
  }, 100);

  // This response will never be sent
  res.writeHead(200);
  res.end("Hello");
});

server.listen(3000);

const client = http.get("http://localhost:3000", (res) => {
  // May not reach here
}).on("error", (err) => {
  if (err.code === "ERR_HTTP1_CONNECTION_CLOSED") {
    console.error("Connection closed prematurely");
  }
});
```

## Related Errors

- [ERR_CONNECTION_RESET]({{< relref "/languages/javascript/err-connection-reset" >}}) — connection was reset.
- [ERR_CONNECTION_REFUSED]({{< relref "/languages/javascript/err-connection-refused" >}}) — server refused connection.
- [ERR_HTTP1_INSUFFICIENT]({{< relref "/languages/javascript/err-http1-insufficient" >}}) — insufficient data for HTTP/1.1.
- [ERR_HTTP1_HEADER_PARSING]({{< relref "/languages/javascript/err-http1-header-parsing" >}}) — header parsing failed.
