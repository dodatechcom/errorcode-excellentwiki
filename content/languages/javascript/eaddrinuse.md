---
title: "[Solution] Node.js EADDRINUSE: port already in use Error Fix"
description: "Fix Node.js EADDRINUSE: port already in use error. Kill existing processes, use different ports, or configure port reuse."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["eaddrinuse", "port", "address-in-use", "server", "listen"]
weight: 5
---

# Node.js EADDRINUSE — port already in use

This error occurs when a Node.js server tries to bind to a TCP port that is already occupied by another process. It is extremely common during development with hot-reloading.

## What This Error Means

Common error messages:

- `Error: listen EADDRINUSE: address already in use :::3000`
- `Error: listen EADDRINUSE 0.0.0.0:8080`
- `Port 3000 is already in use`

The `EADDRINUSE` code means "Error ADDRess IN USE" — another process is already listening on that port.

## Common Causes

```javascript
// Cause 1: Previous server instance still running
const server = app.listen(3000);
// Without closing, restart script = EADDRINUSE

// Cause 2: Two server processes on same port
// Terminal 1: node server.js (port 3000)
// Terminal 2: node server.js (port 3000) — EADDRINUSE

// Cause 3: Previous dev server didn't shut down cleanly
// webpack-dev-server, vite, etc. left zombie process

// Cause 4: Another application uses the port
// PostgreSQL on 5432, Redis on 6379, etc.
```

## How to Fix

### Fix 1: Find and kill the process

```bash
# Find process on port 3000
lsof -i :3000

# Kill by PID
kill -9 <PID>

# Or use fuser
fuser -k 3000/tcp
```

### Fix 2: Use a different port

```javascript
const PORT = process.env.PORT || 3001; // try 3001 if 3000 taken
const server = app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

server.on('error', (err) => {
  if (err.code === 'EADDRINUSE') {
    console.log(`Port ${PORT} in use, trying ${PORT + 1}`);
    app.listen(PORT + 1);
  }
});
```

### Fix 3: Enable SO_REUSEADDR

```javascript
const http = require('http');
const server = http.createServer(app);

server.on('error', (err) => {
  if (err.code === 'EADDRINUSE') {
    console.log('Port in use, retrying with SO_REUSEADDR...');
    server.close();
    server.listen({ port: PORT, reuseAddress: true });
  }
});

server.listen(PORT);
```

### Fix 4: Kill all node processes

```bash
# Kill all node processes
pkill -f node

# On macOS
killall node

# Nuclear option
kill -9 $(lsof -t -i:3000)
```

## Examples

```javascript
// This triggers EADDRINUSE
const http = require('http');

const server1 = http.createServer();
server1.listen(3000, () => console.log('Server 1 on 3000'));

const server2 = http.createServer();
server2.listen(3000, () => console.log('Server 2 on 3000'));
// Error: listen EADDRINUSE: address already in use :::3000
```

## Related Errors

- [ECONNREFUSED]({{< relref "/languages/javascript/econnrefused-node" >}}) — connection refused
- [ETIMEDOUT]({{< relref "/languages/javascript/etimedout" >}}) — connection timed out
- [Express Route 404]({{< relref "/languages/javascript/express-route" >}}) — route not found
