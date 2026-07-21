---
title: "[Solution] Cloudflare Purge Cache Error"
description: "Fix Cloudflare purge cache errors. Resolve cache purge failures."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Purge Cache Error can prevent your application from working correctly.

## Common Causes

- Purge API rate limit exceeded
- Invalid URL format in single-file purge
- Zone is paused
- API token lacks cache purge permissions

## How to Fix

### Purge Everything

```bash
curl -X POST "https://api.cloudflare.com/client/v4/zones/{zone_id}/purge_cache" \
  -H "Authorization: Bearer {api_token}" \
  -H "Content-Type: application/json" \
  --data '{"purge_everything":true}'
```

### Purge Single File

```bash
curl -X POST "https://api.cloudflare.com/client/v4/zones/{zone_id}/purge_cache" \
  -H "Authorization: Bearer {api_token}" \
  -H "Content-Type: application/json" \
  --data '{"files":["https://your-domain.com/image.png"]}'
```

