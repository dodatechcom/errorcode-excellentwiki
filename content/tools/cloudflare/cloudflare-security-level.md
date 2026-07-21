---
title: "[Solution] Cloudflare Security Level Error"
description: "Fix Cloudflare security level errors. Resolve threat assessment blocking issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Security Level Error can prevent your application from working correctly.

## Common Causes

- Security level set too high
- Legitimate IPs getting challenged
- VPN or proxy traffic challenged
- Threat score threshold too low

## How to Fix

### Check Level

```bash
curl -X GET "https://api.cloudflare.com/client/v4/zones/{zone_id}/settings/security_level" \
  -H "Authorization: Bearer {api_token}" | jq '.result'
```

### Adjust

```bash
curl -X PATCH "https://api.cloudflare.com/client/v4/zones/{zone_id}/settings/security_level" \
  -H "Authorization: Bearer {api_token}" \
  -H "Content-Type: application/json" \
  --data '{"value":"medium"}'
```

### Whitelist IPs

Add trusted IPs to IP Access Rules.

