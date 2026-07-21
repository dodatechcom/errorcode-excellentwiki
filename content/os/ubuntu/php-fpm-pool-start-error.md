---
title: "PHP-FPM Pool Failed to Start"
description: "PHP-FPM worker pool fails to initialize and accept connections"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# PHP-FPM Pool Failed to Start

PHP-FPM worker pool fails to initialize and accept connections

## Common Causes

- Socket file path does not exist or wrong permissions
- Listen address already in use
- Pool configuration syntax error in www.conf
- pm.max_children set too high exceeding system memory

## How to Fix

1. Check FPM config: `php-fpm -t`
2. Verify socket directory exists
3. Check pm.max_children vs available RAM
4. Review error log: `tail -f /var/log/php*/fpm/*.log`

## Examples

```bash
# Test FPM configuration
sudo php-fpm -t

# Check FPM error log
sudo tail -50 /var/log/php8.1-fpm.log

# Restart FPM
sudo systemctl restart php8.1-fpm
```
