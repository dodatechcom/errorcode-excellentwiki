---
title: "[Solution] Cloudflare Minimum TLS Version Error"
description: "Fix Cloudflare minimum TLS version errors. Resolve TLS version enforcement issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Minimum TLS Version Error can prevent your application from working correctly.

## Common Causes

- Minimum TLS set too high for client
- Legacy clients cannot connect
- API integrations use outdated TLS
- Setting changed accidentally

## How to Fix

### Check Current Setting

```bash
curl -X GET "https://api.cloudflare.com/client/v4/zones/{zone_id}/settings/min_tls_version" \
  -H "Authorization: Bearer {api_token}" | jq '.result'
```

### Update

```bash
curl -X PATCH "https://api.cloudflare.com/client/v4/zones/{zone_id}/settings/min_tls_version" \
  -H "Authorization: Bearer {api_token}" \
  -H "Content-Type: application/json" \
  --data '{"value":"1.2"}'
```

