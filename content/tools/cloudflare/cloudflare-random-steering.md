---
title: "[Solution] Cloudflare Random Steering Error"
description: "Fix Cloudflare random steering errors. Resolve random traffic distribution issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Random Steering Error can prevent your application from working correctly.

## Common Causes

- Only one pool configured
- Pool weights incorrect
- Fallback pool not set
- Health checks failing

## How to Fix

### Configure

```bash
curl -X PATCH "https://api.cloudflare.com/client/v4/zones/{zone_id}/load_balancers/{lb_id}" \
  -H "Authorization: Bearer {api_token}" \
  -H "Content-Type: application/json" \
  --data '{"steering_policy":"random","default_pools":["{pool_id1}","{pool_id2}"],"fallback_pool":"{pool_id1}"}'
```

