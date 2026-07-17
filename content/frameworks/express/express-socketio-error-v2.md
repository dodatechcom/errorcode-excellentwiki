---
title: "Socket.IO Connection Error in Express"
description: "Fix Socket.IO errors when WebSocket connections fail, drop, or cannot establish due to server or transport issues."
frameworks: ["express.js"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Socket.IO adds real-time bidirectional communication on top of Express. Connection errors occur when the WebSocket handshake fails, the server is behind a proxy that doesn't support upgrades, CORS blocks the connection, or the transport falls back to polling incorrectly.

## Common Causes

- CORS not configured for Socket.IO connections
- Reverse proxy (nginx, Cloudflare) not configured for WebSocket upgrades
- Socket.IO server attached to the wrong HTTP server instance
- Transport type mismatch between client and server
- Connection timeout due to network issues or firewall blocking

## How to Fix

### Set Up Socket.IO with CORS

```javascript
const express = require('express');
const http = require('http');
const { Server } = require('socket.io');

const app = express();
const server = http.createServer(app);

const io = new Server(server, {
  cors: {
    origin: ['https://yourdomain.com'],
    methods: ['GET', 'POST'],
    credentials: true
  },
  pingTimeout: 60000,
  pingInterval: 25000
});

io.on('connection', (socket) => {
  console.log('Client connected:', socket.id);

  socket.on('disconnect', (reason) => {
    console.log('Client disconnected:', socket.id, reason);
  });

  socket.on('error', (err) => {
    console.error('Socket error:', err);
  });
});

server.listen(3000);
```

### Handle Connection Errors Gracefully

```javascript
io.on('connection', (socket) => {
  socket.on('connect_error', (err) => {
    console.error('Connection error:', err.message);
    socket.emit('error', { message: 'Connection issue detected' });
  });

  socket.on('reconnect_attempt', (attempt) => {
    console.log(`Reconnection attempt: ${attempt}`);
  });

  socket.on('reconnect', () => {
    console.log('Reconnected successfully');
  });
});
```

### Configure for Nginx Reverse Proxy

```nginx
# nginx.conf
location /socket.io/ {
  proxy_pass http://localhost:3000;
  proxy_http_version 1.1;
  proxy_set_header Upgrade $http_upgrade;
  proxy_set_header Connection "upgrade";
  proxy_set_header Host $host;
  proxy_set_header X-Real-IP $remote_addr;
  proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
  proxy_set_header X-Forwarded-Proto $scheme;
  proxy_read_timeout 86400;
}
```

### Handle Room and Namespace Errors

```javascript
const adminNs = io.of('/admin');
adminNs.on('connection', (socket) => {
  socket.on('join-room', (roomId) => {
    socket.join(roomId);
    console.log(`Socket ${socket.id} joined room ${roomId}`);
  });

  socket.on('error', (err) => {
    console.error('Namespace error:', err);
  });
});
```

### Client-Side Reconnection Strategy

```javascript
// Client-side configuration
const socket = io('https://yourdomain.com', {
  transports: ['websocket', 'polling'],
  reconnection: true,
  reconnectionAttempts: 10,
  reconnectionDelay: 1000,
  reconnectionDelayMax: 5000,
  timeout: 20000
});

socket.on('connect_error', (err) => {
  console.error('Connection failed:', err.message);
});
```

## Related Errors

- [Express CORS Error]({{< relref "/frameworks/express/express-cors-error-v2" >}}) — Socket.IO CORS misconfiguration
- [Express Proxy Error]({{< relref "/frameworks/express/express-proxy-error-v2" >}}) — proxy not forwarding WebSocket
