---
title: "[Solution] Nginx 404 Not Found"
description: "Fix Nginx 404 Not Found error. Resolve missing files, incorrect root paths, and location block issues."
tools: ["nginx"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["404", "not-found", "missing-file", "root", "nginx"]
weight: 5
---

# Nginx 404 Not Found

A 404 Not Found error means the requested resource does not exist at the path Nginx is trying to serve. This differs from a 403 in that the file or location genuinely cannot be found.

## Common Causes

- The file does not exist at the specified `root` path
- The `root` or `alias` directive is misconfigured
- A `location` block does not match the URL as expected
- The file was deleted or moved

## How to Fix

### Verify the File Exists

```bash
ls -la /var/www/html/your-page.html
```

### Check the root Directive

```nginx
server {
    # If URL is /page.html, Nginx looks for /var/www/html/page.html
    root /var/www/html;
}
```

### Use alias for Path Rewriting

```nginx
location /static/ {
    alias /var/www/assets/;
    # Trailing slash matters for alias
}
```

### Add a Custom 404 Page

```nginx
error_page 404 /custom_404.html;
location = /custom_404.html {
    root /var/www/html;
    internal;
}
```

## Examples

```nginx
# File not found
# 404 Not Found
# nginx: [error] open() "/var/www/html/page.html" failed (2: No such file or directory)
# Fix: create the file or correct the root path

# Wrong alias trailing slash
location /static/ {
    alias /var/www/assets;
    # 404 for /static/style.css because alias is missing trailing slash
    # Fix: alias /var/www/assets/;
}
```

## Related Errors

- [403 Forbidden]({{< relref "/tools/nginx/403-forbidden2" >}}) — permission denied on existing file
- [502 Bad Gateway]({{< relref "/tools/nginx/502-bad-gateway" >}}) — upstream server issue
