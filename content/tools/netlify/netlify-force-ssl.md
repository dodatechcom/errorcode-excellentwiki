---
title: "[Solution] Netlify Force SSL Error"
description: "Fix Netlify force SSL errors. Resolve HTTPS enforcement issues."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

Netlify Force SSL Error can prevent your application from working correctly.

## Common Causes

- SSL not enforced
- Redirect loop
- Mixed content warnings
- Certificate not provisioned

## How to Fix

### Force SSL

```toml
[[redirects]]
from = "http://example.com/*"
to = "https://example.com/:splat"
status = 301
force = true
```

