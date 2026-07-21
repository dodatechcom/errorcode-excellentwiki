---
title: "Nginx Keepalive Connection Error"
description: "Nginx keepalive connections causing upstream to reject requests"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Nginx Keepalive Connection Error

Nginx keepalive connections causing upstream to reject requests

## Common Causes

- Upstream server closes keepalive connections prematurely
- keepalive_timeout mismatch between Nginx and upstream
- keepalive_requests limit too high
- Connection pool exhaustion on upstream

## How to Fix

1. Configure keepalive: `keepalive 32;` in upstream block
2. Set keepalive_timeout: `keepalive_timeout 60s;`
3. Limit requests: `keepalive_requests 1000;`
4. Check upstream connection handling

## Examples

```nginx
# Configure keepalive in upstream
upstream backend {
    server backend1:8080;
    keepalive 32;
}

location /api/ {
    proxy_pass http://backend;
    proxy_http_version 1.1;
    proxy_set_header Connection "";
}
```
