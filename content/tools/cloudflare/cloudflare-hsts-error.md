---
title: "[Solution] Cloudflare HSTS Error"
description: "Fix Cloudflare HSTS errors. Resolve HTTP Strict Transport Security configuration issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare HSTS Error can prevent your application from working correctly.

## Common Causes

- Max-age set too low or too high
- includeSubDomains applied incorrectly
- Preload submission causes issues
- HSTS header conflicts with origin

## How to Fix

### Configure HSTS

1. Go to SSL/TLS > Edge Certificates
2. Click Enable HSTS
3. Set max-age to at least 31536000

### Verify

```bash
curl -I https://your-domain.com | grep -i strict-transport
```

