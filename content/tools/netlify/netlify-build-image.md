---
title: "[Solution] Netlify Build Image Error"
description: "Fix Netlify build image errors. Resolve build environment issues."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

Netlify Build Image Error can prevent your application from working correctly.

## Common Causes

- Build image outdated
- Missing system dependencies
- Docker image not available
- Image version deprecated

## How to Fix

### Check Build Image

1. Go to Site Settings > Build & deploy
2. Select build image

### Use Specific Version

```toml
[build]
image = "nodejs18"
```

