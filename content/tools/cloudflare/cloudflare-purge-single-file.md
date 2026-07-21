---
title: "[Solution] Cloudflare Purge Single File Error"
description: "Fix Cloudflare purge single file errors. Resolve individual file cache purge issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Purge Single File Error can prevent your application from working correctly.

## Common Causes

- URL does not match cached URL exactly
- Query string mismatch
- Protocol mismatch (http vs https)
- URL encoding issues

## How to Fix

### Purge URL

```bash
curl -X POST "https://api.cloudflare.com/client/v4/zones/{zone_id}/purge_cache" \
  -H "Authorization: Bearer {api_token}" \
  -H "Content-Type: application/json" \
  --data '{"files":["https://your-domain.com/path/to/file.css"]}'
```

### Verify

```bash
curl -I https://your-domain.com/path/to/file.css | grep -i "cf-cache-status"
```

