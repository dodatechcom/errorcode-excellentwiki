---
title: "[Solution] Nginx OCSP Stapling Error"
description: "OCSP stapling failed because the responder URL is missing or unreachable."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

OCSP stapling failed because the responder URL is missing or unreachable.

## Common Causes

- **Responder URL unreachable**
- **Firewall blocking** outbound port 80
- **Intermediate CA missing**
- **Nginx cannot resolve** responder hostname

## How to Fix

1. Provide intermediate chain: `ssl_trusted_certificate /path/to/fullchain.pem;`
2. Configure stapling with resolver
3. Test: `openssl s_client -connect example.com:443 -status`
4. Allow outbound port 80

## Examples

**Config:**
```nginx
server {
    listen 443 ssl;
    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
    ssl_trusted_certificate /etc/letsencrypt/live/example.com/chain.pem;
    ssl_stapling on;
    ssl_stapling_verify on;
    resolver 1.1.1.1 8.8.8.8 valid=300s;
}
```