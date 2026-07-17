---
title: "[Solution] Nginx upstream — connection refused"
description: "Fix Nginx upstream connection refused. Resolve upstream server connectivity issues."
tools: ["nginx"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["nginx", "upstream", "connection-refused", "backend", "connectivity"]
weight: 5
---

An upstream connection refused error means the backend server actively rejected the TCP connection from Nginx. The backend is either not listening on the expected port or explicitly refusing connections.

## What This Error Means

When Nginx attempts to connect to an upstream server, the OS returns `ECONNREFUSED` (error code 111) if no process is listening on the target port, or if a firewall/rule actively rejects the connection. Unlike a timeout, a refusal is immediate — the backend either doesn't exist at that address or is explicitly rejecting the connection. The error log shows `connect() failed (111: Connection refused)`.

## Common Causes

- Upstream service is not started or crashed
- Service listening on a different port than Nginx expects
- Service bound to a different network interface (127.0.0.1 vs 0.0.0.0)
- Firewall rules dropping connections on the upstream port
- Service backlog queue is full and refusing new connections
- Wrong upstream address after container/IP change

## How to Fix

### Check What's Listening on the Port

```bash
sudo ss -tlnp | grep :8080
sudo netstat -tlnp | grep :8080
```

### Start the Upstream Service

```bash
sudo systemctl start gunicorn
sudo systemctl start php8.2-fpm
docker start my-backend-container
```

### Verify Service Binding Address

```bash
# Check if bound to all interfaces or just localhost
ss -tlnp | grep :8080
# 127.0.0.1:8080 = only local connections
# 0.0.0.0:8080 = all interfaces
```

### Test Connection Directly

```bash
curl -v http://127.0.0.1:8080/health
telnet 127.0.0.1 8080
```

### Check Nginx Upstream Config

```nginx
upstream backend {
    # Verify this matches the actual service address
    server 127.0.0.1:8080;
}
```

### Check Docker Network

```bash
docker network ls
docker inspect <container> | grep IPAddress
```

### Fix Firewall

```bash
# Allow Nginx to reach upstream
sudo iptables -A INPUT -p tcp --dport 8080 -s 127.0.0.1 -j ACCEPT
sudo ufw allow from 127.0.0.1 to any port 8080
```

### Check Service Logs

```bash
sudo journalctl -u gunicorn --lines=50
docker logs my-backend-container
```

## Related Errors

- [Nginx 502 Bad Gateway]({{< relref "/tools/nginx/nginx-502-error-v2" >}}) — upstream connection closed
- [Nginx Proxy Error]({{< relref "/tools/nginx/nginx-proxy-error-v2" >}}) — proxy_pass error
- [Nginx 504 Timeout]({{< relref "/tools/nginx/nginx-504-error-v2" >}}) — upstream timed out
