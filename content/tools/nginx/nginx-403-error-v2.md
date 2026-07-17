---
title: "[Solution] Nginx 403 Forbidden — directory index forbidden"
description: "Fix Nginx 403 Forbidden directory index. Resolve directory listing and file permission issues."
tools: ["nginx"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["nginx", "403", "forbidden", "directory", "index", "permission"]
weight: 5
---

An Nginx 403 Forbidden with "directory index of ... is forbidden" means Nginx cannot serve the requested path because directory listing is disabled and no index file exists, or the file permissions prevent access.

## What This Error Means

When a client requests a directory path (e.g., `/images/`), Nginx looks for an index file (`index.html`, `index.htm`). If no index file exists and `autoindex` is off (the default), Nginx returns 403 Forbidden. This can also occur when the Nginx worker process lacks filesystem permissions to read the file, or when an explicit `deny` rule blocks access.

## Common Causes

- No `index.html` or `index.htm` in the requested directory
- `autoindex` directive is off (default) and no index file exists
- File permissions prevent Nginx worker (www-data) from reading the file
- `location` block has `deny all` directive
- `.htaccess` or equivalent access control denying the request
- SELinux or AppArmor blocking Nginx file access

## How to Fix

### Check Nginx Error Logs

```bash
sudo tail -f /var/log/nginx/error.log | grep "403"
```

### Fix File Permissions

```bash
sudo chown -R www-data:www-data /var/www/html
sudo chmod -R 755 /var/www/html
```

### Create an Index File

```bash
echo "<h1>Welcome</h1>" | sudo tee /var/www/html/index.html
```

### Enable Directory Listing (Development Only)

```nginx
location /images/ {
    autoindex on;
    autoindex_exact_size off;
}
```

### Check for Deny Directives

```nginx
location /admin/ {
    deny all;  # Intentional restriction
}
```

### Verify SELinux Status

```bash
sudo setsebool -P httpd_read_user_content 1
sudo restorecon -R /var/www/html
```

### Check Access Control

```nginx
# Remove unwanted deny rules
# location / {
#     deny all;  # Remove this if not intended
# }
```

### Debug with curl

```bash
curl -v http://example.com/directory/
# Look for HTTP 403 response
```

## Related Errors

- [Nginx 400 Error]({{< relref "/tools/nginx/nginx-400-error" >}}) — bad request large header
- [Nginx SSL Error]({{< relref "/tools/nginx/nginx-ssl-error-v2" >}}) — SSL handshake failed
- [Nginx Limit Request]({{< relref "/tools/nginx/nginx-limit-req-v2" >}}) — rate limiting 503
