---
title: "[Solution] Netlify Redirects Loop — Fix Infinite Redirect Loop Detected"
description: "Fix Netlify redirect loop errors when redirect rules create infinite cycles. Debug redirect patterns and resolve conflicting source and destination rules."
tools: ["netlify"]
error-types: ["configuration-error"]
severities: ["error"]
weight: 5
---

A Netlify redirect loop error occurs when redirect rules create a cycle where a URL redirects to itself or to another URL that redirects back. Browsers detect and stop the loop.

## What This Error Means

A redirect loop appears as a browser error:

```
This page isn't working
example.com redirected you too many times.
ERR_TOO_MANY_REDIRECTS
```

## Why It Happens

- A redirect source matches a pattern that includes the destination
- A `/index.html` rewrite causes the URL to redirect to itself
- A trailing slash redirect conflicts with a non-trailing slash rule
- An HTTP-to-HTTPS redirect paired with an HTTPS-to-HTTP redirect
- A `_redirects` rule directs a path to another path that redirects back
- The `force` parameter is set incorrectly on redirect rules

## How to Fix It

### Check Redirect Rules

```
# _redirects
# Avoid this:
/old-path    /new-path    301
/new-path    /old-path    301

# Correct:
/old-path    /new-path    301
```

### Check netlify.toml Redirects

```toml
[[redirects]]
  from = "/old-path"
  to = "/new-path"
  status = 301
  force = false
```

### Add Conditions to Prevent Loops

```toml
[[redirects]]
  from = "/app/*"
  to = "/index.html"
  status = 200
  conditions = {Language = ["en"]}

[[redirects]]
  from = "/app/*"
  to = "/index-fr.html"
  status = 200
  conditions = {Language = ["fr"]}
```

### Use 200 Status for SPA Rewrites

```toml
[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

### Test Redirects Locally

```bash
netlify dev
curl -I http://localhost:8888/old-path
```

### Check SSL/HTTPS Settings

Ensure you are not redirecting HTTP to HTTPS and then HTTPS back to HTTP.

## Common Mistakes

- Creating symmetric redirect rules that point to each other
- Using 301 (permanent) redirects for testing (browsers cache them aggressively)
- Forgetting that `/*` matches all paths including the destination
- Combining `_redirects` and `netlify.toml` redirect rules without checking for conflicts

## Related Pages

- [Netlify Redirect Error]({{< relref "/tools/netlify/netlify-redirect-error" >}}) -- Redirect configuration
- [Netlify Headers Error]({{< relref "/tools/netlify/netlify-headers-error" >}}) -- Headers configuration
- [Netlify Build Error]({{< relref "/tools/netlify/netlify-build-error" >}}) -- Build failures
