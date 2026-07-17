---
title: "[Solution] Nginx 502 Bad Gateway"
description: "Fix Nginx 502 Bad Gateway error. Diagnose why Nginx receives an invalid response from the upstream server."
tools: ["nginx"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

A 502 Bad Gateway means Nginx received an invalid or empty response from the upstream server it was proxying requests to. The backend process may have crashed, be misconfigured, or be unreachable.

## Common Causes

- The upstream server is down or not running
- The upstream process crashed or is unresponsive
- Incorrect proxy_pass directive pointing to a wrong address
- The upstream server closed the connection prematurely
- FastCGI process manager (PHP-FPM) is not running

## How to Fix

### Verify Upstream Server is Running

```bash
sudo systemctl status <upstream-service>
curl -v http://127.0.0.1:<upstream-port>
```

### Check Nginx Error Logs

```bash
sudo tail -f /var/log/nginx/error.log
```

### Ensure Correct proxy_pass Configuration

```nginx
location /api/ {
    proxy_pass http://127.0.0.1:8080;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
}
```

### Restart Both Services

```bash
sudo systemctl restart nginx
sudo systemctl restart <upstream-service>
```

### Increase Proxy Timeout

```nginx
proxy_connect_timeout 60s;
proxy_send_timeout 60s;
proxy_read_timeout 60s;
```

## Examples

```nginx
# Upstream server not running
# 502 Bad Gateway
# nginx error log: connect() failed (111: Connection refused)
# Fix: start the upstream service

# Wrong port in proxy_pass
proxy_pass http://127.0.0.1:3000;
# Upstream actually listens on 8080
# Fix: change to proxy_pass http://127.0.0.1:8080;
```

## Related Errors

- [Nginx 504 Timeout]({{< relref "/tools/nginx/nginx-504-error" >}}) — upstream server too slow
- [Nginx Proxy Error]({{< relref "/tools/nginx/nginx-proxy-error" >}}) — reverse proxy error
