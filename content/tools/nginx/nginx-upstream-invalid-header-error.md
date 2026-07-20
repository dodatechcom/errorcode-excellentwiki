---
title: "[Solution] Nginx Upstream Sent Invalid Header Error"
description: "The upstream server returned a malformed or invalid HTTP header in its response."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The upstream server returned a malformed or invalid HTTP header in its response.

## Common Causes

- **Backend generating malformed headers**
- **Duplicate headers** not allowed
- **Encoding issues** in header values
- **Backend proxy forwarding bad headers**

## How to Fix

1. Inspect: `curl -v http://backend:8080/api 2>&1 | head -30`
2. Use proxy manipulation: `proxy_hide_header X-Powered-By;`
3. Fix the backend
4. Enable debug: `error_log /var/log/nginx/error.log debug;`

## Examples

**Filter:**
```nginx
location /api/ {
    proxy_pass http://backend;
    proxy_hide_header X-Invalid-Header;
    proxy_set_header Accept-Encoding "";
}
```