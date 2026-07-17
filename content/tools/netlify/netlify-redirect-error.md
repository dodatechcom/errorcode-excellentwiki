---
title: "[Solution] Netlify Redirect Rules Not Working Error — Fix Redirects"
description: "Fix Netlify redirect rules not working. Resolve redirect configuration issues, path matching, and redirect loops."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["warning"]
weight: 6
---

A Netlify redirect rules not working error occurs when configured redirects are not being applied. Requests either return 404s, serve the wrong content, or create redirect loops.

## What This Error Means

Netlify processes redirects from netlify.toml or _redirects file. When they do not work, the issue is usually with the syntax, rule order, or conflicting rules.

## Why It Happens

- The redirect syntax in netlify.toml or _redirects is wrong
- Rules are in the wrong order (more specific rules should come first)
- The from path does not match the incoming request
- The destination URL is unreachable
- Conflicting rules override each other
- The _redirects file is not in the publish directory
- Force flag is missing when needed

## How to Fix It

### Configure Redirects in netlify.toml

```toml
# netlify.toml
[[redirects]]
  from = "/old-page"
  to = "/new-page"
  status = 301

[[redirects]]
  from = "/blog/:slug"
  to = "/articles/:slug"
  status = 301

[[redirects]]
  from = "/api/*"
  to = "https://external-api.com/:splat"
  status = 200
```

### Use _redirects File

```
# _redirects (place in publish directory)
/old-page          /new-page          301
/blog/:slug        /articles/:slug    301
/api/*             https://api.com/:splat  200
```

### Handle Rewrite vs Redirect

```toml
# Redirect (changes URL in browser)
[[redirects]]
  from = "/old"
  to = "/new"
  status = 301

# Rewrite (keeps original URL, serves different content)
[[redirects]]
  from = "/app/*"
  to = "/index.html"
  status = 200
  force = false
```

### Fix Redirect Loops

```toml
# WRONG: Creates a loop
[[redirects]]
  from = "/app"
  to = "/app"
  status = 301

# RIGHT: Use force only when needed
[[redirects]]
  from = "/app"
  to = "/app/index.html"
  status = 200
  force = false
```

### Test Redirects

```bash
# Test a redirect
curl -I https://your-domain.com/old-page

# Should show:
# HTTP/2 301
# location: /new-page

# Test with follow redirects
curl -L https://your-domain.com/old-page
```

### Debug Redirect Issues

```bash
# Check if redirects are loaded
# In Netlify Dashboard:
# Site > Build & deploy > Post processing > Redirects

# Check for syntax errors in build log
netlify build 2>&1 | grep -i redirect
```

### Use Correct Rule Order

```toml
# Process in order - specific rules first
[[redirects]]
  from = "/api/v1/special"
  to = "/api/v1/handler"
  status = 200

[[redirects]]
  from = "/api/*"
  to = "/api-handler/:splat"
  status = 200
```

## Common Mistakes

- Placing catch-all rules before specific rules
- Using `/*` instead of `/:splat` for path parameters
- Not including the _redirects file in the publish directory
- Using `force: true` unnecessarily which bypasses file existence checks
- Not testing redirects after deployment

## Related Pages

- [Netlify Form Error]({{< relref "/tools/netlify/netlify-redirect-error" >}}) — Forms not receiving submissions
- [Netlify Build Error]({{< relref "/tools/netlify/netlify-build-error" >}}) — Build failed
