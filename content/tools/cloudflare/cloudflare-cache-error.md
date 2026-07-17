---
title: "[Solution] Cloudflare Cache Rules Not Working Error — Fix Caching Issues"
description: "Fix Cloudflare cache rules not working. Resolve caching misconfigurations, stale content, and cache purge issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["warning"]
weight: 11
---

A Cloudflare cache rules not working error occurs when your configured caching behavior is not being applied as expected. Content may be served stale, cache may not be cleared, or rules may not match the intended requests.

## What This Error Means

Cloudflare's cache rules define how, when, and what content should be cached. When they do not work as expected, you might see stale content being served, cache headers being ignored, or purge operations having no effect.

## Why It Happens

- Cache rule expressions do not match the intended URLs
- Origin server cache headers override Cloudflare rules
- The Cache-Control header on the origin is set to no-cache or no-store
- Cache rules are applied in the wrong order
- Purge operations did not complete successfully
- The page rule or cache rule has a typo in the expression

## How to Fix It

### Check Cache Headers

```bash
# Check what headers your origin sends
curl -I https://your-domain.com/page.html

# Look for these headers:
# Cache-Control: max-age=86400
# CF-Cache-Status: HIT or MISS
# If you see: Cache-Control: no-cache, no-store
# That overrides Cloudflare cache rules
```

### Fix Origin Cache Headers

```nginx
# nginx configuration
location /static/ {
    # Let Cloudflare handle caching
    # Remove or override origin cache headers
    add_header Cache-Control "public, max-age=0";
    expires 0;
}
```

### Set Up Page Rules

```bash
# In Cloudflare Dashboard:
# Rules > Page Rules > Create Page Rule

# Example: Cache everything for /static/*
# URL: *your-domain.com/static/*
# Setting: Cache Level -> Cache Everything
# Setting: Edge Cache TTL -> 1 month
```

### Use Cache Rules

```bash
# In Cloudflare Dashboard:
# Rules > Cache Rules > Create Rule

# Example: Cache API responses
# Expression: http.request.uri.path eq "/api/data"
# Action: Cache everything
# Edge TTL: 60 seconds
# Browser TTL: 30 seconds
```

### Purge Cache Correctly

```bash
# Purge everything
curl -X DELETE "https://api.cloudflare.com/client/v4/zones/ZONE_ID/purge_cache" \
  -H "Authorization: Bearer API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{"purge_everything":true}'

# Purge specific URLs
curl -X DELETE "https://api.cloudflare.com/client/v4/zones/ZONE_ID/purge_cache" \
  -H "Authorization: Bearer API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
    "files": [
      "https://your-domain.com/page.html",
      "https://your-domain.com/style.css"
    ]
  }'
```

### Debug Cache Behavior

```bash
# Check cache status for a specific URL
curl -I https://your-domain.com/page.html 2>&1 | grep -i "cf-cache-status"

# CF-Cache-Status values:
# HIT - Served from Cloudflare cache
# MISS - Not in cache, fetched from origin
# DYNAMIC - Excluded from cache by default
# EXPIRED - Was in cache, now expired
# BYPASS - Cache rules set to bypass
# REVALIDATED - Stale but revalidated
```

## Common Mistakes

- Setting Cache-Control: no-store on origin and expecting Cloudflare to cache
- Not waiting after cache purge for changes to take effect
- Using overly broad bypass rules that exclude content from caching
- Forgetting that dynamic content (POST requests) is not cached by default
- Not checking CF-Cache-Status to verify caching behavior

## Related Pages

- [Cloudflare 502 Error]({{< relref "/tools/cloudflare/cloudflare-502" >}}) — Bad Gateway
- [Cloudflare 524 Error]({{< relref "/tools/cloudflare/cloudflare-524" >}}) — A timeout occurred
