---
title: "[Solution] Cloudflare Universal SSL Error"
description: "Fix Cloudflare Universal SSL errors. Resolve automatic certificate provisioning issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Universal SSL Error can prevent your application from working correctly.

## Common Causes

- Universal SSL is disabled in settings
- DNS records are not proxied
- Domain not fully activated on Cloudflare
- Nameserver change not propagated

## How to Fix

### Enable Universal SSL

1. Go to SSL/TLS > Edge Certificates
2. Toggle Universal SSL to Enabled

### Verify

```bash
curl -X GET "https://api.cloudflare.com/client/v4/zones/{zone_id}/ssl/tls/identity" \
  -H "Authorization: Bearer {api_token}" | jq '.result.enabled'
```

