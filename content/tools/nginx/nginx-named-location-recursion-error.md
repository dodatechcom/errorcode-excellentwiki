---
title: "[Solution] Nginx Named Location Recursion Error"
description: "A named location references itself or creates an infinite recursion chain."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

A named location references itself or creates an infinite recursion chain.

## Common Causes

- **error_page** pointing to location triggering same error
- **try_files** referencing looping location
- **Recursive @location chains**

## How to Fix

1. Check error_page directives
2. Ensure named locations have terminal actions
3. Trace: `grep -rn '@' /etc/nginx/conf.d/ | grep -E 'error_page|try_files'`

## Examples

**Loop:**
```nginx
error_page 404 @fallback;
location @fallback { try_files /index.html @fallback; }  # loops
```
**Fixed:**
```nginx
error_page 404 @fallback;
location @fallback { root /var/www; try_files /index.html =404; }
```