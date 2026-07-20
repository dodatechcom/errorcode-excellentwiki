---
title: "[Solution] Nginx Cache Key Too Long Error"
description: "The computed cache key exceeds the maximum allowed length."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The computed cache key exceeds the maximum allowed length.

## Common Causes

- **Very long URL** with many parameters
- **Complex cache_key** configuration
- **Default key too long** for your hash table

## How to Fix

1. Simplify cache_key
2. Use hash of long keys: `set $cache_key $host$uri;`
3. Use a shorter key template

## Examples

**Simple key:**
```nginx
proxy_cache_key "$scheme$request_method$host$uri";
```
**Complex key:**
```nginx
set $cache_key "$scheme$request_method$host$uri$is_args$args";
proxy_cache_key $cache_key;
```