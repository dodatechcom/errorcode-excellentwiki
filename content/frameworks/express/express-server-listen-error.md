---
title: "[Solution] Express Server Listen Error"
description: "Fix Express server listen errors when the application fails to start on the configured port or address."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

A server listen error in Express occurs when `app.listen()` fails to bind to the specified port or address, preventing the server from starting.

## Common Causes

- Port already in use by another process
- Port number below 1024 requires root privileges
- Hostname resolves to an invalid address
- Server already listening on the same port in test setup
- EACCES permission denied on privileged ports

## How to Fix

1. Handle listen errors with event listeners:

```javascript
const server = app.listen(process.env.PORT || 3000);

server.on('error', (err) => {
  if (err.code === 'EADDRINUSE') {
    console.error(`Port ${process.env.PORT} is already in use`);
    process.exit(1);
  }
  if (err.code === 'EACCES') {
    console.error(`Permission denied on port ${process.env.PORT}`);
    process.exit(1);
  }
  throw err;
});

server.on('listening', () => {
  console.log(`Server running on port ${process.env.PORT || 3000}`);
});
```

2. Use a different port when the primary is busy:

```javascript
function startServer(port) {
  const server = app.listen(port);

  server.on('error', (err) => {
    if (err.code === 'EADDRINUSE' && port < 65535) {
      console.warn(`Port ${port} in use, trying ${port + 1}`);
      startServer(port + 1);
    } else {
      throw err;
    }
  });

  server.on('listening', () => {
    console.log(`Listening on port ${port}`);
  });
}

startServer(3000);
```

3. Check port availability before starting:

```javascript
const net = require('net');

function isPortAvailable(port) {
  return new Promise((resolve) => {
    const server = net.createServer();
    server.once('error', () => resolve(false));
    server.once('listening', () => {
      server.close(() => resolve(true));
    });
    server.listen(port);
  });
}

async function main() {
  const port = parseInt(process.env.PORT, 10) || 3000;
  if (await isPortAvailable(port)) {
    app.listen(port, () => console.log(`Running on ${port}`));
  } else {
    console.error(`Port ${port} is unavailable`);
    process.exit(1);
  }
}
```

## Examples

```javascript
// Error when port 3000 is already in use
const server = app.listen(3000, () => {
  console.log('Server started');
});

server.on('error', (err) => {
  // EADDRINUSE: address already in use :::3000
});
```

```text
Error: listen EADDRINUSE: address already in use :::3000
```
