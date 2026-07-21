---
title: "[Solution] Cloudflare Origin Pool Unhealthy Error"
description: "Fix Cloudflare origin pool unhealthy errors. Resolve origin server health check failures."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Origin Pool Unhealthy Error can prevent your application from working correctly.

## Common Causes

- All origin servers are down
- Health check configuration wrong
- Firewall blocking health checks
- Origin returns error status

## How to Fix

### Check Origin

```bash
curl -I https://origin.example.com
```

### Update Pool

```bash
curl -X PATCH "https://api.cloudflare.com/client/v4/zones/{zone_id}/load_balancers/origin_pools/{pool_id}" \
  -H "Authorization: Bearer {api_token}" \
  -H "Content-Type: application/json" \
  --data '{"origins":[{"name":"origin1","address":"192.0.2.1","enabled":true}]}'
```

