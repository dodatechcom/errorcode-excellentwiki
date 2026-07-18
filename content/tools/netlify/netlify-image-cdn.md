---
title: "[Solution] Netlify Image CDN Error — Fix Image Optimization Not Working"
description: "Fix Netlify Image CDN errors when automatic image transformations fail. Configure image transforms URL format and resolve optimization delivery issues."
tools: ["netlify"]
error-types: ["image-error"]
severities: ["warning"]
weight: 5
---

A Netlify Image CDN error occurs when automatic image optimization and transformation does not work. Images may not load, transform, or serve in the requested format.

## What This Error Means

Netlify Image CDN transforms images on the fly using URL parameters. When it fails:

```
Error: Image transformation failed
The requested image transformation is not supported
```

## Why It Happens

- The image URL does not use the correct Netlify Image CDN format
- The image is served from an external domain not configured for transformations
- The image format is not supported (SVG, GIF animation)
- The transformation parameters are invalid or exceed limits
- The image file is too large for the transformation service
- The image CDN feature is not enabled on the Netlify plan
- The _redirects file overrides the image CDN paths

## How to Fix It

### Use Correct Image URL Format

```
# Original image: /images/photo.jpg
# Transformed: /.netlify/images?url=/images/photo.jpg&w=200&h=200&fit=cover
```

### Set Allowed Domains in netlify.toml

```toml
[[image_cdn]]
  allowed_patterns = ["/images/*"]
  # Or for external domains:
  # allowed_domains = ["cdn.example.com"]
```

### Configure Image CDN in netlify.toml

```toml
[[image_cdn]]
  fit = "cover"
  quality = 80
  format = "webp"
```

### Use with HTML Images

```html
<img
  src="/.netlify/images?url=/images/photo.jpg&w=400&h=300&fit=cover"
  alt="Photo"
/>
```

### Check if Feature is Enabled

Image CDN requires a Pro or Enterprise plan.

### Verify No Redirect Conflicts

Ensure no `_redirects` rule intercepts `/.netlify/images` paths.

### Test with a Simple Transform

```
https://your-site.netlify.app/.netlify/images?url=/favicon.ico&w=64
```

## Common Mistakes

- Not using the `/.netlify/images` prefix for image transformations
- Expecting Image CDN to work with external SVG files (not supported)
- Forgetting to allow external domains in the Image CDN configuration
- Using Image CDN on a free plan (requires Pro or Enterprise)

## Related Pages

- [Netlify Build Error]({{< relref "/tools/netlify/netlify-build-error" >}}) -- Build failures
- [Netlify Redirect Error]({{< relref "/tools/netlify/netlify-redirect-error" >}}) -- Redirect configuration
- [Netlify Headers Error]({{< relref "/tools/netlify/netlify-headers-error" >}}) -- Headers configuration
