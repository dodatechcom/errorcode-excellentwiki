---
title: "[Solution] Cloudflare Rocket Loader Error"
description: "Fix Cloudflare Rocket Loader errors. Resolve JavaScript optimization issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Rocket Loader Error can prevent your application from working correctly.

## Common Causes

- Scripts not loading correctly
- Third-party scripts broken
- Inline scripts affected
- Compatibility issues

## How to Fix

### Enable

1. Go to Speed > Optimization
2. Enable Rocket Loader

### Exclude Scripts

```html
<script data-cfasync="false" src="critical-script.js"></script>
```

