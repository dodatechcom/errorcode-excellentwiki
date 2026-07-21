---
title: "[Solution] Vercel Rewrite Error"
description: "Fix Vercel rewrite errors when URL rewriting rules produce unexpected behavior."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vercel Rewrite Error

Vercel rewrites fail or produce unexpected routing behavior.

```
Error: Rewrite to invalid destination
```

## Common Causes

- Rewrite destination does not exist
- Rewrite loop detected
- Missing protocol in destination
- Rewrite conflicts with redirects
- Incorrect path matching

## How to Fix

### Basic Rewrite Configuration

```json
// vercel.json
{
  "rewrites": [
    { "source": "/blog/:slug", "destination": "/posts/:slug" }
  ]
}
```

### Fix Rewrite Loops

```json
// Wrong - creates loop
{
  "rewrites": [
    { "source": "/page", "destination": "/page" }
  ]
}

// Correct
{
  "rewrites": [
    { "source": "/old-page", "destination": "/new-page" }
  ]
}
```

### Use Rewrites with Before Files

```json
{
  "rewrites": [
    { "source": "/api/:path*", "destination": "/api" }
  ],
  "beforeFiles": [
    { "source": "/health", "destination": "/api/health" }
  ]
}
```

### Handle Dynamic Rewrites

```json
{
  "rewrites": [
    {
      "source": "/user/:id/:tab?",
      "destination": "/profile"
    }
  ]
}
```

### Check Rewrite with Regex

```json
{
  "rewrites": [
    {
      "source": "/(.*).json",
      "destination": "/api/data"
    }
  ]
}
```

## Examples

```json
// Complete rewrite configuration
{
  "rewrites": [
    { "source": "/blog/:slug", "destination": "/blog?slug=:slug" },
    { "source": "/docs/:path*", "destination": "/docs/:path*" },
    { "source": "/legacy/:path*", "destination": "/v2/:path*" }
  ]
}
```
