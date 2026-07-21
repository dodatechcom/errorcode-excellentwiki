---
title: "[Solution] Netlify Redirect Loop Error"
description: "Fix Netlify redirect loop errors when redirects create infinite loops between pages."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

# Netlify Redirect Loop Error

Netlify creates infinite redirect loops when redirect rules conflict.

```
ERR_TOO_MANY_REDIRECTS
```

## Common Causes

- Redirect rules pointing to each other
- Force SSL redirect conflicting with custom redirects
- Redirect from path to itself
- Multiple redirect rules matching same URL
- SPA redirect conflicting with page routes

## How to Fix

### Check Redirect Rules

```toml
# netlify.toml
[[redirects]]
  from = "/old-page"
  to = "/new-page"
  status = 301
```

### Fix Circular Redirects

```toml
# Wrong - creates loop
[[redirects]]
  from = "/a"
  to = "/b"
[[redirects]]
  from = "/b"
  to = "/a"

# Correct - only redirect once
[[redirects]]
  from = "/a"
  to = "/b"
  status = 301
```

### Avoid Self-Redirects

```toml
# Wrong - redirects to same path
[[redirects]]
  from = "/page"
  to = "/page"

# Correct
[[redirects]]
  from = "/old-page"
  to = "/page"
  status = 301
```

### Order Redirects Correctly

```toml
# More specific rules first
[[redirects]]
  from = "/api/v1/*"
  to = "/api/v2/:splat"
  status = 301

[[redirects]]
  from = "/api/*"
  to = "/api/v2/:splat"
  status = 301
```

### Test Redirects

```bash
# Check redirect with curl
curl -I https://yoursite.com/page
# Follow redirects and check for loops
curl -IL https://yoursite.com/page
```

## Examples

```toml
# Non-looping redirects
[[redirects]]
  from = "/blog/:slug"
  to = "/posts/:slug"
  status = 301

[[redirects]]
  from = "/posts/:slug"
  to = "/blog/:slug"
  status = 301
  # Only use one direction
```
