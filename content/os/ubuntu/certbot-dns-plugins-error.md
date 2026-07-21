---
title: "Certbot DNS Plugin Configuration Error"
description: "Certbot DNS plugin (route53, cloudflare, etc.) fails to authenticate"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Certbot DNS Plugin Configuration Error

Certbot DNS plugin (route53, cloudflare, etc.) fails to authenticate

## Common Causes

- DNS plugin credentials invalid or expired
- API token does not have required permissions
- DNS plugin package not installed
- Configuration file path incorrect

## How to Fix

1. Check credentials: `certbot dns:<plugin> --help`
2. Verify API token with DNS provider
3. Install plugin: `sudo apt-get install python3-certbot-dns-<plugin>`
4. Test: `certbot dns:<plugin> --dns-<plugin>-credentials /path/to/creds.ini -d example.com --dry-run`

## Examples

```bash
# Install DNS plugin
sudo apt-get install python3-certbot-dns-cloudflare

# Create credentials file
echo 'dns_cloudflare_api_token = YOUR_TOKEN' > ~/.secrets/cloudflare.ini
chmod 600 ~/.secrets/cloudflare.ini

# Test certificate request
sudo certbot certonly --dns-cloudflare --dns-cloudflare-credentials ~/.secrets/cloudflare.ini -d example.com --dry-run
```
