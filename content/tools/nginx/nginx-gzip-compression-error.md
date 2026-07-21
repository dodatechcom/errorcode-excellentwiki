---
title: "[Solution] Nginx Gzip Compression Error"
description: "Nginx gzip compression fails to compress responses because the configuration is misconfigured or the MIME type is not included."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

# Nginx Gzip Compression Error

Nginx gzip module compresses responses to reduce bandwidth. A gzip error occurs when responses are not compressed even though gzip is enabled, or the configuration causes unexpected behavior.

## Common Causes

- The `gzip` directive is set to `off` or not enabled
- The response MIME type is not in the `gzip_types` list
- A proxy adds `Content-Encoding: gzip` to an already compressed response
- The `gzip_min_length` is set higher than the response size

## How to Fix

1. Enable gzip and configure the types:

```nginx
http {
    gzip on;
    gzip_vary on;
    gzip_proxied any;
    gzip_comp_level 6;
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;
}
```

2. Lower the minimum length for compression:

```nginx
http {
    gzip_min_length 256;
}
```

3. Enable gzip for proxied responses:

```nginx
http {
    gzip_proxied any;
}
```

4. Check if content is already compressed:

```bash
curl -I -H "Accept-Encoding: gzip" http://localhost/
# Look for Content-Encoding: gzip in response headers
```

## Examples

```nginx
# Complete gzip configuration
http {
    gzip on;
    gzip_vary on;
    gzip_proxied any;
    gzip_comp_level 6;
    gzip_min_length 1000;
    gzip_types
        text/plain
        text/css
        text/xml
        text/javascript
        application/json
        application/javascript
        application/xml
        application/rss+xml
        image/svg+xml;
}
```

```bash
# Verify gzip is working
curl -s -I -H "Accept-Encoding: gzip" http://example.com/ | grep -i "content-encoding"
```

## Related Errors

- [Gzip Error]({{< relref "/tools/nginx/nginx-gzip-error" >}}) -- gzip configuration issues
- [Unsupported Media Type]({{< relref "/tools/nginx/nginx-unsupported-media-type-error" >}}) -- MIME type issues
