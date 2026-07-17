---
title: "[Solution] Nginx limiting requests — 503 Service Temporarily Unavailable"
description: "Fix Nginx limiting requests 503. Resolve rate limiting and burst configuration."
tools: ["nginx"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

An Nginx 503 with "limiting requests" means the `limit_req` module has rejected the request because it exceeds the configured rate limit. Nginx returns 503 to clients sending requests faster than the allowed rate.

## What This Error Means

Nginx's `limit_req` module enforces request rate limits using a token bucket algorithm. When a client exceeds the allowed requests per second (plus any configured burst), excess requests are rejected with 503 (or optionally 429 or 502). The error log shows `limiting requests, excess: ... by zone`. This is an intentional rate limiting mechanism, not a server failure.

## Common Causes

- `limit_req_zone` rate set too low for legitimate traffic
- `burst` parameter too small for expected traffic spikes
- No `delay` parameter allowing graceful burst handling
- Single IP generating too many concurrent requests
- Bot or crawler hitting endpoints repeatedly
- Missing `nodelay` causing queuing and 503s

## How to Fix

### Check Nginx Rate Limit Configuration

```bash
nginx -T | grep -A 3 "limit_req"
```

### Configure Rate Limiting with Burst

```nginx
http {
    limit_req_zone $binary_remote_addr zone=api:10m rate=10r/s;
}

server {
    location /api/ {
        limit_req zone=api burst=20 nodelay;
        proxy_pass http://backend;
    }
}
```

### Increase Rate Limit

```nginx
# Allow 100 requests per second per IP
limit_req_zone $binary_remote_addr zone=api:10m rate=100r/s;

location /api/ {
    limit_req zone=api burst=50 nodelay;
    proxy_pass http://backend;
}
```

### Add Burst with Delay

```nginx
# Allow burst of 30 requests, delay after 10
location /api/ {
    limit_req zone=api burst=30 delay=10;
    proxy_pass http://backend;
}
```

### Whitelist Trusted IPs

```nginx
geo $limit {
    default 1;
    10.0.0.0/8 0;
    192.168.0.0/16 0;
}

map $limit $limit_key {
    0 "";
    1 $binary_remote_addr;
}

http {
    limit_req_zone $limit_key zone=api:10m rate=10r/s;
}
```

### Monitor Rate Limiting

```bash
# Watch for 503 responses
sudo tail -f /var/log/nginx/access.log | grep " 503 "
# Check limit_req log entries
sudo tail -f /var/log/nginx/error.log | grep "limiting"
```

### Use Separate Zones for Different Paths

```nginx
limit_req_zone $binary_remote_addr zone=login:10m rate=5r/s;
limit_req_zone $binary_remote_addr zone=api:10m rate=50r/s;

location /login {
    limit_req zone=login burst=3 nodelay;
    proxy_pass http://backend;
}

location /api/ {
    limit_req zone=api burst=20 nodelay;
    proxy_pass http://backend;
}
```

## Related Errors

- [Nginx 502 Bad Gateway]({{< relref "/tools/nginx/nginx-502-error-v2" >}}) — upstream connection closed
- [Nginx 504 Timeout]({{< relref "/tools/nginx/nginx-504-error-v2" >}}) — upstream timed out
- [Nginx Worker Error]({{< relref "/tools/nginx/nginx-worker-error-v2" >}}) — worker process exited
