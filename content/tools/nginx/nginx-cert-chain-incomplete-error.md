---
title: "[Solution] Nginx Certificate Chain Incomplete Error"
description: "The server does not send the full certificate chain, causing client verification failures."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The server does not send the full certificate chain, causing client verification failures.

## Common Causes

- **Only leaf certificate** in ssl_certificate file
- **Missing intermediate certificates**
- **Wrong file** used for ssl_certificate
- **Certbot cert.pem** not fullchain.pem

## How to Fix

1. Use fullchain: `ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;`
2. Concatenate: `cat server.crt intermediate.crt root.crt > fullchain.crt`
3. Verify: `openssl verify -CAfile ca-certificates.crt fullchain.pem`
4. Test: `openssl s_client -connect example.com:443 2>&1 | grep Verify`

## Examples

**Check chain:**
```bash
openssl s_client -connect example.com:443 2>&1 | grep -E 'depth=|Verify'
```
**Build chain:**
```bash
cat your-domain.crt intermediate.crt > fullchain.pem
```