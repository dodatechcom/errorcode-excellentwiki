---
title: "[Solution] Nginx Limit Req Zone Missing Error"
description: "The limit_req directive references a zone not defined with limit_req_zone."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The limit_req directive references a zone not defined with limit_req_zone.

## Common Causes

- **limit_req used without** limit_req_zone
- **Zone name mismatch**
- **limit_req_zone in wrong context** (must be http level)

## How to Fix

1. Define zone first: `limit_req_zone $binary_remote_addr zone=api_limit:10m rate=10r/s;`
2. Check name matches exactly
3. Ensure at http level

## Examples

**Complete:**
```nginx
http {
    limit_req_zone $binary_remote_addr zone=login:10m rate=1r/s;
    limit_req_zone $binary_remote_addr zone=api:10m rate=100r/s;
    server {
        location /login { limit_req zone=login burst=3 nodelay; proxy_pass http://backend; }
        location /api/ { limit_req zone=api burst=50 nodelay; proxy_pass http://backend; }
    }
}
```