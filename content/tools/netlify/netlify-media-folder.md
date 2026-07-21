---
title: "[Solution] Netlify CMS Media Folder Error"
description: "Fix Netlify CMS media folder errors. Resolve media storage issues."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

Netlify CMS Media Folder Error can prevent your application from working correctly.

## Common Causes

- Media folder not found
- Folder not configured
- Upload failed
- Media not displaying

## How to Fix

### Configure Media

```yaml
media_folder: static/images
public_folder: /images
```

