---
title: "[Solution] Cloudflare Certificate Pack Error"
description: "Fix Cloudflare certificate pack errors. Resolve Advanced Certificate Manager issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Certificate Pack Error can prevent your application from working correctly.

## Common Causes

- Certificate pack validation failed
- Too many hostnames for a single pack
- Duplicate certificate requests
- Certificate authority rate limits

## How to Fix

### List Packs

```bash
curl -X GET "https://api.cloudflare.com/client/v4/zones/{zone_id}/ssl/certificate_packs" \
  -H "Authorization: Bearer {api_token}" | jq '.result'
```

### Request New Pack

```bash
curl -X POST "https://api.cloudflare.com/client/v4/zones/{zone_id}/ssl/certificate_packs" \
  -H "Authorization: Bearer {api_token}" \
  -H "Content-Type: application/json" \
  --data '{"hosts":["*.example.com","example.com"],"type":"advanced"}'
```

