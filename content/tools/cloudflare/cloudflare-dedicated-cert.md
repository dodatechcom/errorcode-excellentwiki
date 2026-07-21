---
title: "[Solution] Cloudflare Dedicated Certificate Error"
description: "Fix Cloudflare dedicated certificate errors. Resolve custom SSL certificate issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Dedicated Certificate Error can prevent your application from working correctly.

## Common Causes

- Certificate has expired
- Private key does not match certificate
- Certificate does not cover hostname
- Hostname is not part of your zone

## How to Fix

### Upload Certificate

```bash
curl -X POST "https://api.cloudflare.com/client/v4/zones/{zone_id}/custom_certificates" \
  -H "Authorization: Bearer {api_token}" \
  -F "certificate=@/path/to/cert.pem" \
  -F "private_key=@/path/to/key.pem"
```

### Verify Key Matches

```bash
openssl x509 -noout -modulus -in cert.pem | md5sum
openssl rsa -noout -modulus -in key.pem | md5sum
```

