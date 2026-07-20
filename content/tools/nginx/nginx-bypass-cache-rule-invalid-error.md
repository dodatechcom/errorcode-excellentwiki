---
title: "[Solution] Nginx Bypass Cache Rule Invalid Error"
description: "The proxy_cache_bypass or proxy_no_cache directive has invalid syntax or logic."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The proxy_cache_bypass or proxy_no_cache directive has invalid syntax or logic.

## Common Causes

- **Invalid variable** in bypass rule
- **Missing semicolon**
- **Conflicting bypass and no_cache**
- **Logic error** (always bypassing)

## How to Fix

1. Check syntax: `proxy_cache_bypass $http_pragma;`
2. Test: `curl -H 'Pragma: no-cache' http://example.com/`
3. Verify variables are set
4. Validate: `sudo nginx -t`

## Examples

**Bypass config:**
```nginx
location / {
    proxy_cache my_cache;
    proxy_cache_bypass $http_x_no_cache;
    proxy_no_cache $http_x_no_cache;
    proxy_pass http://backend;
}
```
**Test:**
```bash
# Bypass cache
curl -H 'X-No-Cache: 1' http://example.com/
# Normal cached response
curl http://example.com/
```