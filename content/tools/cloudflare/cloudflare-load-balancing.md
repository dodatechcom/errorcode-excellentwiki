---
title: "[Solution] Cloudflare Load Balancing Error"
description: "Fix Cloudflare load balancing errors. Resolve traffic distribution issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Load Balancing Error can prevent your application from working correctly.

## Common Causes

- No load balancer configured
- Origin pool is empty
- Health checks failing
- Steering policy misconfigured

## How to Fix

### Create Load Balancer

```bash
curl -X POST "https://api.cloudflare.com/client/v4/zones/{zone_id}/load_balancers" \
  -H "Authorization: Bearer {api_token}" \
  -H "Content-Type: application/json" \
  --data '{"name":"lb.example.com","fallback_pool":"{pool_id}","default_pools":["{pool_id}"]}'
```

