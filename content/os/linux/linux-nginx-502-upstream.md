---
title: "[Solution] Linux nginx 502 Bad Gateway — Upstream Error"
description: "Fix Linux nginx 502 Bad Gateway upstream errors. Resolve proxy issues, upstream connection failures, and gateway errors."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["nginx", "502", "bad-gateway", "upstream", "proxy", "reverse-proxy"]
weight: 5
---

# Linux: nginx — 502 Bad Gateway — upstream error

The nginx `502 Bad Gateway` error means nginx received an invalid response from the upstream server or could not connect to it at all. nginx acts as a reverse proxy and expects the backend application to respond with a valid HTTP response — when it does not, nginx returns 502 to the client.

## What This Error Means

nginx is configured to proxy requests to an upstream server (application server). A 502 error indicates the upstream is not responding correctly: it may be down, not listening on the expected port, crashing during request handling, or returning malformed data. The nginx error log will contain details about why the upstream connection failed.

## Common Causes

- Backend application server is down or crashed
- Upstream server not listening on the configured port
- FastCGI/PHP-FPM process not running (for PHP sites)
- Proxy buffer too small for the upstream response
- Upstream server overloaded and dropping connections
- Unix socket path incorrect or permissions wrong
- DNS resolution failure for upstream hostname

## How to Fix

### 1. Check nginx Error Log

```bash
# View the error log for details
sudo tail -50 /var/log/nginx/error.log

# Common error messages:
# "connect() failed (111: Connection refused)" — upstream not listening
# "upstream prematurely closed connection" — upstream crashed
# "no live upstreams" — all upstream servers are down
```

### 2. Verify Upstream Server Is Running

```bash
# Check if the backend process is running
sudo systemctl status <backend-service>

# Check if the port is listening
sudo ss -tlnp | grep <upstream-port>

# For PHP-FPM
sudo systemctl status php8.1-fpm
sudo ss -tlnp | grep 9000
```

### 3. Test Upstream Directly

```bash
# Bypass nginx and test the backend
curl -v http://127.0.0.1:<upstream-port>/

# For FastCGI
cgi-fcgi -bind -connect 127.0.0.1:9000

# For Unix socket
curl -v --unix-socket /run/php/php8.1-fpm.sock http://localhost/
```

### 4. Fix nginx Upstream Configuration

```nginx
# /etc/nginx/sites-available/mysite.conf

upstream backend {
    server 127.0.0.1:8080;
    keepalive 32;
}

server {
    listen 80;
    server_name example.com;

    location / {
        proxy_pass http://backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

        # Increase timeouts
        proxy_connect_timeout 60s;
        proxy_read_timeout 60s;
        proxy_send_timeout 60s;
    }
}
```

### 5. Fix PHP-FPM Issues

```bash
# Check PHP-FPM status
sudo systemctl status php8.1-fpm

# Check FPM pool configuration
sudo grep -r 'listen' /etc/php/8.1/fpm/pool.d/

# Ensure nginx and PHP-FPM use the same socket/port
# nginx: fastcgi_pass unix:/run/php/php8.1-fpm.sock
# PHP-FPM: listen = /run/php/php8.1-fpm.sock

# Restart PHP-FPM
sudo systemctl restart php8.1-fpm

# Check socket permissions
ls -la /run/php/php8.1-fpm.sock
```

### 6. Increase Proxy Buffer Size

```nginx
# In nginx config
proxy_buffer_size 128k;
proxy_buffers 4 256k;
proxy_busy_buffers_size 256k;

# For large responses
proxy_buffering off;
```

### 7. Reload nginx After Changes

```bash
# Test configuration
sudo nginx -t

# Reload without downtime
sudo nginx -s reload

# Full restart if needed
sudo systemctl restart nginx
```

## Examples

```bash
$ curl -I http://example.com
HTTP/1.1 502 Bad Gateway
Server: nginx/1.18.0

$ sudo tail -5 /var/log/nginx/error.log
2025/07/14 10:00:00 [error] 1234#1234: *5678 connect() failed (111: Connection refused) while connecting to upstream,
client: 192.168.1.10, server: example.com, upstream: "http://127.0.0.1:8080", host: "example.com"

$ sudo ss -tlnp | grep 8080
# Nothing listening — backend is down

$ sudo systemctl start myapp
$ sudo ss -tlnp | grep 8080
LISTEN  0  128  127.0.0.1:8080  0.0.0.0:*  users:(("myapp",pid=5678))

$ curl -I http://example.com
HTTP/1.1 200 OK
```

## Related Errors

- [nginx 504 timeout]({{< relref "/os/linux/linux-nginx-504-timeout" >}}) — Upstream timed out
- [nginx 403 forbidden]({{< relref "/os/linux/linux-nginx-403-forbidden" >}}) — Permission denied
- [MySQL connection refused]({{< relref "/os/linux/linux-mysql-connection-refused" >}}) — Database connection issues
