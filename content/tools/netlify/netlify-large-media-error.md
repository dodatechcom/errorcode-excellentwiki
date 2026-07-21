---
title: "[Solution] Netlify Large Media Error"
description: "Fix Netlify Large Media errors when uploading or serving large media files via LFS."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

# Netlify Large Media Error

Netlify Large Media fails to upload or serve large files.

```
Error: Request Entity Too Large
```

## Common Causes

- File exceeds Large Media size limit
- Git LFS not configured properly
- Media path not set correctly
- Bandwidth limit exceeded
- Transform request invalid

## How to Fix

### Configure Large Media

```toml
# netlify.toml
[build]
  publish = "."

[large_media]
  patterns = ["images/*.{jpg,png,gif}", "videos/*.mp4"]
```

### Check File Size Limits

```bash
# Large Media accepts files up to:
# - Images: 50MB
# - Videos: 100MB
# Check file size
ls -lh images/large-file.jpg
```

### Set Up Git LFS

```bash
git lfs install
git lfs track "images/*.{jpg,png,gif}"
git lfs track "videos/*.mp4"
```

### Fix Transform Requests

```bash
# Check transform endpoint
curl -I https://your-site.netlify.app/.netlify/images/w:300,h:200/images/photo.jpg
```

### Check Bandwidth

```bash
# Monitor Large Media usage via Netlify Dashboard
# Site settings > Large Media
```

## Examples

```toml
# Full Large Media configuration
[large_media]
  patterns = [
    "images/**",
    "assets/**/*.{jpg,png,gif,webp}",
    "videos/*.mp4"
  ]
```

```html
<!-- Use Large Media transform URLs -->
<img src="/.netlify/images/w:400,h:300,f:auto/images/photo.jpg" />
```
