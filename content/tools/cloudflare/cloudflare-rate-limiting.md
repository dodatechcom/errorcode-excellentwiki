---
title: "[Solution] Cloudflare Rate Limiting Error"
description: "Fix Cloudflare rate limiting errors. Resolve request rate limit issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Rate Limiting Error can prevent your application from working correctly.

## Common Causes

- Rate limit threshold too low
- Legitimate traffic patterns exceed limit
- API calls not accounted for
- Rate limiting rule too broad

## How to Fix

### Check Rules

```bash
curl -X GET "https://api.cloudflare.com/client/v4/zones/{zone_id}/rate_limits" \
  -H "Authorization: Bearer {api_token}" | jq '.result'
```

### Create Custom Rate Limit

```bash
curl -X POST "https://api.cloudflare.com/client/v4/zones/{zone_id}/rate_limits" \
  -H "Authorization: Bearer {api_token}" \
  -H "Content-Type: application/json" \
  --data '{"match":{"request":{"uri":{"path":{"contains":"/api/"}}},"count":100},"action":{"mode":"simulate","timeout":600}}'
```

