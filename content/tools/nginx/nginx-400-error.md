---
title: "[Solution] Nginx 400 Bad Request — large header"
description: "Fix Nginx 400 Bad Request large header. Resolve header size limit issues."
tools: ["nginx"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

An Nginx 400 Bad Request with "request header or cookie too large" means the client sent HTTP headers exceeding Nginx's buffer size. Nginx rejects the request at the header parsing stage.

## What This Error Means

Nginx allocates a fixed buffer for reading client request headers (`large_client_header_buffers`, default 4 buffers of 8KB each = 32KB total). When cookies, authorization tokens, or other headers exceed this limit, Nginx cannot parse the request and returns 400 Bad Request. The error log shows `client intended to send too large body` or `upstream prematurely closed connection` depending on which buffer is exceeded.

## Common Causes

- Excessive cookies from applications (session cookies accumulating)
- Large JWT tokens in Authorization header
- Custom headers with large base64-encoded values
- `proxy_buffer_size` too small for large upstream response headers
- Browser sending oversized cookie jars
- Malformed request line or headers

## How to Fix

### Check Nginx Error Logs

```bash
sudo tail -f /var/log/nginx/error.log | grep "400\|large header"
```

### Increase Large Client Header Buffers

```nginx
server {
    listen 443 ssl;
    large_client_header_buffers 4 32k;
}
```

### Set Appropriate Buffer Size

```nginx
# For normal applications
large_client_header_buffers 4 16k;

# For applications with large headers
large_client_header_buffers 4 64k;
```

### Check Cookie Size

```bash
# Monitor cookie sizes
curl -v http://example.com/ | grep -i "set-cookie"
```

### Clear Excessive Cookies

```javascript
// Reduce cookie size in application
// Remove unnecessary data from cookies
document.cookie = "session=abc123; path=/; max-age=3600";
```

### Increase Proxy Buffer Size

```nginx
location / {
    proxy_pass http://backend;
    proxy_buffer_size 16k;
    proxy_buffers 4 32k;
    proxy_busy_buffers_size 64k;
}
```

### Test with curl

```bash
# Send large header to test
curl -H "X-Custom: $(python -c 'print("A"*10000')" http://example.com
```

### Debug Header Sizes

```bash
# Check response header sizes
curl -sI http://example.com | wc -c
curl -sI http://example.com | head -20
```

## Related Errors

- [Nginx 413 Error]({{< relref "/tools/nginx/nginx-413-error-v2" >}}) — request entity too large
- [Nginx 403 Forbidden]({{< relref "/tools/nginx/nginx-403-error-v2" >}}) — directory forbidden
- [Nginx SSL Error]({{< relref "/tools/nginx/nginx-ssl-error-v2" >}}) — SSL handshake failed
