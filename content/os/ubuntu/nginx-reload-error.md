---
title: "[Solution] Ubuntu Server: nginx-reload-error"
description: "Fix Ubuntu nginx-reload-error. nginx reload fails and configuration is not applied."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Nginx Reload Error

nginx reload fails when applying new configuration.

## Common Causes
- Syntax error in new configuration
- Missing required module
- Bind address not available
- Certificate file not found

## How to Fix
1. Test configuration
```bash
sudo nginx -t
```
2. Check for syntax errors
```bash
sudo nginx -T 2>&1 | grep -i error
```
3. Fix and reload
```bash
sudo nano /etc/nginx/sites-available/default
sudo nginx -t
sudo systemctl reload nginx
```

## Examples
```bash
$ sudo nginx -t
nginx: [emerg] bind() to 0.0.0.0:80 failed (98: Address already in use)
nginx: configuration file /etc/nginx/nginx.conf test failed
```
