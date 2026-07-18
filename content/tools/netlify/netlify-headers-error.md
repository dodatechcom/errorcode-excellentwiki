---
title: "[Solution] Netlify Headers Error — Fix Headers Not Applied to Deployment"
description: "Fix Netlify headers errors when custom HTTP headers defined in netlify.toml or _headers are not applied. Debug header syntax, path matching, and priority conflicts."
tools: ["netlify"]
error-types: ["configuration-error"]
severities: ["warning"]
weight: 5
---

A Netlify headers error occurs when custom HTTP headers are not applied to site responses. The headers may be missing, incorrect, or overridden by Netlify defaults.

## What This Error Means

Netlify allows custom headers via `_headers` file or `netlify.toml`. When headers are not applied:

```
Warning: Headers defined in netlify.toml are not being applied
Expected X-Frame-Options: DENY, but got X-Frame-Options: SAMEORIGIN
```

## Why It Happens

- The `_headers` file is not in the publish directory
- The header syntax in `_headers` is incorrect
- The header path pattern does not match any route
- Netlify's built-in headers override the custom headers
- The headers configuration conflicts with security headers from the app
- The header values are invalid or contain prohibited characters
- The headers file has the wrong format (YAML instead of plaintext)

## How to Fix It

### Use the _headers File

```
# _headers (in publish directory)
/*
  X-Frame-Options: DENY
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin

/api/*
  Access-Control-Allow-Origin: *
  Content-Type: application/json
```

### Use netlify.toml Headers

```toml
[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"

[[headers]]
  for = "/api/*"
  [headers.values]
    Access-Control-Allow-Origin = "*"
```

### Check Header Priority

netlify.toml headers take priority over _headers file. More specific paths override less specific ones.

### Verify Publish Directory

```bash
ls -la dist/  # or your publish directory
cat dist/_headers
```

### Use Deploy Preview to Test

```bash
netlify deploy --build --open
# Check headers in browser dev tools
```

### Remove Conflicting App Headers

Check your application code for headers set via HTML meta tags or JavaScript.

## Common Mistakes

- Placing the `_headers` file in the project root instead of the publish directory
- Using YAML format in `_headers` (it uses a plaintext format)
- Defining headers in both `_headers` and `netlify.toml` with conflicting values
- Forgetting to re-deploy after making header configuration changes

## Related Pages

- [Netlify Redirects Loop]({{< relref "/tools/netlify/netlify-redirects-loop" >}}) -- Redirect loop detection
- [Netlify Build Error]({{< relref "/tools/netlify/netlify-build-error" >}}) -- Build failures
- [Netlify Deploy Error]({{< relref "/tools/netlify/netlify-deploy-error" >}}) -- Deploy failures
