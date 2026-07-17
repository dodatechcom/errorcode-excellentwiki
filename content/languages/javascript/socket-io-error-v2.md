---
title: "[Solution] Socket.IO: Connection Error Fix"
description: "Fix Socket.IO connection errors including transport failures, authentication issues, and namespace errors."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Socket.IO: Connection Error

This error occurs when a Socket.IO client fails to establish or maintain a connection to the server. It covers transport failures, authentication rejects, namespace issues, and connection timeouts.

## What This Error Means

Common error messages:

- `Error: websocket error`
- `Error: xhr poll error`
- `connect_error: xhr post error (Pending)`
- `connect_error: server error (type: "Unauthorized")`
- `Error: connection timeout`
- `socket.io-client: url is empty`

Socket.IO tries multiple transports (WebSocket, HTTP long-polling) and retries connecting automatically. The error event fires when all transports fail or the server rejects the connection.

## Common Causes

```javascript
// Cause 1: Server not running or wrong URL
const socket = io('http://localhost:3001'); // server on 3000

// Cause 2: CORS configuration mismatch
// Server: cors: { origin: "https://example.com" }
// Client connects from: http://localhost:5173

// Cause 3: Authentication middleware rejects
io.use((socket, next) => {
  const token = socket.handshake.auth.token;
  if (!token) return next(new Error('Unauthorized'));
  next();
});

// Cause 4: Transport not supported by proxy
// Nginx/WebSocket proxy misconfigured

// Cause 5: Path mismatch between client and server
const socket = io('https://api.example.com', { path: '/ws' });
// Server expects: path: '/socket.io'
```

## How to Fix

### Fix 1: Configure CORS on the server

```javascript
// Server
import { Server } from 'socket.io';

const io = new Server(server, {
  cors: {
    origin: ['http://localhost:5173', 'https://example.com'],
    methods: ['GET', 'POST'],
    credentials: true,
  },
});
```

### Fix 2: Handle connection lifecycle events

```javascript
import { io } from 'socket.io-client';

const socket = io('https://api.example.com', {
  auth: { token: getToken() },
  reconnectionAttempts: 5,
  reconnectionDelay: 1000,
  timeout: 10000,
});

socket.on('connect', () => {
  console.log('Connected:', socket.id);
});

socket.on('connect_error', (err) => {
  console.error('Connection error:', err.message);
  if (err.message === 'Unauthorized') {
    refreshToken();
  }
});

socket.on('disconnect', (reason) => {
  console.log('Disconnected:', reason);
  if (reason === 'io server disconnect') {
    socket.connect(); // server forced disconnect
  }
});
```

### Fix 3: Configure proxy for WebSocket support

```nginx
# nginx.conf
location /socket.io/ {
    proxy_pass http://localhost:3000;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_set_header Host $host;
    proxy_read_timeout 86400;
}
```

### Fix 4: Ensure path matches between client and server

```javascript
// Server
const io = new Server(server, {
  path: '/ws',
});

// Client — must match
const socket = io('https://api.example.com', { path: '/ws' });
```

### Fix 5: Handle authentication token refresh

```javascript
socket.on('connect_error', async (err) => {
  if (err.message.includes('jwt expired')) {
    const newToken = await refreshAuthToken();
    socket.auth.token = newToken;
    socket.connect();
  }
});
```

## Examples

```
socket.io-client: url is empty
socket.io-client: websocket error
socket.io-client: connect attempt timed out
socket.io-client: server error: Unauthorized
```

```javascript
// Fix: check connection before sending
socket.on('connect', () => {
  socket.emit('chat:send', { message: 'Hello' });
});
```

## Related Errors

- [Socket.IO Error]({{< relref "/languages/javascript/socket-io-error" >}}) — basic socket.io error
- [WebSocket Timeout]({{< relref "/languages/javascript/ERR_SOCKET_TIMEOUT" >}}) — socket timeout
- [Axios Error V2]({{< relref "/languages/javascript/axios-error-v2" >}}) — HTTP request failed
