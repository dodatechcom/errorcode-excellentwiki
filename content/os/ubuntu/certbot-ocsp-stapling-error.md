---
title: "Certbot OCSP Stapling Error"
description: "OCSP stapling not working or returning stale revocation data"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Certbot OCSP Stapling Error

OCSP stapling not working or returning stale revocation data

## Common Causes

- OCSP responder URL unreachable from server
- SSL Stapling not enabled in web server config
- OCSP response expired and not refreshed
- Staple cache file permissions wrong

## How to Fix

1. Test OCSP: `openssl s_client -connect example.com:443 -status`
2. Enable stapling in Nginx: `ssl_stapling on;`
3. Enable in Apache: `SSLUseStapling On`
4. Check OCSP cache: `ls -la /var/cache/ocsp/`

## Examples

```nginx
# Enable OCSP stapling in Nginx
server {
    ssl_stapling on;
    ssl_stapling_verify on;
    ssl_trusted_certificate /etc/letsencrypt/live/example.com/chain.pem;
    resolver 8.8.8.8 8.8.4.4 valid=300s;
}
```
