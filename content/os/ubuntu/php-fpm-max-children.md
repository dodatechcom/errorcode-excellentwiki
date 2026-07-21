---
title: "PHP-FPM Max Children Reached"
description: "PHP-FPM exhausted all worker processes and cannot serve new requests"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# PHP-FPM Max Children Reached

PHP-FPM exhausted all worker processes and cannot serve new requests

## Common Causes

- pm.max_children too low for traffic volume
- Scripts taking too long to execute holding workers
- Database queries blocking PHP workers
- Memory limit per child too high preventing spawn

## How to Fix

1. Increase pm.max_children in www.conf
2. Check current usage: `ps aux | grep php-fpm | wc -l`
3. Optimize slow scripts or increase request timeout
4. Monitor with `php-fpm-status` page

## Examples

```bash
# Check current FPM process count
ps aux | grep 'php-fpm: pool' | wc -l

# Check FPM status page (if configured)
curl http://localhost/fpm-status
```
