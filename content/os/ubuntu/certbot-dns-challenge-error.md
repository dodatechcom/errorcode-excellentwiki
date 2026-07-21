---
title: "[Solution] Ubuntu Server: certbot-dns-challenge-error"
description: "Fix Ubuntu certbot-dns-challenge-error. Certbot DNS challenge fails to verify domain."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Certbot DNS Challenge Error

Certbot DNS challenge fails to verify domain ownership.

## Common Causes
- DNS plugin not installed
- API credentials wrong
- DNS record not propagated

## How to Fix
1. Check DNS plugin
```bash
sudo certbot plugins | grep dns
```
2. Install DNS plugin
```bash
sudo apt install python3-certbot-dns-cloudflare
```
3. Configure credentials
```bash
sudo nano /etc/letsencrypt/dns-cloudflare.ini
dns_cloudflare_email = admin@example.com
dns_cloudflare_api_key = your-api-key
```

## Examples
```bash
$ sudo certbot plugins | grep dns
 * dns-cloudflare
 * dns-route53
```