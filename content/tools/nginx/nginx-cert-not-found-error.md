---
title: "[Solution] Nginx Certificate Not Found Error"
description: "Nginx cannot locate the SSL certificate file specified in the configuration."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

Nginx cannot locate the SSL certificate file specified in the configuration.

## Common Causes

- **File path typo** in ssl_certificate
- **Certificate not generated** or expired
- **Permissions issue**
- **Certificate deleted or moved** by renewal

## How to Fix

1. Verify: `ls -la /etc/ssl/certs/example.com.pem`
2. Check permissions: `sudo -u nginx cat /path/to/cert.pem`
3. Renew if needed: `sudo certbot renew`
4. Fix the path in config

## Examples

**Broken (typo):**
```nginx
ssl_certificate /etc/ssl/certs/exmaple.com.pem;
```
**Fixed:**
```nginx
ssl_certificate /etc/ssl/certs/example.com.pem;
ssl_certificate_key /etc/ssl/private/example.com.key;
```
**Verify:**
```bash
openssl x509 -in /etc/ssl/certs/example.com.pem -noout -text | head -5
```