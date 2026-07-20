---
title: "[Reference] JavaScript WebSocket Close Codes — Status Codes Reference"
description: "Complete reference for JavaScript WebSocket close codes 1000-1015. Understand server/client initiated close, error conditions, and proper close handling."
languages: ["javascript"]
error-types: ["runtime"]
severities: ["error"]
comments: true
weight: 813
---

# JavaScript WebSocket Close Codes

WebSocket close codes are sent in `CloseEvent` when a connection terminates. Codes 1000-1015 are standardized by the WebSocket protocol and indicate different close reasons and error conditions.

## Common Close Codes

### 1000 — Normal Closure

The connection closed normally. No error occurred.

```javascript
ws.close(1000, 'Session ended')
// Event code: 1000, reason: 'Session ended'
```

### 1001 — Going Away

Server or client is shutting down or leaving the page.

```javascript
window.addEventListener('beforeunload', () => {
  ws.close(1001, 'Page unloading')
})
```

### 1002 — Protocol Error

Endpoint received malformed data that violates the WebSocket protocol.

```javascript
// ❌ Server sends invalid frame → code 1002
ws.onclose = (event) => {
  if (event.code === 1002) {
    console.error('Protocol error - malformed frame')
  }
}
```

### 1003 — Unsupported Data

Endpoint received data of a type it cannot accept (e.g., binary-only endpoint received text).

```javascript
ws.onclose = (event) => {
  if (event.code === 1003) {
    console.error('Unsupported data type')
  }
}
```

### 1005 — No Status Received

No close code was provided. Connection closed abruptly.

```javascript
ws.onclose = (event) => {
  // event.code === 1005 when no close frame sent
  console.log('Connection closed without status code')
}
```

### 1006 — Abnormal Closure

Connection closed without a close frame. Usually indicates network failure.

```javascript
ws.onclose = (event) => {
  if (event.code === 1006) {
    console.error('Abnormal closure - possible network issue')
    reconnectWebSocket()
  }
}
```

### 1007 — Invalid Frame Payload Data

UTF-8 validation failed or message data is malformed.

```javascript
ws.onclose = (event) => {
  if (event.code === 1007) {
    console.error('Invalid UTF-8 data received')
  }
}
```

### 1008 — Policy Violation

Connection rejected due to policy violation (e.g., message too large).

```javascript
ws.onclose = (event) => {
  if (event.code === 1008) {
    console.error('Policy violation:', event.reason)
  }
}
```

### 1009 — Message Too Big

Frame or message exceeds the maximum allowed size.

```javascript
ws.onclose = (event) => {
  if (event.code === 1009) {
    console.error('Message exceeds size limit')
    // Reduce payload size and retry
  }
}
```

### 1010 — Mandatory Extension

Client requested an extension that the server does not support.

```javascript
// Server closes with 1010 when extension not available
ws.onclose = (event) => {
  if (event.code === 1010) {
    console.error('Requested extension not available')
  }
}
```

### 1011 — Internal Server Error

Server encountered an unexpected condition.

```javascript
ws.onclose = (event) => {
  if (event.code === 1011) {
    console.error('Server error:', event.reason)
    retryWithBackoff()
  }
}
```

### 1012 — Service Restart

Server is restarting. Client should reconnect.

```javascript
ws.onclose = (event) => {
  if (event.code === 1012) {
    console.log('Server restarting - reconnecting...')
    reconnectWebSocket()
  }
}
```

### 1013 — Try Again Later

Server is temporarily overloaded.

```javascript
ws.onclose = (event) => {
  if (event.code === 1013) {
    console.log('Server busy - retrying later')
    setTimeout(reconnectWebSocket, 5000)
  }
}
```

### 1014 — Bad Gateway

Server acting as gateway received an invalid response.

```javascript
ws.onclose = (event) => {
  if (event.code === 1014) {
    console.error('Bad gateway upstream')
  }
}
```

### 1015 — TLS Handshake Failed

TLS handshake could not be completed. Reserved and not sent by endpoint.

```javascript
// Cannot be sent or received - reserved for TLS layer
ws.onclose = (event) => {
  if (event.code === 1015) {
    console.error('TLS handshake failed')
  }
}
```

## How to Handle Close Codes

```javascript
function handleWebSocketClose(event) {
  console.log(`Closed: code=${event.code}, reason="${event.reason}", wasClean=${event.wasClean}`)

  switch (event.code) {
    case 1000:
      // Normal - no action needed
      break
    case 1001:
    case 1012:
    case 1013:
      // Transient - reconnect
      reconnectWithDelay()
      break
    case 1006:
    case 1011:
    case 1014:
      // Error - reconnect with backoff
      reconnectWithExponentialBackoff()
      break
    case 1002:
    case 1003:
    case 1007:
    case 1008:
    case 1009:
      // Protocol/data error - do not reconnect, log
      console.error('Protocol error:', event.code, event.reason)
      break
    default:
      // Custom codes 3000-4999
      handleCustomCode(event.code, event.reason)
  }
}
```

## Related Errors

- [WebSocket Error](/languages/javascript/websocket-error)
- [WebRTC Error](/languages/javascript/webrtc-error)
- [JavaScript Network Error](/languages/javascript/fetch-network-error)
