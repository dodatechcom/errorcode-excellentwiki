---
title: "[Solution] Netlify HTTPS Redirect Error"
description: "Fix Netlify HTTPS redirect errors. Resolve HTTP to HTTPS redirect issues."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

Netlify HTTPS Redirect Error can prevent your application from working correctly.

## Common Causes

- Redirect not working
- Loop detected
- Mixed content
- Certificate pending

## How to Fix

### Configure Redirect

```toml
[[redirects]]
from = "http://example.com/*"
to = "https://example.com/:splat"
status = 301
```

