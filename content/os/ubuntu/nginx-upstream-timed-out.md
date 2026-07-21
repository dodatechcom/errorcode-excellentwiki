---
title: "Nginx Upstream Timed Out Error"
description: "Nginx returns 504 Gateway Timeout waiting for upstream server"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Nginx Upstream Timed Out Error

Nginx returns 504 Gateway Timeout waiting for upstream server

## Common Causes

- Upstream server too slow to respond
- Nginx proxy_read_timeout too low
- Upstream server overloaded or crashed
- Network connectivity issue between Nginx and upstream

## How to Fix

1. Increase timeout: `proxy_read_timeout 300s;` in config
2. Check upstream server health
3. Review Nginx error logs: `tail -f /var/log/nginx/error.log`
4. Test upstream directly: `curl http://upstream-server:port`

## Examples

```nginx
# Increase proxy timeout in Nginx config
location /api/ {
    proxy_pass http://backend;
    proxy_read_timeout 300s;
    proxy_connect_timeout 60s;
}
```
