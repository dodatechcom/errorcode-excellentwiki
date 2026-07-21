---
title: "[Solution] Ubuntu Server: nginx-404-not-found"
description: "Fix Ubuntu nginx-404-not-found. nginx returns 404 for all or specific requests."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Nginx 404 Not Found

nginx returns 404 for requests that should return content.

## Common Causes
- Root directory incorrect in config
- Alias or location block misconfigured
- Files not in expected directory
- Symlinks not followed

## How to Fix
1. Check root directory
```bash
sudo nginx -T | grep root
ls -la /var/www/html/
```
2. Test configuration
```bash
sudo nginx -t
```
3. Check symlink following
```bash
# In server block:
# location / {
#     try_files $uri $uri/ =404;
# }
```

## Examples
```bash
$ curl http://localhost/index.html
404 Not Found

$ ls -la /var/www/html/
total 0

$ sudo cp /tmp/index.html /var/www/html/
$ curl http://localhost/index.html
# Returns 200 OK
```
