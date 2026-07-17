---
title: "[Solution] Nginx 504 Gateway Timeout"
description: "Fix Nginx 504 Gateway Timeout error. Diagnose upstream server timeout issues."
tools: ["nginx"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

A 504 Gateway Timeout means the upstream server did not respond within the configured time limit. Nginx timed out while waiting for the backend to process the request.

## Common Causes

- Upstream server is too slow to process requests
- Database queries taking too long
- Upstream server is overloaded
- Network latency between Nginx and upstream
- Timeout values too low for the workload

## How to Fix

### Increase Proxy Timeout

```nginx
location /api/ {
    proxy_pass http://127.0.0.1:8080;
    proxy_read_timeout 300s;
    proxy_connect_timeout 60s;
}
```

### Check Upstream Performance

```bash
curl -w "time_total: %{time_total}\n" http://127.0.0.1:8080/api
```

### Monitor Upstream Response Time

```bash
sudo tail -f /var/log/nginx/access.log | awk '{print $NF}'
```

### Optimize Backend Application

```bash
# Profile the backend application
# Check database query performance
# Add caching layer
```

### Increase FastCGI Timeout (PHP)

```nginx
fastcgi_read_timeout 300s;
```

## Examples

```nginx
# Default timeout too low
proxy_read_timeout 60s;
# API takes 2 minutes to process
# Fix: increase to 300s

# PHP-FPM timeout
fastcgi_read_timeout 300s;
```

## Related Errors

- [Nginx 502 Bad Gateway]({{< relref "/tools/nginx/nginx-502-error" >}}) — upstream invalid response
- [Nginx Upstream Error]({{< relref "/tools/nginx/nginx-upstream-error" >}}) — upstream timed out
