---
title: "[Solution] Nginx Client Sent Malformed Headers Error"
description: "The client sent HTTP headers that are syntactically invalid or malformed."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The client sent HTTP headers that are syntactically invalid or malformed.

## Common Causes

- **Invalid characters** (control chars, null bytes)
- **Missing colon separator**
- **Extremely long header lines**
- **Binary data** in text headers

## How to Fix

1. Check client application
2. Increase buffers: `large_client_header_buffers 4 16k;`
3. Enable logging: `error_log /var/log/nginx/error.log warn;`
4. Use proxy_set_header to fix upstream headers

## Examples

**Increase:**
```nginx
server { listen 80; large_client_header_buffers 4 32k; }
```
**Inspect:**
```bash
tail -f /var/log/nginx/error.log | grep invalid
```