---
title: "[Solution] Netlify Redirect Loop or Misconfiguration Error — How to Fix"
description: "Fix Netlify redirect loops and misconfigurations. Resolve infinite redirects, conflicting rules, and broken URL patterns."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
weight: 1
comments: true
---

A Netlify redirect loop or misconfiguration error occurs when redirect rules in `_redirects` or `netlify.toml` create an infinite cycle or conflict with each other, causing the browser to display a "too many redirects" error.

## What This Error Means

Netlify processes redirects in the order they are listed. When a redirect points to a URL that triggers another redirect back to the original, an infinite loop is created. The browser typically terminates the loop after 20 redirects and displays an error page.

## Why It Happens

- Two redirect rules create a circular reference
- A redirect rule matches its own destination URL
- Trailing slash rules conflict with path rewriting rules
- A catch-all pattern `/*` redirects to a path that matches `/*`
- The redirect source and destination are the same path
- Custom 404 page redirect creates a loop
- The `_redirects` file has duplicate rules
- A condition-based redirect does not account for all scenarios

## Common Error Messages

- `ERR_TOO_MANY_REDIRECTS` — Browser detected infinite redirect loop
- `This page isn't working` — Redirect loop error page
- `The page was redirected too many times` — Chrome redirect error
- `308 Loop detected` — Netlify terminated the redirect chain

## How to Fix It

### Audit Redirect Rules

```bash
# Check _redirects file
cat static/_redirects

# Or check netlify.toml redirects
cat netlify.toml | grep -A 3 "\[\[redirects\]\]"

# List all redirects and look for circular patterns
```

### Fix Circular Redirects

```bash
# WRONG: Creates a loop
/blog          /blog/          301
/blog/         /blog           301

# RIGHT: Choose one direction
/blog          /blog/          301
# Remove the second rule entirely
```

### Fix Catch-All Patterns

```bash
# WRONG: Catch-all redirects to a path that matches catch-all
/*             /index.html     200
/page          /*              301

# RIGHT: Use specific paths or conditional logic
/page          /other-page     301
/*             /index.html     200
```

### Use Netlify.toml Redirects

```toml
# netlify.toml — proper redirect configuration
[[redirects]]
  from = "/old-page"
  to = "/new-page"
  status = 301
  force = false

# Use force: true to override other rules
[[redirects]]
  from = "/api/*"
  to = "/.netlify/functions/:splat"
  status = 200
  force = true

# Use conditions to avoid loops
[[redirects]]
  from = "/blog/:slug"
  to = "/blog/:slug/"
  status = 301
  conditions = {Role = ["admin"]}
```

### Debug Redirect Chains

```bash
# Trace redirects with curl
curl -vL https://your-domain.com/page 2>&1 | grep -i "location"

# This shows each redirect hop:
# < HTTP/1.1 301 Moved Permanently
# < location: /page/
# < HTTP/1.1 301 Moved Permanently
# < location: /page  ← Loop detected!

# Check all redirects at once
curl -sI https://your-domain.com/old-path | grep -i "location"
```

### Handle Trailing Slash Consistency

```toml
# netlify.toml — enforce consistent trailing slashes

# Force trailing slashes
[[redirects]]
  from = "/:path"
  to = "/:path/"
  status = 301
  conditions = {Role = ["admin"]}

# Remove trailing slashes (alternative)
[[redirects]]
  from = "/:path/"
  to = "/:path"
  status = 301
  conditions = {Role = ["admin"]}
```

### Fix SPA Fallback Issues

```toml
# netlify.toml — proper SPA fallback without loops

# WRONG: SPA fallback that creates loops
# [[redirects]]
#   from = "/*"
#   to = "/index.html"
#   status = 200

# RIGHT: Use a more specific pattern
[[redirects]]
  from = "/app/*"
  to = "/app/index.html"
  status = 200

# For Next.js or React Router, use the catch-all at the end
[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

## Common Scenarios

- **Migration redirect conflicts:** Old site had `/blog` redirect to `/blog/` but new site redirects `/blog/` to `/blog`, creating a loop.
- **SPA fallback loop:** A catch-all `/*` rule redirects to `/index.html`, but `/index.html` is also matched by another rule that redirects elsewhere.
- **Custom 404 redirect:** A rule redirects 404 pages to the homepage, but the homepage itself returns a 404 due to a missing file.

## Prevent It

1. Always test redirect rules with `curl -vL` before deploying to production
2. Use `force: false` (default) for most redirects to avoid overriding other rules
3. Maintain a documented list of all redirect rules and verify they do not create circular references

## Related Pages

- [Netlify Redirect Error]({{< relref "/tools/netlify/netlify-redirect-error" >}}) — Redirect misconfiguration
- [Netlify Headers Error]({{< relref "/tools/netlify/netlify-headers-error" >}}) — Headers issues
