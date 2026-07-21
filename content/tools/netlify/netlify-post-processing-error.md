---
title: "[Solution] Netlify Post Processing Error"
description: "Fix Netlify post processing errors when image optimization or asset transformation fails."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["warning"]
---

# Netlify Post Processing Error

Netlify post-processing fails to optimize or transform assets during deployment.

```
Post processing error: image optimization failed
```

## Common Causes

- Unsupported image format
- Image corrupt or malformed
- Post-processing timeout
- Feature not available on plan
- Configuration disables processing

## How to Fix

### Check Image Format Support

```bash
# Netlify supports:
# JPEG, PNG, GIF, WebP, SVG, AVIF
# Check image type
file images/photo.jpg
```

### Disable Post Processing

```toml
# netlify.toml
[build]
  command = "npm run build"

[build.processing]
  skip_processing = true
```

### Configure Selective Processing

```toml
[build.processing]
  [build.processing.css]
    bundle = true
    minify = true
  [build.processing.js]
    bundle = true
    minify = true
  [build.processing.images]
    compress = true
```

### Fix Corrupt Images

```bash
# Check image integrity
identify images/photo.jpg  # ImageMagick

# Re-export from source
convert source.psd -quality 85 output.jpg
```

### Enable Pretty URLs

```toml
[build.processing]
  pretty_urls = true
```

## Examples

```toml
# Custom processing configuration
[build.processing]
  skip_processing = false
  
  [build.processing.html]
    pretty_urls = true
    
  [build.processing.css]
    bundle = true
    minify = true
    
  [build.processing.js]
    bundle = true
    minify = true
    
  [build.processing.images]
    compress = true
```
