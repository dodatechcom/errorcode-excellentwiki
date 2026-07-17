---
title: "[Solution] Nginx 403 Forbidden"
description: "Fix Nginx 403 Forbidden error. Diagnose permission and access issues."
tools: ["nginx"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

A 403 Forbidden means Nginx understood the request but refused to authorize it. This is typically a file permission or configuration issue.

## Common Causes

- Nginx worker process does not have read permissions on the file
- Directory listing is disabled and no index file exists
- `.htaccess` or `allow/deny` rules blocking access
- SELinux or AppArmor blocking Nginx access
- Root directive points to wrong directory

## How to Fix

### Check File Permissions

```bash
ls -la /var/www/html/
sudo chown -R www-data:www-data /var/www/html
sudo chmod -R 755 /var/www/html
```

### Verify Root Directive

```nginx
server {
    root /var/www/html;
    index index.html index.htm;
}
```

### Enable Directory Index

```nginx
location / {
    autoindex on;
}
```

### Check SELinux

```bash
sudo setsebool -P httpd_read_user_content 1
sudo restorecon -R /var/www/html
```

### Check Error Log

```bash
sudo tail -f /var/log/nginx/error.log
```

## Examples

```nginx
# No index file and autoindex off
# 403 Forbidden
# Fix: add index.html or enable autoindex

# Wrong permissions
# 403 Forbidden
# nginx error log: (13: Permission denied)
# Fix: sudo chmod 755 /var/www/html
```

## Related Errors

- [Nginx 413 Error]({{< relref "/tools/nginx/nginx-413-error" >}}) — request entity too large
- [Nginx 499 Error]({{< relref "/tools/nginx/nginx-499-error" >}}) — client closed request
