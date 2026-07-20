---
title: "[Solution] Apache mod_cache Error"
description: "The mod_cache module is misconfigured or has a storage error."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The mod_cache module is misconfigured or has a storage error.

## Common Causes

- CacheRoot directory does not exist or is not writable
- CacheDefaultExpire or CacheMaxExpire not set
- Conflicting cache storage modules

## How to Fix

- Create and set permissions on CacheRoot directory
- Set appropriate expiration times
- Choose one storage module (mod_cache_disk or mod_cache_socache)

## Examples

```
['CacheRoot /var/cache/apache2/\nCacheDefaultExpire 3600\nCacheEnable disk http/']
```
