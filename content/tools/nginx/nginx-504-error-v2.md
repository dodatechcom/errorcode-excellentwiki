---
title: "[Solution] Nginx 504 Gateway Timeout — upstream timed out"
description: "Fix Nginx 504 Gateway Timeout upstream timed out. Resolve upstream server timeout issues."
tools: ["nginx"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["nginx", "504", "gateway-timeout", "upstream", "timeout", "slow"]
weight: 5
---

An Nginx 504 Gateway Timeout with "upstream timed out" means the backend server took too long to respond. Nginx waited for the configured timeout duration and gave up before receiving a complete response.

## What This Error Means

Nginx enforces timeouts when proxying requests to upstream servers. When the backend does not respond within `proxy_read_timeout` (default 60s), Nginx terminates the connection and returns 504. The error log shows `upstream timed out (110: Connection timed out) while reading response header`. This indicates the backend is either processing too slowly, blocked on a resource, or deadlocked.

## Common Causes

- Backend process is performing a slow query or long-running operation
- Database connection pool exhausted causing request queuing
- External API call from backend is hanging
- `proxy_read_timeout` set too low for the workload
- Backend server is overloaded and cannot process requests in time
- Deadlock in backend application code

## How to Fix

### Check Nginx Error Logs

```bash
sudo tail -f /var/log/nginx/error.log | grep "upstream timed out"
```

### Increase Proxy Read Timeout

```nginx
location / {
    proxy_pass http://backend;
    proxy_read_timeout 180s;
    proxy_connect_timeout 10s;
    proxy_send_timeout 60s;
}
```

### Add Request Timeout to Backend

```nginx
location /api/slow-endpoint {
    proxy_pass http://backend;
    proxy_read_timeout 300s;
}
```

### Check Backend Query Performance

```bash
# MySQL slow query log
tail -f /var/log/mysql/slow-query.log

# PostgreSQL
SELECT * FROM pg_stat_activity WHERE state = 'active';
```

### Monitor Backend Response Times

```bash
# Check response times with curl
curl -w "@curl-format.txt" -o /dev/null -s http://backend/endpoint
```

### Use Request Buffering for Large Payloads

```nginx
proxy_request_buffering on;
proxy_buffering on;
client_body_buffer_size 128k;
```

### Implement Request Queuing

```nginx
upstream backend {
    server 127.0.0.1:8080 max_fails=3 fail_timeout=30s;
    server 127.0.0.1:8081 max_fails=3 fail_timeout=30s;
    keepalive 16;
}
```

## Related Errors

- [Nginx 502 Bad Gateway]({{< relref "/tools/nginx/nginx-502-error-v2" >}}) — upstream connection closed
- [Nginx Upstream Error]({{< relref "/tools/nginx/nginx-upstream-error-v2" >}}) — connection refused
- [Nginx Limit Request]({{< relref "/tools/nginx/nginx-limit-req-v2" >}}) — rate limiting 503
