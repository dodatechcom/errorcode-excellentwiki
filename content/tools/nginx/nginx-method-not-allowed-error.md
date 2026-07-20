---
title: "[Solution] Nginx Method Not Allowed Error"
description: "The client sent an HTTP method not permitted for the requested resource (HTTP 405)."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The client sent an HTTP method not permitted for the requested resource (HTTP 405).

## Common Causes

- **Wrong method** (POST to GET-only)
- **CORS preflight** (OPTIONS) not handled
- **Restrictive Nginx config**

## How to Fix

1. Allow methods: `if ($request_method !~ ^(GET|POST|PUT|DELETE|PATCH)$) { return 405; }`
2. Use limit_except
3. Handle OPTIONS for CORS

## Examples

**Restrict:**
```nginx
location /upload/ {
    limit_except POST { deny all; }
    client_max_body_size 100M;
    proxy_pass http://backend;
}
```