---
title: "PHP-FPM Connection Refused Error"
description: "Web server cannot connect to PHP-FPM backend"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# PHP-FPM Connection Refused Error

Web server cannot connect to PHP-FPM backend

## Common Causes

- PHP-FPM not running or crashed
- Socket/port mismatch between web server and FPM
- FPM pool not configured for correct listen address
- Permission denied on socket file

## How to Fix

1. Check FPM status: `systemctl status php*-fpm`
2. Verify listen config: `grep listen /etc/php/*/fpm/pool.d/www.conf`
3. Check socket permissions: `ls -la /run/php/`
4. Restart FPM: `sudo systemctl restart php*-fpm`

## Examples

```bash
# Check PHP-FPM status
systemctl status php8.1-fpm

# Check listen configuration
grep listen /etc/php/8.1/fpm/pool.d/www.conf

# Restart PHP-FPM
sudo systemctl restart php8.1-fpm
```
