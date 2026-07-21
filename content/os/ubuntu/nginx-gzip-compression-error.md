---
title: "Nginx Gzip Compression Error"
description: "Nginx gzip compression not working or causing errors"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Nginx Gzip Compression Error

Nginx gzip compression not working or causing errors

## Common Causes

- gzip on; directive missing from config
- gzip_types not including content types being served
- gzip_min_length set too high for small responses
- Proxy response already compressed upstream

## How to Fix

1. Enable gzip: `gzip on;` in http or server block
2. Add types: `gzip_types text/plain application/json;`
3. Adjust minimum: `gzip_min_length 256;`
4. Test: `curl -H 'Accept-Encoding: gzip' -I http://site/`

## Examples

```nginx
# Enable gzip compression
http {
    gzip on;
    gzip_types text/plain text/css application/json application/javascript;
    gzip_min_length 256;
    gzip_vary on;
}
```
