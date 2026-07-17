---
title: "[Solution] Nginx 499 Client Closed Request"
description: "Fix Nginx 499 Client Closed Request error. Diagnose client disconnect issues."
tools: ["nginx"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

A 499 Client Closed Request means the client closed the connection before Nginx finished sending the response. This is a non-standard status code defined by Nginx.

## Common Causes

- Client timeout was shorter than server processing time
- User navigated away before page loaded
- Load balancer health check timeout
- Client-side AJAX request abandoned
- Upstream server too slow causing client to give up

## How to Fix

### Increase Client Timeout

```nginx
proxy_read_timeout 300s;
proxy_send_timeout 300s;
```

### Check Upstream Response Time

```bash
sudo tail -f /var/log/nginx/access.log | grep 499
```

### Optimize Backend Performance

```bash
# Add caching
# Optimize database queries
# Use CDN for static assets
```

### Configure Client Timeout

```nginx
client_body_timeout 60s;
client_header_timeout 60s;
```

### Add Keepalive Connections

```nginx
upstream backend {
    server 127.0.0.1:8080;
    keepalive 32;
}
```

## Examples

```nginx
# Client times out waiting for slow backend
# 499 Client Closed Request
# Fix: optimize backend or increase timeout

# Health check timeout
# 499 on health check endpoint
# Fix: increase health check timeout on load balancer
```

## Related Errors

- [Nginx 504 Timeout]({{< relref "/tools/nginx/nginx-504-error" >}}) — gateway timeout
- [Nginx Upstream Error]({{< relref "/tools/nginx/nginx-upstream-error" >}}) — upstream timed out
