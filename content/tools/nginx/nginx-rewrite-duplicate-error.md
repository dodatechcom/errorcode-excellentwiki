---
title: "[Solution] Nginx Rewrite Duplicate Error"
description: "Multiple rewrite rules with identical patterns cause conflicts."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

Multiple rewrite rules with identical patterns cause conflicts.

## Common Causes

- **Copy-paste errors**
- **Include files** with same rewrites
- **Multiple rewrites** with identical regex

## How to Fix

1. Find: `grep -rn 'rewrite' /etc/nginx/conf.d/ | sort`
2. Remove or merge duplicates
3. Use break/last appropriately

## Examples

**Duplicate:**
```nginx
rewrite ^/old/(.*)$ /new/$1 permanent;
rewrite ^/old/(.*)$ /new/$1 permanent;
```
**Fixed:**
```nginx
rewrite ^/old/(.*)$ /new/$1 permanent;
```