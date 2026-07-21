---
title: "[Solution] Cloudflare Pages Redirect Error"
description: "Fix Cloudflare Pages redirect errors. Resolve _redirects file issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Pages Redirect Error can prevent your application from working correctly.

## Common Causes

- _redirects syntax error
- Redirect creates a loop
- Status code incorrect
- Wildcard usage incorrect

## How to Fix

### Create _redirects

```
/old-page /new-page 301
/api/* /api/:splat 200
```

### Test

```bash
curl -I https://your-domain.com/old-page
```

