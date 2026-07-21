---
title: "[Solution] Cloudflare Health Monitor Fail Error"
description: "Fix Cloudflare health monitor fail errors. Resolve origin server health check issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Health Monitor Fail Error can prevent your application from working correctly.

## Common Causes

- Monitor configuration incorrect
- Origin returns error status
- Health check path does not exist
- Timeout too short

## How to Fix

### Create Monitor

```bash
curl -X POST "https://api.cloudflare.com/client/v4/zones/{zone_id}/load_balancers/monitors" \
  -H "Authorization: Bearer {api_token}" \
  -H "Content-Type: application/json" \
  --data '{"type":"https","path":"/health","interval":60,"retries":2,"timeout":5}'
```

