---
title: "PHP-FPM Slow Request Logging"
description: "PHP-FPM slow request log shows scripts exceeding timeout"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# PHP-FPM Slow Request Logging

PHP-FPM slow request log shows scripts exceeding timeout

## Common Causes

- request_slowlog_timeout too low
- Database queries causing slow execution
- External API calls blocking PHP execution
- OPcache disabled causing repeated script compilation

## How to Fix

1. Check slow log: `tail -f /var/log/php*/fpm/www-slow.log`
2. Increase timeout: `request_slowlog_timeout = 10s`
3. Enable OPcache: `opcache.enable=1` in php.ini
4. Optimize slow queries identified in log

## Examples

```bash
# Check PHP-FPM slow log
sudo tail -50 /var/log/php8.1-fpm/www-slow.log

# Enable slow request logging
echo 'request_slowlog_timeout = 5s' | sudo tee -a /etc/php/8.1/fpm/pool.d/www.conf
echo 'slowlog = /var/log/php8.1-fpm/www-slow.log' | sudo tee -a /etc/php/8.1/fpm/pool.d/www.conf
```
