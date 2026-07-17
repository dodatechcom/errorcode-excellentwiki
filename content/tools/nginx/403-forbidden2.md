---
title: "[Solution] Nginx 403 Forbidden"
description: "Fix Nginx 403 Forbidden error. Resolve permission denied and directory indexing issues."
tools: ["nginx"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Nginx 403 Forbidden

A 403 Forbidden error means Nginx received the request but refused to serve the resource. This is a permission or configuration issue, not a missing file.

## Common Causes

- The Nginx worker process lacks read permission on the file or directory
- Directory indexing is disabled and no index file exists
- The `root` or `alias` directive points to the wrong path
- An `.htaccess` or access rule is blocking the request

## How to Fix

### Check File and Directory Permissions

```bash
ls -la /var/www/html/
# Ensure files are readable by the Nginx user
sudo chmod -R 755 /var/www/html
sudo chown -R www-data:www-data /var/www/html
```

### Enable Directory Indexing or Add an Index File

```nginx
location / {
    index index.html;
    autoindex on;  # or off, depending on your needs
}
```

### Verify the root Directive

```nginx
server {
    root /var/www/html;
    # Ensure this path is correct and accessible
}
```

### Check for Forbidden Index Files

```bash
# Ensure index.html or index.htm exists
ls /var/www/html/index.html
```

## Examples

```nginx
# Missing index file and autoindex disabled
location / {
    # 403 Forbidden — no index.html, autoindex off
    # Fix: add index.html or enable autoindex on

# Wrong permissions on web root
# 403 Forbidden
# Fix: chmod -R 755 /var/www/html && chown -R www-data:www-data /var/www/html
```

## Related Errors

- [404 Not Found]({{< relref "/tools/nginx/404-not-found3" >}}) — file does not exist
- [SSL Certificate Problem]({{< relref "/tools/nginx/ssl-certificate" >}}) — SSL handshake failure
