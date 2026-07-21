---
title: "PHP Session Save Path Error"
description: "PHP cannot write session files to configured save path"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# PHP Session Save Path Error

PHP cannot write session files to configured save path

## Common Causes

- Session save path does not exist
- Directory permissions prevent PHP-FPM from writing
- Disk full in session save directory
- Session handler configured to use database but DB unavailable

## How to Fix

1. Check config: `php -i | grep session.save_path`
2. Create directory: `mkdir -p /var/lib/php/sessions`
3. Fix permissions: `chown www-data:www-data /var/lib/php/sessions`
4. Check disk: `df -h /var/lib/php/`

## Examples

```bash
# Check session save path
php -i | grep session.save_path

# Create and set permissions
sudo mkdir -p /var/lib/php/sessions
sudo chown www-data:www-data /var/lib/php/sessions
sudo chmod 733 /var/lib/php/sessions
```
