---
title: "[Solution] Nginx Client Body Buffer Error"
description: "Nginx cannot buffer the client request body because the buffer is too small or the body exceeds the configured client_body_buffer_size."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

# Nginx Client Body Buffer Error

Nginx buffers client request bodies in memory. An error occurs when the request body exceeds `client_body_buffer_size`, forcing Nginx to write to temporary files or reject the request.

## Common Causes

- The `client_body_buffer_size` is too small for the application's expected uploads
- Large file uploads exceed the buffer limit
- Multiple large form submissions happen concurrently
- The `client_max_body_size` limit is also exceeded

## How to Fix

1. Increase the client body buffer size:

```nginx
http {
    client_body_buffer_size 128k;
    client_max_body_size 10M;
}
```

2. Configure buffers per location:

```nginx
location /upload {
    client_body_buffer_size 512k;
    client_max_body_size 50M;
    proxy_pass http://backend;
}
```

3. Set temporary file storage for large bodies:

```nginx
http {
    client_body_temp_path /var/cache/nginx/client_temp 1 2;
}
```

4. Check disk space for temporary files:

```bash
df -h /var/cache/nginx/
```

## Examples

```nginx
# File upload configuration
location /upload {
    client_body_buffer_size 1M;
    client_max_body_size 100M;
    proxy_pass http://backend;
    proxy_request_buffering off;  # stream large uploads
}
```

```nginx
# General configuration for large payloads
http {
    client_body_buffer_size 256k;
    client_max_body_size 50M;
    large_client_header_buffers 4 16k;
}
```

## Related Errors

- [Body Too Large]({{< relref "/tools/nginx/nginx-body-too-large-error" >}}) -- body size exceeded
- [Proxy Buffer Error]({{< relref "/tools/nginx/nginx-proxy-buffer-error" >}}) -- proxy buffer issues
- [Out of Memory]({{< relref "/tools/nginx/nginx-out-of-memory-error" >}}) -- memory exhaustion
