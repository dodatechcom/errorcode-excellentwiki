---
title: "[Solution] Nginx WebSocket Error"
description: "Fix Nginx websocket errors. Learn why this happens and how to resolve it quickly."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Nginx WebSocket Error

Nginx WebSocket errors occur when WebSocket connections fail to upgrade or maintain.

## Why This Happens

- Upgrade failed
- Connection closed
- Protocol mismatch
- Timeout exceeded

## Common Error Messages

- `websocket_upgrade_error`
- `websocket_connection_error`
- `websocket_protocol_error`
- `websocket_timeout_error`

## How to Fix It

### Solution 1: Configure WebSocket

Set up WebSocket proxying:

```nginx
location /ws/ {
    proxy_pass http://backend;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "Upgrade";
}
```

### Solution 2: Fix timeout issues

Increase WebSocket timeout:

```nginx
proxy_read_timeout 3600s;
proxy_send_timeout 3600s;
```

### Solution 3: Fix connection issues

Ensure proper headers are set.


## Common Scenarios

- **Upgrade failed:** Check if WebSocket headers are set correctly.
- **Connection closed:** Increase timeout values.

## Prevent It

- Configure WebSocket properly
- Set appropriate timeouts
- Test WebSocket connections
