---
title: "[Solution] Cloudflare Rate Limit Action Error"
description: "Fix Cloudflare rate limit action errors. Configure rate limit response behavior."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Rate Limit Action Error can prevent your application from working correctly.

## Common Causes

- Action set to challenge instead of block
- Simulation mode not showing blocks
- Response status code incorrect
- Timeout period too short or long

## How to Fix

### Configure Action

Actions: simulate, challenge, js_challenge, ban

```bash
curl -X PUT "https://api.cloudflare.com/client/v4/zones/{zone_id}/rate_limits/{rule_id}" \
  -H "Authorization: Bearer {api_token}" \
  -H "Content-Type: application/json" \
  --data '{"action":{"mode":"ban","timeout":300}}'
```

