---
title: "[Solution] Ubuntu Server: php-opcache-error"
description: "Fix Ubuntu php-opcache-error. PHP OPcache configuration causes issues."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# PHP OPcache Error

PHP OPcache encounters errors or causes unexpected behavior.

## Common Causes
- OPcache memory too low
- validate_timestamps causing stale cache
- OPcache restart not clearing properly
- JIT compilation errors

## How to Fix
1. Check OPcache status
```bash
php -r "print_r(opcache_get_status());"
```
2. Configure OPcache
```bash
sudo nano /etc/php/8.1/fpm/conf.d/10-opcache.ini
opcache.enable=1
opcache.memory_consumption=256
opcache.max_accelerated_files=10000
```
3. Restart PHP-FPM
```bash
sudo systemctl restart php8.1-fpm
```

## Examples
```bash
$ php -r "print_r(opcache_get_status());"
Array
(
    [opcache_enabled] => 1
)
```