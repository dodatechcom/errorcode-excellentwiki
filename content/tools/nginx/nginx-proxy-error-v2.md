---
title: "[Solution] Nginx proxy_pass — connection error"
description: "Fix Nginx proxy_pass connection error. Resolve reverse proxy connection failures."
tools: ["nginx"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["nginx", "proxy", "proxy_pass", "connection", "error", "reverse-proxy"]
weight: 5
---

A proxy_pass connection error means Nginx cannot establish a TCP connection to the upstream server specified in the `proxy_pass` directive. Requests are rejected at the proxy layer before reaching the backend.

## What This Error Means

When Nginx processes a `proxy_pass` directive, it opens a TCP connection to the specified upstream address and port. If the connection fails, Nginx returns 502 Bad Gateway and logs errors like `connect() failed (111: Connection refused)` or `no live upstreams`. This means the backend is either not running, listening on the wrong port, or blocked by a firewall.

## Common Causes

- Upstream server is not running or has crashed
- Wrong IP address or port in `proxy_pass`
- Firewall blocking connection from Nginx to upstream
- Upstream server backlog queue is full
- DNS resolution failure for upstream hostname
- Unix socket path does not exist

## How to Fix

### Check Nginx Error Logs

```bash
sudo tail -f /var/log/nginx/error.log | grep "connect\|proxy_pass"
```

### Verify Upstream Server is Running

```bash
curl -v http://127.0.0.1:8080
telnet 127.0.0.1 8080
ss -tlnp | grep 8080
```

### Check proxy_pass Configuration

```nginx
location /api/ {
    proxy_pass http://127.0.0.1:8080;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
}
```

### Fix Upstream Definition

```nginx
upstream backend {
    server 127.0.0.1:8080 max_fails=3 fail_timeout=30s;
    server 127.0.0.1:8081 backup;
    keepalive 32;
}
```

### Test Connection from Nginx Server

```bash
# Test as the www-data user
sudo -u www-data curl http://127.0.0.1:8080
```

### Check Firewall Rules

```bash
sudo iptables -L -n | grep 8080
sudo ufw status
```

### Fix Unix Socket Proxy

```nginx
location /api/ {
    proxy_pass http://unix:/run/gunicorn.sock;
}
```

## Related Errors

- [Nginx 502 Bad Gateway]({{< relref "/tools/nginx/nginx-502-error-v2" >}}) — upstream connection closed
- [Nginx Upstream Error]({{< relref "/tools/nginx/nginx-upstream-error-v2" >}}) — connection refused
- [Nginx Worker Error]({{< relref "/tools/nginx/nginx-worker-error-v2" >}}) — worker process exited
