---
title: "[Solution] Nginx Cache Lock Timeout Error"
description: "The cache lock timeout was reached while waiting to populate the cache."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The cache lock timeout was reached while waiting to populate the cache.

## Common Causes

- **Backend very slow** to respond
- **cache_lock_timeout too short**
- **Multiple requests** hitting same uncached URI
- **Backend returning errors**

## How to Fix

1. Increase timeout: `proxy_cache_lock_timeout 60s;`
2. Use lock_age: `proxy_cache_lock_age 5s;`
3. Disable lock: `proxy_cache_lock off;`
4. Fix slow backend

## Examples

**Config:**
```nginx
proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=my_cache:10m;

location / {
    proxy_cache my_cache;
    proxy_cache_lock on;
    proxy_cache_lock_timeout 60s;
    proxy_cache_lock_age 5s;
    proxy_pass http://backend;
}
```