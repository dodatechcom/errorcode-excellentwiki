---
title: "[Solution] Cloudflare Steering Policy Error"
description: "Fix Cloudflare steering policy errors. Resolve traffic routing issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Steering Policy Error can prevent your application from working correctly.

## Common Causes

- Policy not configured
- Fallback pool missing
- Default pools empty
- Policy conflicts with geo steering

## How to Fix

### Configure Policy

```bash
curl -X PATCH "https://api.cloudflare.com/client/v4/zones/{zone_id}/load_balancers/{lb_id}" \
  -H "Authorization: Bearer {api_token}" \
  -H "Content-Type: application/json" \
  --data '{"steering_policy":"random"}'
```

### Available Policies

random, least_connections, round_robin, hash, geo

