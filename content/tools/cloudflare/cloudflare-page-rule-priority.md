---
title: "[Solution] Cloudflare Page Rule Priority Error"
description: "Fix Cloudflare page rule priority errors. Resolve conflicts with multiple matching rules."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Page Rule Priority Error can prevent your application from working correctly.

## Common Causes

- Multiple rules match same URL
- Rules added without considering priority
- Wildcard patterns overlap
- Rule order changed accidentally

## How to Fix

### List by Priority

```bash
curl -X GET "https://api.cloudflare.com/client/v4/zones/{zone_id}/pagerules?order=priority" \
  -H "Authorization: Bearer {api_token}" | jq '.result[] | {id,priority}'
```

### Update Priority

```bash
curl -X PATCH "https://api.cloudflare.com/client/v4/zones/{zone_id}/pagerules/{rule_id}" \
  -H "Authorization: Bearer {api_token}" \
  -H "Content-Type: application/json" \
  --data '{"priority":1}'
```

