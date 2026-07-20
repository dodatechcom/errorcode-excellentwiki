---
title: "[Solution] Nginx Certificate Expired Error"
description: "The SSL certificate has passed its validity period and can no longer be used."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The SSL certificate has passed its validity period and can no longer be used.

## Common Causes

- **Auto-renewal failed** (certbot timer not running)
- **Manual certificate** not renewed
- **Clock skew** on server
- **Wrong certificate file** linked

## How to Fix

1. Check: `openssl x509 -in cert.pem -noout -dates`
2. Renew: `sudo certbot renew --force-renewal && sudo nginx -s reload`
3. Enable auto-renewal: `sudo systemctl enable --now certbot.timer`
4. Check clock: `timedatectl`

## Examples

**Check expiry:**
```bash
openssl x509 -in /etc/ssl/certs/example.com.pem -noout -enddate
```
**Renew:**
```bash
sudo certbot renew
sudo nginx -t && sudo nginx -s reload
```