---
title: "[Solution] Vercel Redirects Error"
description: "Fix Vercel redirects errors when URL redirects fail or create loops."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vercel Redirects Error

Vercel redirect rules produce incorrect redirects or loops.

```
Error: Redirect loop detected
```

## Common Causes

- Circular redirect rules
- Redirect to same path
- Missing trailing slash configuration
- Conflicting redirect and rewrite rules
- Permanent redirect used for temporary changes

## How to Fix

### Configure Redirects

```json
// vercel.json
{
  "redirects": [
    {
      "source": "/old-page",
      "destination": "/new-page",
      "permanent": true
    }
  ]
}
```

### Fix Trailing Slash

```json
{
  "trailingSlash": true,
  "redirects": [
    { "source": "/blog/:slug", "destination": "/blog/:slug/" }
  ]
}
```

### Prevent Redirect Loops

```json
// Wrong - loop
{
  "redirects": [
    { "source": "/a", "destination": "/b" },
    { "source": "/b", "destination": "/a" }
  ]
}

// Correct - one direction only
{
  "redirects": [
    { "source": "/a", "destination": "/b", "permanent": true }
  ]
}
```

### Use Before Files

```json
{
  "redirects": [
    { "source": "/api/:path*", "destination": "/api" }
  ],
  "beforeFiles": [
    { "source": "/health", "destination": "/api/health" }
  ]
}
```

### Test Redirects

```bash
# Test redirect
curl -I https://yoursite.com/old-page

# Follow redirects
curl -IL https://yoursite.com/old-page
```

## Examples

```json
// Complete redirect configuration
{
  "redirects": [
    { "source": "/blog/:slug", "destination": "/posts/:slug", "permanent": true },
    { "source": "/docs/:path*", "destination": "/documentation/:path*", "permanent": false },
    { "source": "/old-api/:path*", "destination": "/api/v2/:path*", "permanent": true }
  ]
}
```
