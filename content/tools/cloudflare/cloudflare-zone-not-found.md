---
title: "[Solution] Cloudflare Zone Not Found"
description: "Fix Cloudflare zone not found errors. Resolve domain not recognized in Cloudflare account."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Zone Not Found can prevent your application from working correctly.

## Common Causes

- Domain not added to Cloudflare
- Domain is in a different Cloudflare account
- API token lacks permission for the zone
- Zone was recently removed or transferred

## How to Fix

### List Zones

```bash
curl -X GET "https://api.cloudflare.com/client/v4/zones" \
  -H "Authorization: Bearer {api_token}"
```

### Add Domain

1. Log in to Cloudflare dashboard
2. Click Add a Site
3. Enter your domain name
4. Select a plan
5. Update nameservers at your registrar

