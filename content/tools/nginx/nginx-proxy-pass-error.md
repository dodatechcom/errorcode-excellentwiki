---
title: "[Solution] Nginx Proxy Pass Error"
description: "Fix Nginx proxy pass errors. Learn why this happens and how to resolve it quickly."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Nginx Proxy Pass Error

Nginx proxy_pass errors occur when proxying requests to backend servers fails.

## Why This Happens

- Upstream not found
- Connection refused
- Timeout exceeded
- Invalid URL

## Common Error Messages

- `proxy_pass_upstream_error`
- `proxy_pass_connection_error`
- `proxy_pass_timeout_error`
- `proxy_pass_url_error`

## How to Fix It

### Solution 1: Configure proxy_pass

Set up proxy_pass:

```nginx
location /api/ {
    proxy_pass http://backend/;
}
```

### Solution 2: Fix upstream issues

Ensure backend server is running.

### Solution 3: Adjust timeouts

Configure proxy timeout settings.


## Common Scenarios

- **Upstream not found:** Check upstream server configuration.
- **Connection refused:** Verify backend server is running.

## Prevent It

- Configure proxy_pass properly
- Test proxy connectivity
- Monitor proxy performance
