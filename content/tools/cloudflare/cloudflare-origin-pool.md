---
title: "[Solution] Cloudflare Origin Pool Error"
description: "Fix Cloudflare origin pool errors. Resolve origin server pool configuration issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Origin Pool Error can prevent your application from working correctly.

## Common Causes

- No origins in pool
- Origin address incorrect
- Origin weight misconfigured
- Health check not assigned

## How to Fix

### Create Pool

```bash
curl -X POST "https://api.cloudflare.com/client/v4/zones/{zone_id}/load_balancers/origin_pools" \
  -H "Authorization: Bearer {api_token}" \
  -H "Content-Type: application/json" \
  --data '{"name":"my-pool","origins":[{"name":"origin1","address":"192.0.2.1","enabled":true}]}'
```

