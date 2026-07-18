---
title: "[Solution] Nginx Stream Error"
description: "Fix Nginx stream errors. Learn why this happens and how to resolve it quickly."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Nginx Stream Error

Nginx stream errors occur when TCP/UDP stream proxying fails.

## Why This Happens

- Stream not configured
- Backend unreachable
- Timeout exceeded
- Protocol error

## Common Error Messages

- `stream_config_error`
- `stream_backend_error`
- `stream_timeout_error`
- `stream_protocol_error`

## How to Fix It

### Solution 1: Configure stream

Set up stream proxying:

```nginx
stream {
    upstream backend {
        server 127.0.0.1:3306;
    }
    server {
        listen 3306;
        proxy_pass backend;
    }
}
```

### Solution 2: Fix backend issues

Verify backend servers are running.

### Solution 3: Adjust timeouts

Configure stream timeouts:

```nginx
proxy_timeout 300s;
proxy_connect_timeout 60s;
```


## Common Scenarios

- **Stream not configured:** Add stream block configuration.
- **Backend unreachable:** Check backend server status.

## Prevent It

- Configure stream properly
- Set appropriate timeouts
- Test stream connections
