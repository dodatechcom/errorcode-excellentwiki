---
title: "[Solution] Cloudflare Opportunistic Encryption Error"
description: "Fix Cloudflare opportunistic encryption errors. Resolve automatic HTTPS issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Opportunistic Encryption Error can prevent your application from working correctly.

## Common Causes

- SSL/TLS mode is set to Off
- Origin server does not support HTTPS
- Mixed content prevents encryption
- HSTS settings interfere

## How to Fix

### Enable Always Use HTTPS

1. Go to SSL/TLS > Edge Certificates
2. Enable Always Use HTTPS

### Set Full Strict

```bash
curl -X PATCH "https://api.cloudflare.com/client/v4/zones/{zone_id}/settings/ssl" \
  -H "Authorization: Bearer {api_token}" \
  -H "Content-Type: application/json" \
  --data '{"value":"strict"}'
```

