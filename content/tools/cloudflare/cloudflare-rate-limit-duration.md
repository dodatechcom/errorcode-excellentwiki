---
title: "[Solution] Cloudflare Rate Limit Duration Error"
description: "Fix Cloudflare rate limit duration errors. Configure blocking duration after limit exceeded."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Rate Limit Duration Error can prevent your application from working correctly.

## Common Causes

- Duration too short allowing rapid retries
- Duration too long blocking legitimate users
- Duration not configured properly
- Timeout resets not working as expected

## How to Fix

### Set Duration

```bash
curl -X PUT "https://api.cloudflare.com/client/v4/zones/{zone_id}/rate_limits/{rule_id}" \
  -H "Authorization: Bearer {api_token}" \
  -H "Content-Type: application/json" \
  --data '{"action":{"mode":"ban","timeout":60}}'
```

### Recommended

- API abuse: 60-300s
- Login attempts: 900s
- Scraping: 3600s

