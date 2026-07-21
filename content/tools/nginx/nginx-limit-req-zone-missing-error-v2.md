---
title: "[Solution] Nginx Limit Req Zone Missing Error"
description: "Nginx rate limiting fails because the limit_req_zone directive is not defined for the zone used in limit_req."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

# Nginx Limit Req Zone Missing Error

Nginx rate limiting requires a `limit_req_zone` definition before `limit_req` can be used. This error occurs when the zone is referenced but not defined.

## Common Causes

- The `limit_req_zone` directive is missing from the http block
- The zone name in `limit_req` does not match the defined zone
- The zone is defined in a different server block that is not loaded
- The `limit_req_zone` has a syntax error preventing it from loading

## How to Fix

1. Define the rate limit zone in the http block:

```nginx
http {
    limit_req_zone $binary_remote_addr zone=api:10m rate=10r/s;
}
```

2. Reference the zone correctly in the location block:

```nginx
server {
    listen 80;

    location /api/ {
        limit_req zone=api burst=20 nodelay;
        proxy_pass http://backend;
    }
}
```

3. Check zone syntax:

```nginx
# Syntax: limit_req_zone key zone=name:size rate=rate
limit_req_zone $binary_remote_addr zone=myzone:10m rate=5r/s;
```

4. Test configuration before applying:

```bash
nginx -t
```

## Examples

```nginx
# Error configuration -- zone not defined
server {
    location /api/ {
        limit_req zone=api burst=20;  # 'api' zone not defined
    }
}
```

```nginx
# Fixed configuration
http {
    limit_req_zone $binary_remote_addr zone=api:10m rate=10r/s;
    limit_req_zone $binary_remote_addr zone=web:10m rate=5r/s;

    server {
        location /api/ {
            limit_req zone=api burst=20 nodelay;
        }
        location / {
            limit_req zone=web burst=10;
        }
    }
}
```

## Related Errors

- [Limit Req Error]({{< relref "/tools/nginx/nginx-limit-req-error" >}}) -- rate limiting errors
- [Limit Req Zone Missing]({{< relref "/tools/nginx/nginx-limit-req-zone-missing-error" >}}) -- zone definition issues
