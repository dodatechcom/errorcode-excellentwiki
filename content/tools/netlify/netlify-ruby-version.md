---
title: "[Solution] Netlify Ruby Version Error"
description: "Fix Netlify Ruby version errors. Resolve Ruby version mismatch issues."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

Netlify Ruby Version Error can prevent your application from working correctly.

## Common Causes

- Ruby version not specified
- Incompatible Ruby version
- Gemfile missing
- Ruby gems not installed

## How to Fix

### Set Ruby Version

```toml
[build]
environment = { RUBY_VERSION = "3.1" }
```

