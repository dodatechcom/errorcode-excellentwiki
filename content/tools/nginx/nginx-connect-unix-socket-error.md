---
title: "[Solution] Nginx Connect to Unix Socket Failed Error"
description: "Nginx cannot connect to the upstream Unix socket."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

Nginx cannot connect to the upstream Unix socket.

## Common Causes

- **Socket file does not exist**
- **Backend not running**
- **Permission denied**
- **Socket path wrong**

## How to Fix

1. Check socket: `ls -la /run/php-fpm.sock`
2. Verify backend running: `systemctl status php-fpm`
3. Check permissions: `ls -la /run/php-fpm.sock`
4. Fix path in config

## Examples

**Check:**
```bash
ls -la /run/php-fpm.sock
# If missing, restart backend
sudo systemctl restart php-fpm
```
**Config:**
```nginx
location ~ \.php$ {
    fastcgi_pass unix:/run/php-fpm.sock;
    fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
}
```