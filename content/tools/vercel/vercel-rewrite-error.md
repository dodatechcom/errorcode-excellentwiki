---
title: "[Solution] Vercel Rewrite or Redirect Loop Error — How to Fix"
description: "Fix Vercel rewrite or redirect loops. Resolve infinite redirect cycles, trailing slash conflicts, and misconfigured rules."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
weight: 1
comments: true
---

A Vercel rewrite or redirect loop error occurs when a redirect rule points to a URL that redirects back to itself or to another rule, creating an infinite cycle that the browser or Vercel terminates.

## What This Error Means

Redirect loops happen when Rule A redirects to a URL matched by Rule B, and Rule B redirects back to a URL matched by Rule A. Browsers detect this and display an error after approximately 20 hops. Vercel may also terminate the loop before the browser limit is reached.

## Why It Happens

- Two redirect rules create a circular reference
- A redirect rule matches its own destination URL
- Trailing slash rules conflict (add trailing slash vs remove trailing slash)
- HTTPS redirect combined with a redirect rule that goes to HTTP
- A rewrite and redirect rule both match the same path
- The `vercel.json` configuration has conflicting rewrite and redirect entries
- Middleware creates redirects that conflict with `vercel.json` rules

## Common Error Messages

- `ERR_TOO_MANY_REDIRECTS` — Browser detected infinite redirect loop
- `The redirect did not complete` — Vercel detected too many redirects
- `308 Too Many Redirects` — The loop was terminated by Vercel
- `This page isn't working` — Browser error page for redirect loops

## How to Fix It

### Audit Redirect Rules

```json
// vercel.json — check for circular rules
{
  "redirects": [
    {
      "source": "/old-page",
      "destination": "/new-page",
      "permanent": true
    },
    {
      "source": "/new-page",
      "destination": "/old-page",
      "permanent": false
    }
  ]
}
```

### Fix Trailing Slash Conflicts

```javascript
// next.config.js — choose one approach, not both
module.exports = {
  // Option A: Add trailing slashes
  trailingSlash: true,

  // Option B: Remove trailing slashes (default)
  // trailingSlash: false,
};
```

```json
// vercel.json — explicit trailing slash rules
{
  "redirects": [
    {
      "source": "/:path+/",
      "destination": "/:path+",
      "permanent": false
    }
  ]
}
```

### Prevent Self-Referencing Redirects

```json
// WRONG: Redirect matches its own destination
{
  "redirects": [
    {
      "source": "/blog/:slug",
      "destination": "/blog/:slug/"
    }
  ]
}

// RIGHT: Use trailingSlash option instead
// next.config.js
// { "trailingSlash": true }
```

### Separate Rewrite and Redirect Rules

```json
// WRONG: Rewrite and redirect on same path
{
  "rewrites": [
    { "source": "/app/:path*", "destination": "/:path*" }
  ],
  "redirects": [
    { "source": "/:path*", "destination": "/app/:path*" }
  ]
}

// RIGHT: Use rewrites only for internal routing
{
  "rewrites": [
    { "source": "/app/:path*", "destination": "/:path*" }
  ]
}
```

### Debug Redirect Loops

```bash
# Use curl to trace redirect chains
curl -vL https://your-domain.com/problem-path 2>&1 | grep -E "(< HTTP|< location|< Location)"

# This shows each redirect hop:
# < HTTP/1.1 301 Moved Permanently
# < Location: /new-page
# < HTTP/1.1 301 Moved Permanently
# < Location: /old-page  ← Loop detected!

# Check for redirect loops in your vercel.json
cat vercel.json | jq '.redirects[] | {source, destination}'
```

### Use Rewrites for Internal Routing

```javascript
// vercel.json — use rewrites instead of redirects for internal routing
{
  "rewrites": [
    // Internal rewrite — no redirect, no loop risk
    {
      "source": "/blog/:slug",
      "destination": "/blog/[slug]"
    },
    // Proxy to external API
    {
      "source": "/api/v1/:path*",
      "destination": "https://external-api.com/:path*"
    }
  ]
}

// Use beforeFiles and afterFiles for ordered rewrites
{
  "rewrites": {
    "beforeFiles": [
      { "source": "/api/:path*", "destination": "/api-handler/:path*" }
    ],
    "afterFiles": [
      { "source": "/blog/:slug", "destination": "/blog/[slug]" }
    ],
    "fallback": [
      { "source": "/:path*", "destination": "/404" }
    ]
  }
}
```

## Common Scenarios

- **Trailing slash inconsistency:** `trailingSlash: true` in next.config.js redirects `/blog/post` to `/blog/post/`, but a vercel.json rule redirects `/blog/post/` back to `/blog/post`.
- **HTTP to HTTPS redirect conflict:** A vercel.json rule redirects `http://example.com` to `https://example.com`, but another rule redirects `https://example.com` back to `http://example.com` for a specific path.
- **Legacy redirect rules:** Old redirect rules from a site migration are still active and conflict with new routing rules.

## Prevent It

1. Use `curl -vL` to trace redirect chains before deploying new redirect rules
2. Prefer rewrites over redirects for internal routing to avoid redirect loops entirely
3. Test all redirect rules with a variety of URLs in Vercel's preview deployment before merging to production

## Related Pages

- [Vercel Rewrite Error]({{< relref "/tools/vercel/vercel-rewrite-error" >}}) — Rewrite misconfiguration
- [Vercel Middleware Error]({{< relref "/tools/vercel/vercel-middleware-error" >}}) — Middleware runtime error
