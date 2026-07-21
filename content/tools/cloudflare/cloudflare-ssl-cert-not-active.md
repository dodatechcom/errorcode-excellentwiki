---
title: "[Solution] Cloudflare SSL Certificate Not Active"
description: "Fix Cloudflare SSL certificate not active errors. Resolve certificate activation issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare SSL Certificate Not Active can prevent your application from working correctly.

## Common Causes

- Universal SSL is disabled
- DNS records are not proxied
- Certificate validation is pending
- Custom certificate uploaded incorrectly

## How to Fix

### Enable Universal SSL

```bash
curl -X PATCH "https://api.cloudflare.com/client/v4/zones/{zone_id}/ssl/tls/identity" \
  -H "Authorization: Bearer {api_token}" \
  -H "Content-Type: application/json" \
  --data '{"value":"universal"}'
```

### Check SSL Status

1. Go to SSL/TLS > Overview
2. Verify encryption mode is correct

