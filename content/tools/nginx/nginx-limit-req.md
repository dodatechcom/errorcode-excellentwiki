---
title: "[Solution] Nginx limit_req — limiting requests"
description: "Fix Nginx limit_req rate limiting errors. Resolve request rate limiting issues."
tools: ["nginx"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["limit_req", "rate-limit", "throttle", "503", "nginx"]
weight: 5
---

A limit_req error means Nginx is rejecting requests because they exceed the configured rate limit. Clients receive 503 Service Temporarily Unavailable responses.

## Common Causes

- Request rate exceeds the configured limit
- Burst traffic exceeds burst allowance
- rate and burst values too restrictive
- All workers are busy processing delayed requests
- Legitimate traffic patterns exceed limits

## How to Fix

### Check Current Rate Limit Config

```bash
nginx -T | grep limit_req
```

### Increase Rate Limit

```nginx
limit_req_zone $binary_remote_addr zone=api:10m rate=10r/s;

location /api/ {
    limit_req zone=api burst=20 nodelay;
}
```

### Add Burst Allowance

```nginx
location /api/ {
    limit_req zone=api burst=50 nodelay;
}
```

### Use Different Zone for Different Paths

```nginx
limit_req_zone $binary_remote_addr zone=login:10m rate=1r/s;
limit_req_zone $binary_remote_addr zone=api:10m rate=10r/s;

location /login {
    limit_req zone=login burst=5;
}
```

### Configure Limit Exceeded Response

```nginx
limit_req_status 429;
```

## Examples

```nginx
# Rate limit hit
# limiting requests, excess: 15.000 by zone "api"
# Fix: increase rate or burst

# Different limits per path
limit_req zone=login burst=3;
limit_req zone=api burst=20 nodelay;
```

## Related Errors

- [Nginx 403 Forbidden]({{< relref "/tools/nginx/nginx-403-error" >}}) — permission denied
- [Nginx Worker Error]({{< relref "/tools/nginx/nginx-worker-error" >}}) — worker process error
