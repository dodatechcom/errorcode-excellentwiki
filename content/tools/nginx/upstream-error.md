---
title: "[Solution] Nginx 502 Bad Gateway — upstream timed out"
description: "Fix Nginx 502 Bad Gateway upstream timed out error. Diagnose upstream connection and timeout issues."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Nginx 502 Bad Gateway — upstream timed out

A 502 Bad Gateway with "upstream timed out" means Nginx received no valid response from the upstream server within the configured timeout. This indicates the backend service is either down, overloaded, or too slow.

## Common Causes

- Upstream server is not running or crashed
- Upstream server is overloaded and cannot respond in time
- Network connectivity issue between Nginx and upstream
- Nginx proxy timeout is too low for the workload

## How to Fix

### Check Upstream Server Status

```bash
sudo systemctl status <upstream-service>
curl http://localhost:<upstream-port>
```

### Increase Proxy Timeout

```nginx
proxy_connect_timeout 60s;
proxy_read_timeout 60s;
proxy_send_timeout 60s;
```

### Check Nginx Error Logs

```bash
sudo tail -f /var/log/nginx/error.log
```

### Verify Upstream Configuration

```nginx
upstream backend {
    server 127.0.0.1:8080;
}
```

### Restart Services

```bash
sudo systemctl restart nginx
sudo systemctl restart <upstream-service>
```

## Examples

```bash
# Example 1: Backend service down
sudo systemctl status my-api
# my-api.service: inactive (dead)
# Fix: sudo systemctl start my-api

# Example 2: Timeout too short
# Nginx error log shows: upstream timed out (110: Connection timed out)
# Fix: increase proxy_read_timeout in nginx.conf
```

## Related Errors

- [SSL Certificate Problem]({{< relref "/tools/nginx/ssl-certificate" >}}) — SSL/TLS issues with upstream
- [Port In Use]({{< relref "/tools/docker/port-in-use" >}}) — port binding conflict
