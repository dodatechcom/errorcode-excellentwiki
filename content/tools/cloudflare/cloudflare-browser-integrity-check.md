---
title: "[Solution] Cloudflare Browser Integrity Check Error"
description: "Fix Cloudflare Browser Integrity Check errors. Resolve BIC blocking legitimate visitors."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Browser Integrity Check Error can prevent your application from working correctly.

## Common Causes

- Missing common browser headers
- Bot traffic flagged as malicious
- API clients without browser headers
- Custom headers triggering checks

## How to Fix

### Add Whitelist

```bash
curl -X POST "https://api.cloudflare.com/client/v4/zones/{zone_id}/firewall/rules" \
  -H "Authorization: Bearer {api_token}" \
  -H "Content-Type: application/json" \
  --data '[{"filter":{"expression":"ip.src eq 1.2.3.4"},"action":"allow","description":"Whitelist API client"}]'
```

### Fix Client Headers

Ensure API clients send appropriate User-Agent headers.

