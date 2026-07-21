---
title: "Nginx Large File Upload Error"
description: "File upload fails when file size exceeds Nginx configured limit"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Nginx Large File Upload Error

File upload fails when file size exceeds Nginx configured limit

## Common Causes

- client_max_body_size too small
- Upstream server rejects large files
- Temporary upload directory full
- Request timeout during large upload

## How to Fix

1. Increase limit: `client_max_body_size 100M;` in nginx.conf
2. Check temp directory: `df -h /var/lib/nginx/`
3. Increase timeout for uploads: `proxy_read_timeout 600s;`
4. Check upstream server upload limits

## Examples

```nginx
# Allow larger file uploads
server {
    client_max_body_size 200M;
    client_body_timeout 600s;
    location /upload {
        proxy_pass http://backend;
    }
}
```
