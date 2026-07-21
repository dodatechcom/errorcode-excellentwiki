---
title: "[Solution] Netlify SPA Redirect Error"
description: "Fix Netlify single-page application redirect errors when client-side routing fails."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

# Netlify SPA Redirect Error

Netlify SPA routing fails when navigating to routes directly.

```
Page not found for /dashboard
```

## Common Causes

- SPA redirect rule missing
- _redirects file not in publish directory
- Redirect conflicts with API routes
- File extensions matching routes
- Redirect order incorrect

## How to Fix

### Add SPA Fallback Redirect

```toml
# netlify.toml
[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

### Create _redirects File

```
# public/_redirects
/*  /index.html  200
```

### Preserve API Routes

```toml
# API routes must come before SPA catch-all
[[redirects]]
  from = "/api/*"
  to = "/.netlify/functions/:splat"
  status = 200

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

### Handle Specific Routes

```toml
# Redirect specific routes to pages
[[redirects]]
  from = "/dashboard"
  to = "/index.html"
  status = 200

[[redirects]]
  from = "/settings"
  to = "/index.html"
  status = 200
```

### Fix Next.js Routes

```toml
# For Next.js, use @netlify/plugin-nextjs plugin
[[plugins]]
  package = "@netlify/plugin-nextjs"
```

## Examples

```toml
# Complete SPA redirect setup
[[redirects]]
  from = "/api/*"
  to = "/.netlify/functions/:splat"
  status = 200

[[redirects]]
  from = "/assets/*"
  to = "/assets/:splat"
  status = 200

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```
