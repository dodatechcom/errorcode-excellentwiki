---
title: "[Solution] Nginx No Cache Key Error"
description: "No cache key was configured or the computed key is empty, preventing cache storage."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

No cache key was configured or the computed key is empty, preventing cache storage.

## Common Causes

- **proxy_cache_key not set**
- **Key evaluates to empty string**
- **Variables in key are empty**
- **Default key not suitable**

## How to Fix

1. Set explicit key: `proxy_cache_key "$scheme$request_method$host$uri";`
2. Ensure variables have values
3. Debug: add key to header
4. Validate: `sudo nginx -t`

## Examples

**Config:**
```nginx
location / {
    proxy_cache my_cache;
    proxy_cache_key "$scheme$request_method$host$uri$is_args$args";
    proxy_pass http://backend;
}
```
**Debug key:**
```nginx
add_header X-Cache-Key $scheme$request_method$host$uri;
```
**Verify:**
```bash
curl -I http://example.com/
# Look for X-Cache-Key header
```