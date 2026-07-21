---
title: "Nginx Stub Status Page Error"
description: "Nginx stub_status module not available or misconfigured"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Nginx Stub Status Page Error

Nginx stub_status module not available or misconfigured

## Common Causes

- stub_status module not compiled into Nginx
- stub_status directive in wrong context
- Access to /nginx_status restricted by IP
- Module loaded but not configured

## How to Fix

1. Check modules: `nginx -V 2>&1 | grep stub_status`
2. Add to server block: `location /nginx_status { stub_status; }`
3. Restrict access: `allow 127.0.0.1; deny all;`
4. Test: `curl http://localhost/nginx_status`

## Examples

```nginx
# Enable stub_status
server {
    location /nginx_status {
        stub_status;
        allow 127.0.0.1;
        deny all;
    }
}
```
