---
title: "[Solution] Socket.IO Connection Error Fix"
description: "Fix Socket.IO connection errors, authentication failures, and real-time communication issues. Handle reconnection and namespace errors."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["socketio", "websocket", "realtime", "connection", "namespace"]
weight: 5
---

# Socket.IO Connection Error

This error occurs when Socket.IO fails to establish or maintain a WebSocket connection. It can involve connection failures, authentication issues, or namespace problems.

## What This Error Means

Common error messages:

- `Error: connect ECONNREFUSED (Socket.IO)`
- `Socket.IO: connect_error`
- `WebSocket connection to 'ws://...' failed`

Socket.IO falls back to HTTP long-polling when WebSocket is unavailable. Connection errors indicate both transport methods failed.

## Common Causes

```javascript
// Cause 1: Server not running
const socket = io('http://localhost:3000'); // ECONNREFUSED

// Cause 2: CORS misconfiguration
const socket = io('https://api.example.com'); // CORS error

// Cause 3: Authentication failure
const socket = io('http://localhost:3000', {
  auth: { token: 'invalid' },
});

// Cause 4: Namespace doesn't exist
const socket = io('http://localhost:3000/nonexistent');
```

## How to Fix

### Fix 1: Configure CORS on server

```javascript
const io = new Server(httpServer, {
  cors: {
    origin: 'http://localhost:5173',
    methods: ['GET', 'POST'],
  },
});
```

### Fix 2: Handle connection events

```javascript
const socket = io('http://localhost:3000');

socket.on('connect', () => {
  console.log('Connected:', socket.id);
});

socket.on('connect_error', (err) => {
  console.error('Connection error:', err.message);
});

socket.on('disconnect', (reason) => {
  console.log('Disconnected:', reason);
});
```

### Fix 3: Add reconnection logic

```javascript
const socket = io('http://localhost:3000', {
  reconnection: true,
  reconnectionAttempts: 10,
  reconnectionDelay: 1000,
  reconnectionDelayMax: 5000,
});
```

### Fix 4: Handle authentication

```javascript
// Server
io.use((socket, next) => {
  const token = socket.handshake.auth.token;
  if (isValidToken(token)) {
    next();
  } else {
    next(new Error('authentication error'));
  }
});

// Client
const socket = io('http://localhost:3000', {
  auth: { token: getUserToken() },
});
```

## Examples

```javascript
// This triggers connection error
const socket = io('http://nonexistent-server:3000');

socket.on('connect_error', (err) => {
  console.error('Failed to connect:', err.message);
  // "Failed to connect: connect ECONNREFUSED"
});
```

## Related Errors

- [ECONNREFUSED]({{< relref "/languages/javascript/econnrefused-node" >}}) — connection refused
- [WebSocket Error]({{< relref "/languages/javascript/websocket-error" >}}) — WebSocket error
- [CORS Error]({{< relref "/languages/javascript/cors-error" >}}) — CORS policy error
