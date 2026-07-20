---
title: "[Solution] Nginx Stale Cache Error"
description: "The cached response is stale and Nginx is configured to not serve stale content."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The cached response is stale and Nginx is configured to not serve stale content.

## Common Causes

- **Cache expired**
- **proxy_cache_use_stale not configured**
- **Backend unreachable** while cache expired
- **No fallback for stale**

## How to Fix

1. Enable stale: `proxy_cache_use_stale error timeout updating http_500 http_502 http_503;`
2. Use updating: `proxy_cache_background_update on;`
3. Set graceful period

## Examples

**Stale config:**
```nginx
location / {
    proxy_cache my_cache;
    proxy_cache_valid 200 5m;
    proxy_cache_use_stale error timeout updating http_500 http_502 http_503;
    proxy_cache_background_update on;
    proxy_cache_lock on;
    proxy_pass http://backend;
}
```