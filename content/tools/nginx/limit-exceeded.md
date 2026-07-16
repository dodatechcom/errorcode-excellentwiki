---
title: "[Solution] Nginx Limiting Requests (429 Too Many Requests)"
description: "Fix Nginx rate limiting errors. Resolve 429 Too Many Requests and limit_req burst issues."
tools: ["nginx"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["rate-limit", "429", "limit-req", "throttle", "nginx"]
weight: 5
---

# Nginx Limiting Requests (429 Too Many Requests)

Nginx returns a 429 status when a client exceeds the configured request rate limit. The `limit_req` module tracks incoming requests and rejects those that exceed the defined threshold.

## Common Causes

- The `limit_req` zone is too restrictive for normal traffic
- A client or bot is sending too many requests in a short period
- Burst limit is not configured or is too low
- Legitimate traffic spikes are hitting the rate limit

## How to Fix

### Review Current Rate Limit Configuration

```nginx
http {
    limit_req_zone $binary_remote_addr zone=apilimit:10m rate=10r/s;
}
```

### Increase Rate or Add Burst Tolerance

```nginx
location /api/ {
    limit_req zone=apilimit burst=20 nodelay;
}
```

### Whitelist Trusted IPs

```nginx
geo $limit {
    default 1;
    10.0.0.0/8 0;       # internal network — no limit
    192.168.1.0/24 0;    # trusted range
}

map $limit $limit_key {
    0 "";
    1 $binary_remote_addr;
}

http {
    limit_req_zone $limit_key zone=apilimit:10m rate=10r/s;
}
```

### Adjust Response for Limited Requests

```nginx
limit_req_status 429;

error_page 429 = @rate_limited;
location @rate_limited {
    return 429 '{"error": "rate limit exceeded"}';
}
```

## Examples

```nginx
# Client exceeding 10 requests per second
# 429 Too Many Requests
# Fix: increase burst or adjust rate for the zone

# Legitimate batch operation hitting limit
# 429 Too Many Requests
# Fix: whitelist the IP or increase burst for that location
```

## Related Errors

- [403 Forbidden]({{< relref "/tools/nginx/403-forbidden2" >}}) — access denied by configuration
- [Connection Refused]({{< relref "/tools/nginx/connection-refused6" >}}) — TCP connection rejected
