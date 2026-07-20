---
title: "[Solution] Nginx No SSL Configured Error"
description: "SSL parameters are referenced but no SSL certificate or key is configured."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

SSL parameters are referenced but no SSL certificate or key is configured.

## Common Causes

- **ssl on** without certificate directives
- **listen 443 ssl** without ssl_certificate
- **Missing include** for SSL fragment
- **Certificate directives commented out**

## How to Fix

1. Always provide both certificate and key
2. Create reusable SSL snippet
3. Validate: `sudo nginx -t`

## Examples

**Broken:**
```nginx
server { listen 443 ssl; server_name example.com; }
```
**Fixed:**
```nginx
server {
    listen 443 ssl http2; server_name example.com;
    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
}
```