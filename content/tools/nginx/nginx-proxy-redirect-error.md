---
title: "[Solution] Nginx Proxy Redirect Error"
description: "The proxy_redirect directive is misconfigured or cannot rewrite the Location header."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The proxy_redirect directive is misconfigured or cannot rewrite the Location header.

## Common Causes

- **Invalid proxy_redirect syntax**
- **Redirect URL does not match** upstream response
- **Missing proxy_redirect default**
- **Multiple conflicting redirects**

## How to Fix

1. Use default: `proxy_redirect default;`
2. Override specific: `proxy_redirect http://backend:8080/ https://example.com/;`
3. Disable: `proxy_redirect off;`

## Examples

**Rewrite:**
```nginx
location /api/ {
    proxy_pass http://backend:8080/api/;
    proxy_redirect http://backend:8080/ https://example.com/;
}
```
**Default:**
```nginx
location / { proxy_pass http://backend:8080/; proxy_redirect default; }
```