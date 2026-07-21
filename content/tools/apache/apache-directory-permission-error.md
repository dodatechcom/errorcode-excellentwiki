---
title: "[Solution] Apache Directory Permission Error"
description: "Fix Apache directory permission errors when the server cannot access document root or directories."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Apache returns 403 Forbidden or fails to serve content due to incorrect directory permissions.

## Common Causes

- DocumentRoot directory not readable by Apache user
- Parent directory lacks execute permission
- Incorrect file ownership
- SELinux or AppArmor denying access
- Options directive missing FollowSymLinks for symlinks

## How to Fix

- Ensure Apache user can read and traverse all parent directories
- Set correct ownership and permissions on document root
- Adjust SELinux context if applicable

## Examples

```bash
sudo chown -R www-data:www-data /var/www/html
sudo chmod -R 755 /var/www/html
# Ensure parent directories are traversable
sudo chmod 755 /var/www
sudo chmod 755 /var

# Check SELinux
sudo restorecon -Rv /var/www/html
sudo chcon -R -t httpd_sys_content_t /var/www/html
```
