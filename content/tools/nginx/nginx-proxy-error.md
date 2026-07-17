---
title: "[Solution] Nginx Reverse Proxy Error"
description: "Fix Nginx reverse proxy errors. Resolve proxy_pass configuration issues."
tools: ["nginx"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

A reverse proxy error occurs when Nginx cannot properly forward requests to the backend server. This can be caused by misconfiguration, connectivity issues, or protocol mismatches.

## Common Causes

- proxy_pass directive has incorrect URL or port
- Backend server is not running on the expected address
- Missing or incorrect proxy headers
- WebSocket upgrade not configured
- Buffer size too small for backend response

## How to Fix

### Verify proxy_pass Configuration

```nginx
location /api/ {
    proxy_pass http://127.0.0.1:8080;
}
```

### Add Required Proxy Headers

```nginx
location / {
    proxy_pass http://backend;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
}
```

### Configure WebSocket Proxy

```nginx
location /ws/ {
    proxy_pass http://backend;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
}
```

### Increase Buffer Size

```nginx
proxy_buffer_size 128k;
proxy_buffers 4 256k;
```

## Examples

```nginx
# Missing trailing slash
proxy_pass http://127.0.0.1:8080;
# Location: /api/users
# Proxied to: http://127.0.0.1:8080/api/users

# Trailing slash strips location prefix
proxy_pass http://127.0.0.1:8080/;
# Location: /api/users
# Proxied to: http://127.0.0.1:8080/users
```

## Related Errors

- [Nginx 502 Bad Gateway]({{< relref "/tools/nginx/nginx-502-error" >}}) — upstream invalid response
- [Nginx Upstream Error]({{< relref "/tools/nginx/nginx-upstream-error" >}}) — upstream timed out
