---
title: "Node.js Error: listen EADDRINUSE"
description: "Error: listen EADDRINUSE — Fix port already in use errors in Node.js servers."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

The `EADDRINUSE` error occurs when a Node.js server tries to bind to a port that is already in use by another process. This is one of the most common errors when developing or deploying Node.js applications.

## Description

Common EADDRINUSE messages include:

- `Error: listen EADDRINUSE: address already in use :::3000` — port 3000 is taken
- `listen EADDRINUSE 0.0.0.0:80` — port 80 is in use
- `Error: listen EADDRINUSE 127.0.0.1:5432` — port already bound

## Common Causes

```javascript
// Cause 1: Previous server instance still running
// $ node server.js (crashed but process still in background)

// Cause 2: Another application uses the same port
// Another Node.js app, Python server, or system service

// Cause 3: Rapid restart during development
// Port is still in TIME_WAIT state after server closes

// Cause 4: Multiple workers binding to the same port
// cluster.fork() without sharing the socket handle
```

## Solutions

### Fix 1: Find and kill the process using the port

```bash
# Find the process using the port
lsof -i :3000

# Or with ss
ss -tlnp | grep 3000

# Kill the process
kill -9 $(lsof -t -i :3000)
```

### Fix 2: Use a dynamic port or SO_REUSEADDR

```javascript
const http = require("node:http");

const server = http.createServer((req, res) => {
  res.end("ok");
});

// Let the OS assign a random available port
server.listen(0, () => {
  console.log(`Listening on port ${server.address().port}`);
});
```

### Fix 3: Handle the error with retry logic

```javascript
const http = require("node:http");

function startServer(port, retries = 3) {
  const server = http.createServer((req, res) => {
    res.end("ok");
  });

  server.on("error", (err) => {
    if (err.code === "EADDRINUSE" && retries > 0) {
      console.log(`Port ${port} in use, retrying in 1s...`);
      setTimeout(() => startServer(port + 1, retries - 1), 1000);
    } else {
      console.error(`Failed to start server on port ${port}:`, err.message);
      process.exit(1);
    }
  });

  server.listen(port, () => {
    console.log(`Server running on port ${port}`);
  });
}

startServer(3000);
```

### Fix 4: Use SO_REUSEADDR option

```javascript
const net = require("node:net");

const server = net.createServer();
server.on("error", (err) => {
  console.error("Server error:", err.message);
});

// Set SO_REUSEADDR before binding
server.listen({ port: 3000, exclusive: false });
```

## Examples

```javascript
// EADDRINUSE: port 3000 already in use
// $ lsof -i :3000
// COMMAND   PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
// node    12345 admin  20u  IPv6  ...    0t0      TCP *:3000 (LISTEN)
// $ kill 12345
// $ node server.js  (now it works)
```

## Related Errors

- [ERR_HTTP_SERVER_RESPONSE]({{< relref "/languages/javascript/err_http_headers_sent" >}}) — HTTP response error.
- [ERR_STREAM_DESTROYED]({{< relref "/languages/javascript/err_stream_destroyed" >}}) — stream destroyed before operation completes.
- [ERR_SOCKET_DESTROYED]({{< relref "/languages/javascript/err_socket_destroyed" >}}) — socket destroyed.
