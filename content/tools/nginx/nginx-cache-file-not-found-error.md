---
title: "[Solution] Nginx Cache File Not Found Error"
description: "A cached response file is missing or was deleted from the cache directory."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

A cached response file is missing or was deleted from the cache directory.

## Common Causes

- **Cache purged externally**
- **Disk error** corrupted cache
- **Cache cleared** by admin
- **Temporary files** not committed

## How to Fix

1. Rebuild cache by clearing and re-fetching
2. Check disk: `df -h /var/cache/nginx/`
3. Verify cache_path exists
4. Re-enable caching

## Examples

**Clear and rebuild:**
```bash
rm -rf /var/cache/nginx/my_cache/*
sudo nginx -s reload
```
**Verify:**
```bash
ls -la /var/cache/nginx/my_cache/
```