---
title: "[Solution] Cloudflare Worker Route Error"
description: "Fix Cloudflare Worker route errors. Resolve Worker route configuration issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Worker Route Error can prevent your application from working correctly.

## Common Causes

- Route pattern incorrect
- Route conflicts with other Workers
- Route not associated with zone
- Pattern does not match intended URLs

## How to Fix

### List Routes

```bash
curl -X GET "https://api.cloudflare.com/client/v4/zones/{zone_id}/workers/routes" \
  -H "Authorization: Bearer {api_token}" | jq '.result'
```

### Add Route

```bash
curl -X POST "https://api.cloudflare.com/client/v4/zones/{zone_id}/workers/routes" \
  -H "Authorization: Bearer {api_token}" \
  -H "Content-Type: application/json" \
  --data '{"pattern":"example.com/api/*","script":"my-worker"}'
```

