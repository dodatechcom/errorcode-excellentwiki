---
title: "[Solution] Cloudflare Image Optimization Error"
description: "Fix Cloudflare image optimization errors. Resolve Cloudflare Images and Polish issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Image Optimization Error can prevent your application from working correctly.

## Common Causes

- Images not proxied
- Polish setting too aggressive
- Image format not supported
- Origin image not accessible

## How to Fix

### Enable Polish

1. Go to Speed > Optimization
2. Enable Polish

### Use Image Resizing

```bash
curl -I "https://your-domain.com/cdn-cgi/image/width=300,height=200/image.jpg"
```

