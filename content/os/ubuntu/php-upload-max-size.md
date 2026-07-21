---
title: "PHP Upload Max Filesize Error"
description: "File upload exceeds PHP configured maximum upload size"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# PHP Upload Max Filesize Error

File upload exceeds PHP configured maximum upload size

## Common Causes

- upload_max_filesize too small in php.ini
- post_max_size smaller than upload_max_filesize
- max_file_uploads limit reached
- Temporary upload directory full

## How to Fix

1. Check settings: `php -i | grep upload_max_filesize`
2. Edit php.ini: `upload_max_filesize = 64M`
3. Also set: `post_max_size = 128M`
4. Restart PHP-FPM: `sudo systemctl restart php*-fpm`

## Examples

```bash
# Check current PHP upload settings
php -i | grep -E 'upload_max_filesize|post_max_size'

# Edit php.ini
sudo nano /etc/php/8.1/fpm/php.ini

# Restart PHP-FPM
sudo systemctl restart php8.1-fpm
```
