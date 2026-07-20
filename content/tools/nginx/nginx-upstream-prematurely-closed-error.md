---
title: "[Solution] Nginx Upstream Prematurely Closed Connection Error"
description: "The upstream server closed the connection before sending a complete response."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The upstream server closed the connection before sending a complete response.

## Common Causes

- **Backend worker crash** or OOM kill
- **FastCGI/php-fpm worker timeout**
- **Backend not handling keepalive**
- **Buffer too small** for response

## How to Fix

1. Increase buffers: `proxy_buffer_size 16k; proxy_buffers 4 32k;`
2. Add retry: `proxy_next_upstream error timeout http_502 http_503;`
3. Check backend logs: `journalctl -u app-backend --since '10 min ago'`
4. Match keepalive settings

## Examples

**Robust:**
```nginx
proxy_buffer_size 16k;
proxy_buffers 4 32k;
proxy_busy_buffers_size 64k;
proxy_connect_timeout 30s;
proxy_read_timeout 300s;
proxy_next_upstream error timeout http_502 http_503;
```