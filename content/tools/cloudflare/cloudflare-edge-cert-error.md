---
title: "[Solution] Cloudflare Edge Certificate Error"
description: "Fix Cloudflare edge certificate errors. Resolve SSL issues at edge servers."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Edge Certificate Error can prevent your application from working correctly.

## Common Causes

- Universal SSL still provisioning
- Custom SSL certificate expired
- Certificate does not cover hostname
- Certificate chain is incomplete

## How to Fix

### Check Certificate

```bash
openssl s_client -connect your-domain.com:443 -servername your-domain.com </dev/null 2>/dev/null | openssl x509 -noout -dates
```

### Reissue Certificate

1. Go to SSL/TLS > Edge Certificates
2. Click on the certificate
3. Select Reissue

