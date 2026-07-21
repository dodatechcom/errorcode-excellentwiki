---
title: "[Solution] Nginx Upstream Timed Out Error"
description: "Nginx upstream connection times out because the backend server did not respond within the configured timeout period."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

# Nginx Upstream Timed Out Error

Nginx upstream timed out error (110: Connection timed out) occurs when the upstream server does not send a complete response within the configured timeout. The error log records which stage timed out.

## Common Causes

- The upstream server is not responding due to high load or crashes
- The `proxy_read_timeout` is too short for long-running requests
- The upstream server is processing a slow database query
- Network issues between Nginx and the upstream server

## How to Fix

1. Increase the relevant timeout directives:

```nginx
location / {
    proxy_pass http://backend;
    proxy_connect_timeout 10s;
    proxy_read_timeout 300s;
    proxy_send_timeout 300s;
}
```

2. Enable failover to the next upstream on timeout:

```nginx
location / {
    proxy_pass http://backend;
    proxy_next_upstream error timeout http_502 http_503;
    proxy_next_upstream_tries 3;
}
```

3. Monitor upstream server health:

```bash
# Check if the upstream server is responding
curl -w "Time: %{time_total}s\n" -o /dev/null -s http://127.0.0.1:8080/health
```

4. Add connection keepalive for faster subsequent requests:

```nginx
upstream backend {
    server 127.0.0.1:8080;
    keepalive 32;
}
```

## Examples

```nginx
# Timeout configuration for long-running APIs
location /api/reports {
    proxy_pass http://backend;
    proxy_read_timeout 600s;
    proxy_connect_timeout 10s;
    proxy_next_upstream timeout error;
}
```

```bash
# Check Nginx error log for timeout details
tail -f /var/log/nginx/error.log | grep "upstream timed out"
```

## Related Errors

- [Proxy Timeout Error]({{< relref "/tools/nginx/nginx-proxy-timeout-error" >}}) -- general timeout issues
- [Upstream Error]({{< relref "/tools/nginx/nginx-upstream-error" >}}) -- upstream connection failures
