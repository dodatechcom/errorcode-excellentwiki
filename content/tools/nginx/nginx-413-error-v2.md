---
title: "[Solution] Nginx 413 Request Entity Too Large — client body size exceeds"
description: "Fix Nginx 413 client body size exceeds limit. Resolve request size limit configuration."
tools: ["nginx"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

An Nginx 413 Request Entity Too Large means the client sent a request body larger than Nginx's `client_max_body_size` limit. The request is rejected before reaching the backend.

## What This Error Means

Nginx enforces a maximum size for client request bodies via the `client_max_body_size` directive (default 1MB). When a client uploads a file or sends a POST body exceeding this limit, Nginx immediately returns 413 without forwarding the request to the upstream. This is a protective measure to prevent large uploads from consuming backend resources or disk space.

## Common Causes

- `client_max_body_size` set too low for the application's needs
- File upload exceeds the configured limit
- Client sending unexpectedly large JSON or form data
- Missing or default Nginx configuration not accounting for uploads
- Proxy pass location does not override the server-level limit
- Backend allows larger uploads than Nginx permits

## How to Fix

### Increase Client Max Body Size

```nginx
# Set globally in http block
http {
    client_max_body_size 50m;
}

# Or per server
server {
    client_max_body_size 100m;
}

# Or per location
location /upload {
    client_max_body_size 200m;
    proxy_pass http://backend;
}
```

### Configure for File Uploads

```nginx
location /api/upload {
    client_max_body_size 500m;
    client_body_buffer_size 128k;
    proxy_pass http://backend;
}
```

### Set Multiple Size Limits by Path

```nginx
location /api/small {
    client_max_body_size 1m;
    proxy_pass http://backend;
}

location /api/upload {
    client_max_body_size 100m;
    proxy_pass http://backend;
}
```

### Check Current Configuration

```bash
nginx -T | grep client_max_body_size
```

### Test Upload Size

```bash
# Create a test file
dd if=/dev/zero of=test.bin bs=1M count=10
curl -X POST -F "file=@test.bin" http://example.com/upload
```

### Match Backend Limits

```python
# Flask example
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB
```

## Related Errors

- [Nginx 400 Error]({{< relref "/tools/nginx/nginx-400-error" >}}) — bad request large header
- [Nginx 403 Forbidden]({{< relref "/tools/nginx/nginx-403-error-v2" >}}) — directory forbidden
- [Nginx Limit Request]({{< relref "/tools/nginx/nginx-limit-req-v2" >}}) — rate limiting 503
