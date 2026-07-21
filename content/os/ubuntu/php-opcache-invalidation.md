---
title: "PHP OPcache Invalidation Error"
description: "OPcache serving stale content after code changes"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# PHP OPcache Invalidation Error

OPcache serving stale content after code changes

## Common Causes

- OPcache revalidate frequency too high
- file_cache not enabled for shared hosting
- CLI and web OPcache not synchronized
- opcache.validate_timestamps disabled

## How to Fix

1. Check opcache status: `php -r 'print_r(opcache_get_status());'`
2. Clear opcache: `sudo service php*-fpm restart`
3. Set revalidate: `opcache.revalidate_freq=0` in php.ini
4. Verify timestamps validation: `opcache.validate_timestamps=1`

## Examples

```php
// Check OPcache status via PHP
<?php
print_r(opcache_get_status());
?>
```
