---
title: "[Solution] Nginx Cache Log Error"
description: "Nginx encountered an error writing to the cache-related log or the cache log path is invalid."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

Nginx encountered an error writing to the cache-related log or the cache log path is invalid.

## Common Causes

- **Cache directory does not exist**
- **Permission denied** on cache path
- **Disk full**
- **Invalid cache_path directive**

## How to Fix

1. Check: `ls -la /var/cache/nginx/`
2. Permissions: `sudo chown nginx:nginx /var/cache/nginx/`
3. Disk: `df -h /var/cache/`
4. Validate: `sudo nginx -t`

## Examples

**Fix:**
```bash
sudo mkdir -p /var/cache/nginx
sudo chown nginx:nginx /var/cache/nginx/
sudo nginx -t
```
**Config:**
```nginx
proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=my_cache:10m;
```