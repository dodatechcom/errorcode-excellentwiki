---
title: "[Solution] Nginx Headers Too Large Error"
description: "The total size of all request headers exceeds the configured buffer limit."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The total size of all request headers exceeds the configured buffer limit.

## Common Causes

- **Too many cookies**
- **Large Authorization headers** (JWT)
- **Custom headers with large values**
- **Browser accumulating cookies**

## How to Fix

1. Increase: `large_client_header_buffers 4 32k;`
2. Reduce cookie size
3. Move large data to body
4. Strip cookies: `proxy_set_header Cookie $cookie_small;`

## Examples

**Increase:**
```nginx
large_client_header_buffers 8 16k;
```
**Strip cookies:**
```nginx
location /api/ { proxy_set_header Cookie ""; proxy_pass http://backend; }
```