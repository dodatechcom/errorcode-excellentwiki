---
title: "[Solution] Netlify Status Code Error"
description: "Fix Netlify status code errors. Resolve HTTP status code configuration issues."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

Netlify Status Code Error can prevent your application from working correctly.

## Common Causes

- Status code missing in redirect
- Incorrect status code
- Default status code wrong

## How to Fix

### Set Status Code

```toml
[[redirects]]
from = "/old"
to = "/new"
status = 301
```

