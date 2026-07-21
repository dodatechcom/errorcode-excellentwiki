---
title: "Nginx Proxy Buffer Size Error"
description: "Nginx returns 502 Bad Gateway due to upstream response headers too large"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Nginx Proxy Buffer Size Error

Nginx returns 502 Bad Gateway due to upstream response headers too large

## Common Causes

- proxy_buffer_size too small for response headers
- Upstream returns unusually large headers
- Cookies or authentication tokens in headers exceeding buffer
- Multiple proxy_pass headers stacking up

## How to Fix

1. Increase buffer size: `proxy_buffer_size 128k;`
2. Adjust buffer counts: `proxy_buffers 4 256k;`
3. Check upstream headers: `curl -I http://upstream`
4. Review Nginx error log for 'upstream sent too big header'

## Examples

```nginx
# Increase proxy buffer sizes
location / {
    proxy_pass http://backend;
    proxy_buffer_size 128k;
    proxy_buffers 4 256k;
    proxy_busy_buffers_size 512k;
}
```
