---
title: "[Solution] Nginx Upstream Sent Too Big Header Error"
description: "The upstream response headers exceed the configured proxy_buffer_size limit."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The upstream response headers exceed the configured proxy_buffer_size limit.

## Common Causes

- **Large cookies** or session data
- **Many Set-Cookie headers**
- **Large Authorization headers**
- **Default buffer too small** (4k/8k)

## How to Fix

1. Increase buffer: `proxy_buffer_size 16k; proxy_buffers 4 16k;`
2. Reduce header size in backend
3. Strip headers: `proxy_hide_header Set-Cookie;`

## Examples

**Large buffer:**
```nginx
location /api/ {
    proxy_buffer_size 32k;
    proxy_buffers 8 32k;
    proxy_busy_buffers_size 64k;
    proxy_pass http://backend;
}
```