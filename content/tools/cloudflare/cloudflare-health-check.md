---
title: "[Solution] Cloudflare Health Check Error"
description: "Fix Cloudflare health check errors. Resolve origin server monitoring issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Health Check Error can prevent your application from working correctly.

## Common Causes

- Health check path does not exist
- Timeout too short
- Interval too frequent
- Expected status code wrong

## How to Fix

### Create Check

```bash
curl -X POST "https://api.cloudflare.com/client/v4/zones/{zone_id}/load_balancers/monitors" \
  -H "Authorization: Bearer {api_token}" \
  -H "Content-Type: application/json" \
  --data '{"type":"https","path":"/health","expected_codes":"200","interval":60}'
```

### Check Results

```bash
curl -X GET "https://api.cloudflare.com/client/v4/zones/{zone_id}/load_balancers/origin_pools/{pool_id}" \
  -H "Authorization: Bearer {api_token}" | jq '.result.origins[] | {name,healthy}'
```

