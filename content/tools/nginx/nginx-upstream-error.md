---
title: "[Solution] Nginx Upstream Timed Out"
description: "Fix Nginx upstream timed out error. Resolve upstream server timeout issues."
tools: ["nginx"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

An upstream timed out error means Nginx waited too long for a response from the upstream server. The backend process is slow or unresponsive.

## Common Causes

- Backend application is slow to respond
- Database queries are taking too long
- Upstream server is overloaded with requests
- Network latency between Nginx and upstream
- Timeout values too low for the workload

## How to Fix

### Increase Proxy Timeout

```nginx
location / {
    proxy_pass http://backend;
    proxy_read_timeout 300s;
    proxy_connect_timeout 60s;
    proxy_send_timeout 300s;
}
```

### Check Backend Performance

```bash
curl -w "time_total: %{time_total}\n" http://127.0.0.1:8080/
```

### Monitor Upstream Health

```bash
sudo tail -f /var/log/nginx/error.log | grep upstream
```

### Optimize Backend

```bash
# Add caching
# Optimize database queries
# Scale backend horizontally
```

### Configure Keepalive

```nginx
upstream backend {
    server 127.0.0.1:8080;
    keepalive 32;
}
```

## Examples

```nginx
# Default 60s timeout
# upstream timed out (110: Connection timed out)
# Fix: increase proxy_read_timeout

# Slow API endpoint
proxy_read_timeout 600s;
# For endpoints that take up to 10 minutes
```

## Related Errors

- [Nginx 504 Timeout]({{< relref "/tools/nginx/nginx-504-error" >}}) — gateway timeout
- [Nginx 502 Bad Gateway]({{< relref "/tools/nginx/nginx-502-error" >}}) — upstream invalid response
