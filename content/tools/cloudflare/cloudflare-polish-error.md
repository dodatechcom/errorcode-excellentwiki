---
title: "[Solution] Cloudflare Polish Error"
description: "Fix Cloudflare Polish errors. Resolve automatic image optimization issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Polish Error can prevent your application from working correctly.

## Common Causes

- Polish disabled
- Origin image too large
- Lossy compression artifacts
- Image served from cache

## How to Fix

### Enable Polish

1. Go to Speed > Optimization
2. Enable Polish

### Check Headers

```bash
curl -I https://your-domain.com/image.jpg | grep -i "cf-polished"
```

