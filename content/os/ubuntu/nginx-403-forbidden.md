---
title: "[Solution] Ubuntu Server: nginx-403-forbidden"
description: "Fix Ubuntu nginx-403-forbidden. nginx returns 403 Forbidden for web requests."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Nginx 403 Forbidden

nginx returns 403 Forbidden when serving files.

## Common Causes
- File permissions do not allow nginx user
- index.html or index.php missing
- autoindex off and no index file
- Directory listing not enabled
- SELinux or AppArmor blocking access

## How to Fix
1. Check nginx user
```bash
grep -E "^user" /etc/nginx/nginx.conf
```
2. Fix file permissions
```bash
sudo chown -R www-data:www-data /var/www/html
sudo chmod -R 755 /var/www/html
```
3. Check directory listing
```bash
sudo nginx -T | grep autoindex
```

## Examples
```bash
$ curl -I http://localhost/
HTTP/1.1 403 Forbidden

$ ls -la /var/www/html/
drwxr-x--- 2 root root 4096 Mar 15 10:00 index.html
# nginx user cannot read!

$ sudo chmod 755 /var/www/html
$ curl -I http://localhost/
HTTP/1.1 200 OK
```
