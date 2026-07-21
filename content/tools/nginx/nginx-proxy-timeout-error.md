---
title: "[Solution] Nginx Proxy Timeout Error"
description: "Nginx proxy_pass times out waiting for a response from the upstream server, returning a 504 Gateway Timeout to the client."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

# Nginx Proxy Timeout Error

Nginx proxy timeout occurs when the upstream server takes too long to respond. Nginx closes the connection and returns 504 Gateway Timeout to the client.

## Common Causes

- The upstream server is overloaded or slow to respond
- The `proxy_read_timeout` value is too low for the application
- The backend application is blocking on database or external API calls
- Network latency between Nginx and the upstream server is high

## How to Fix

1. Increase the proxy timeout values:

```nginx
location / {
    proxy_pass http://backend;
    proxy_connect_timeout 60s;
    proxy_send_timeout 60s;
    proxy_read_timeout 120s;
}
```

2. Configure keepalive connections to the upstream:

```nginx
upstream backend {
    server 127.0.0.1:8080;
    keepalive 32;
}

server {
    location / {
        proxy_pass http://backend;
        proxy_http_version 1.1;
        proxy_set_header Connection "";
    }
}
```

3. Add proxy buffering for large responses:

```nginx
location / {
    proxy_pass http://backend;
    proxy_buffering on;
    proxy_buffer_size 4k;
    proxy_buffers 8 4k;
}
```

4. Monitor upstream response times:

```bash
tail -f /var/log/nginx/access.log | grep 504
```

## Examples

```nginx
# Timeout configuration for slow APIs
location /api/ {
    proxy_pass http://backend;
    proxy_read_timeout 300s;
    proxy_connect_timeout 10s;
    proxy_next_upstream error timeout http_502 http_503;
}
```

```nginx
# Upstream with keepalive
upstream backend {
    server 127.0.0.1:8080;
    keepalive 64;
}
```

## Related Errors

- [Upstream Timed Out]({{< relref "/tools/nginx/nginx-upstream-timed-out-error" >}}) -- upstream timeout issues
- [Proxy Buffer Error]({{< relref "/tools/nginx/nginx-proxy-buffer-error" >}}) -- proxy buffer configuration
