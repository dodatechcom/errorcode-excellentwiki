---
title: "[Solution] Nginx Cache Zone Not Defined Error"
description: "The proxy_cache directive references a zone not defined with proxy_cache_path."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The proxy_cache directive references a zone not defined with proxy_cache_path.

## Common Causes

- **proxy_cache without proxy_cache_path**
- **Zone name mismatch**
- **proxy_cache_path in wrong context**

## How to Fix

1. Define zone: `proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=my_cache:10m;`
2. Check name matches
3. Ensure at http level

## Examples

**Config:**
```nginx
http {
    proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=my_cache:10m;
    server {
        location / {
            proxy_cache my_cache;
            proxy_cache_valid 200 10m;
            proxy_pass http://backend;
        }
    }
}
```