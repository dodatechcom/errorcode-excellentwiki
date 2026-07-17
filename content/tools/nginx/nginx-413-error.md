---
title: "[Solution] Nginx 413 Request Entity Too Large"
description: "Fix Nginx 413 Request Entity Too Large error. Resolve request size limit issues."
tools: ["nginx"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

A 413 Request Entity Too Large means the client sent a request body that exceeds Nginx's configured maximum size. This commonly happens with file uploads.

## Common Causes

- Request body exceeds `client_max_body_size` directive
- Default limit (1MB) is too small for the use case
- Uploading large files without adjusting limits
- Multiple directives limiting request size

## How to Fix

### Increase Client Max Body Size

```nginx
client_max_body_size 100M;
```

### Set Per-Location Limit

```nginx
location /upload {
    client_max_body_size 200M;
}
```

### Check Current Limit

```bash
nginx -T | grep client_max_body_size
```

### Apply to Server Block

```nginx
server {
    client_max_body_size 50M;
    # ... other config
}
```

### Test with curl

```bash
curl -X POST -F "file=@large-file.zip" http://example.com/upload
```

## Examples

```nginx
# Default 1MB limit
# 413 Request Entity Too Large
# Fix: client_max_body_size 100M;

# Per-location limit
location /api/upload {
    client_max_body_size 500M;
}
```

## Related Errors

- [Nginx 403 Forbidden]({{< relref "/tools/nginx/nginx-403-error" >}}) — permission denied
- [Nginx Limit Req]({{< relref "/tools/nginx/nginx-limit-req" >}}) — rate limiting
