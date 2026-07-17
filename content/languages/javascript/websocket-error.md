---
title: "[Solution] WebSocket Connection Error Fix"
description: "Fix WebSocket connection errors in browsers and Node.js. Handle connection failures, close events, and protocol issues."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# WebSocket Connection Error

This error occurs when a WebSocket connection fails to establish, drops unexpectedly, or encounters protocol errors during communication.

## What This Error Means

Common error messages:

- `WebSocket connection to 'ws://...' failed`
- `WebSocket is already in CLOSING or CLOSED state`
- `WebSocket connection closed abnormally`

WebSocket provides full-duplex communication. Errors can occur during handshake, message exchange, or disconnection.

## Common Causes

```javascript
// Cause 1: Server not supporting WebSocket
const ws = new WebSocket('http://localhost:3000'); // upgrade fails

// Cause 2: WSS without proper TLS
const ws = new WebSocket('wss://self-signed.example.com');

// Cause 3: Sending to closed socket
const ws = new WebSocket('ws://localhost:3000');
ws.close();
ws.send('data'); // WebSocket is closed

// Cause 4: Max message size exceeded
ws.send(largeBuffer); // message too large
```

## How to Fix

### Fix 1: Handle connection lifecycle

```javascript
const ws = new WebSocket('ws://localhost:3000');

ws.onopen = () => {
  console.log('Connected');
  ws.send('hello');
};

ws.onmessage = (event) => {
  console.log('Received:', event.data);
};

ws.onerror = (error) => {
  console.error('WebSocket error:', error);
};

ws.onclose = (event) => {
  console.log('Closed:', event.code, event.reason);
};
```

### Fix 2: Implement reconnection

```javascript
class ReconnectingWebSocket {
  constructor(url, maxRetries = 5) {
    this.url = url;
    this.maxRetries = maxRetries;
    this.connect();
  }

  connect() {
    this.ws = new WebSocket(this.url);
    this.ws.onclose = (event) => {
      if (event.code !== 1000 && this.maxRetries > 0) {
        this.maxRetries--;
        setTimeout(() => this.connect(), 1000);
      }
    };
  }

  send(data) {
    if (this.ws.readyState === WebSocket.OPEN) {
      this.ws.send(data);
    }
  }
}
```

### Fix 3: Check readyState before operations

```javascript
function safeSend(ws, data) {
  if (ws.readyState === WebSocket.OPEN) {
    ws.send(data);
  } else {
    console.warn('WebSocket not open, state:', ws.readyState);
  }
}
```

### Fix 4: Use ws library for Node.js

```javascript
const WebSocket = require('ws');

const wss = new WebSocket.Server({ port: 3000 });

wss.on('connection', (ws) => {
  ws.on('message', (data) => {
    console.log('Received:', data);
  });

  ws.on('error', (err) => {
    console.error('WS error:', err.message);
  });
});
```

## Examples

```javascript
// This triggers WebSocket error
const ws = new WebSocket('ws://localhost:9999');
ws.onerror = (e) => console.error('Error:', e.message);
// Error: WebSocket connection to 'ws://localhost:9999' failed
```

## Related Errors

- [Socket.IO Error]({{< relref "/languages/javascript/socket-io-error" >}}) — Socket.IO error
- [ECONNREFUSED]({{< relref "/languages/javascript/econnrefused-node" >}}) — connection refused
- [ETIMEDOUT]({{< relref "/languages/javascript/etimedout" >}}) — timeout
