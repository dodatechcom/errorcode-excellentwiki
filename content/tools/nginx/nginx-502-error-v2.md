---
title: "[Solution] Nginx 502 Bad Gateway — upstream prematurely closed connection"
description: "Fix Nginx 502 Bad Gateway upstream prematurely closed connection. Resolve upstream connection drops."
tools: ["nginx"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["nginx", "502", "bad-gateway", "upstream", "connection", "closed"]
weight: 5
---

An Nginx 502 Bad Gateway with "upstream prematurely closed connection" means the backend server closed the TCP connection before sending a complete response. Nginx received a partial or empty response and returned 502 to the client.

## What This Error Means

Nginx acts as a reverse proxy and expects the upstream server to send a complete HTTP response. When the upstream closes the connection unexpectedly — before sending headers or the response body — Nginx logs `upstream prematurely closed connection while reading response header` and returns 502. This typically indicates the backend process crashed, ran out of memory, or terminated prematurely.

## Common Causes

- Backend process (PHP-FPM, Node.js, Gunicorn) crashed during request processing
- Backend hit a memory limit and was killed by the OS OOM killer
- Backend closed the connection due to an unhandled exception
- `proxy_read_timeout` too low for slow backend responses
- Backend is not configured to handle keep-alive connections properly
- Mismatched HTTP protocol versions between Nginx and upstream

## How to Fix

### Check Nginx Error Logs

```bash
sudo tail -f /var/log/nginx/error.log | grep "upstream prematurely closed"
```

### Check Backend Process Status

```bash
sudo systemctl status php8.2-fpm
ps aux | grep gunicorn
docker ps | grep backend
```

### Increase Proxy Timeouts

```nginx
proxy_connect_timeout 60s;
proxy_send_timeout 60s;
proxy_read_timeout 120s;
proxy_buffering on;
proxy_buffer_size 128k;
proxy_buffers 4 256k;
```

### Fix Backend Memory Issues

```bash
# Check PHP-FPM memory settings
grep memory_limit /etc/php/8.2/fpm/php.ini

# Increase PHP-FPM memory
memory_limit = 512M
```

### Enable Proxy Buffering

```nginx
location / {
    proxy_pass http://backend;
    proxy_buffering on;
    proxy_buffer_size 16k;
    proxy_buffers 4 32k;
}
```

### Use HTTP Keep-Alive to Backend

```nginx
upstream backend {
    server 127.0.0.1:8080;
    keepalive 32;
}

location / {
    proxy_pass http://backend;
    proxy_http_version 1.1;
    proxy_set_header Connection "";
}
```

### Fix Backend Process Limits

```bash
# Increase ulimits for PHP-FPM
# /etc/security/limits.conf
www-data soft nofile 65535
www-data hard nofile 65535
```

## Related Errors

- [Nginx 504 Timeout]({{< relref "/tools/nginx/nginx-504-error-v2" >}}) — upstream timed out
- [Nginx Upstream Error]({{< relref "/tools/nginx/nginx-upstream-error-v2" >}}) — connection refused
- [Nginx Proxy Error]({{< relref "/tools/nginx/nginx-proxy-error-v2" >}}) — proxy_pass error
