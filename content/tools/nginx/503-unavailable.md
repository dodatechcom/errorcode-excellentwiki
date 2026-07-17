---
title: "[Solution] Nginx 503 Service Temporarily Unavailable"
description: "Fix Nginx 503 Service Temporarily Unavailable error. Resolve upstream overload and maintenance issues."
tools: ["nginx"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Nginx 503 Service Temporarily Unavailable

A 503 error indicates the upstream server is temporarily unable to handle requests. This typically means the server is overloaded, in maintenance mode, or has hit a resource limit.

## Common Causes

- The upstream server is overloaded or has too many concurrent connections
- The server is in maintenance mode
- Rate limiting or connection limits are blocking requests
- The upstream server's thread or worker pool is exhausted

## How to Fix

### Check Upstream Server Load

```bash
# Check system load
uptime
top -bn1 | head -20

# Check if the service is running
sudo systemctl status <upstream-service>
```

### Increase Upstream Capacity

```nginx
upstream backend {
    server 127.0.0.1:8080 max_fails=3 fail_timeout=30s;
    server 127.0.0.1:8081 max_fails=3 fail_timeout=30s;
}
```

### Disable Maintenance Mode

```bash
# Check if a maintenance flag exists
rm /var/www/html/maintenance.flag
sudo systemctl restart <upstream-service>
```

### Adjust Connection Limits

```nginx
# Increase worker connections
events {
    worker_connections 4096;
}
```

## Examples

```nginx
# Server overloaded with too many requests
# 503 Service Temporarily Unavailable
# Fix: add more upstream servers or increase capacity

# Maintenance mode active
# 503 Service Temporarily Unavailable
# Fix: remove maintenance flag and restart service
```

## Related Errors

- [502 Bad Gateway]({{< relref "/tools/nginx/502-bad-gateway" >}}) — invalid upstream response
- [Upstream Timed Out]({{< relref "/tools/nginx/upstream-error" >}}) — upstream too slow
