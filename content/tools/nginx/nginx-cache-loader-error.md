---
title: "[Solution] Nginx Cache Loader Error"
description: "The Nginx cache loader process failed to load cached files into memory."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The Nginx cache loader process failed to load cached files into memory.

## Common Causes

- **Cache directory permissions** wrong
- **Corrupted cache files**
- **Cache zone too small**
- **Loader process crashed**

## How to Fix

1. Check permissions: `ls -la /var/cache/nginx/`
2. Clear corrupted files
3. Increase zone: `keys_zone=my_cache:100m;`
4. Restart Nginx

## Examples

**Fix:**
```bash
sudo rm -rf /var/cache/nginx/my_cache/*
sudo nginx -s reload
```
**Increase zone:**
```nginx
proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=my_cache:100m max_size=10g;
```