---
title: "[Solution] Nginx Proxy Buffer Size Error"
description: "The proxy buffer is too small to hold the upstream response headers or body."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The proxy buffer is too small to hold the upstream response headers or body.

## Common Causes

- **Default buffer too small** (4k)
- **Large cookies/auth tokens**
- **Multiple Set-Cookie headers**
- **Response larger than buffers**

## How to Fix

1. Increase: `proxy_buffer_size 16k; proxy_buffers 4 32k;`
2. Temp files: `proxy_max_temp_file_size 1024m;`
3. Disable for streaming: `proxy_buffering off;`

## Examples

**Upload (no buffering):**
```nginx
location /upload/ {
    proxy_buffering off;
    proxy_request_buffering off;
    client_max_body_size 100M;
    proxy_pass http://backend:8080;
}
```
**API:**
```nginx
proxy_buffer_size 16k; proxy_buffers 8 16k; proxy_busy_buffers_size 32k;
```