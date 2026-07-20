---
title: "[Solution] Nginx Cache Purger Error"
description: "The cache purger failed to remove cached files, possibly due to permission or path issues."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The cache purger failed to remove cached files, possibly due to permission or path issues.

## Common Causes

- **purger module not compiled in**
- **Wrong purge method** (proxy_cache_purge)
- **Cache path wrong**
- **Permission denied**

## How to Fix

1. Check module: `nginx -V 2>&1 | grep purge`
2. Verify cache_path
3. Use correct purge method

## Examples

**Purge config:**
```nginx
proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=my_cache:10m purge=on;

location ~ /purge(/.*) {
    allow 127.0.0.1;
    deny all;
    proxy_cache_purge my_cache $host$1$is_args$args;
}
```
**Manual purge:**
```bash
rm -rf /var/cache/nginx/my_cache/*
sudo nginx -s reload
```