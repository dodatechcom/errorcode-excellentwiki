---
title: "[Solution] Cloudflare Challenge Passage Error"
description: "Fix Cloudflare challenge passage errors. Resolve browser challenge cookie issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Challenge Passage Error can prevent your application from working correctly.

## Common Causes

- Passage time too short causing repeated challenges
- Browser clearing cookies frequently
- Incognito mode re-triggering challenges
- Passage time too long allowing threats

## How to Fix

### Check Duration

```bash
curl -X GET "https://api.cloudflare.com/client/v4/zones/{zone_id}/settings/challenge_ttl" \
  -H "Authorization: Bearer {api_token}" | jq '.result'
```

### Update

```bash
curl -X PATCH "https://api.cloudflare.com/client/v4/zones/{zone_id}/settings/challenge_ttl" \
  -H "Authorization: Bearer {api_token}" \
  -H "Content-Type: application/json" \
  --data '{"value":1800}'
```

