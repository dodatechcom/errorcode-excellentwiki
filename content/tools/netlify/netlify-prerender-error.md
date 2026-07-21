---
title: "[Solution] Netlify Prerender Error"
description: "Fix Netlify prerender errors when pre-rendering pages for SEO fails."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["warning"]
---

# Netlify Prerender Error

Netlify prerendering fails to generate static HTML for dynamic pages.

```
Prerender error: timeout or rendering failed
```

## Common Causes

- Prerender service timeout
- Page requires authentication to render
- JavaScript errors preventing render
- External API calls timing out
- Too many pages to prerender

## How to Fix

### Configure Prerender

```toml
[[redirects]]
  from = "/*"
  to = "/.netlify/prerender/*"
  status = 200
  conditions = ["Prerender=true"]
```

### Add Prerender Headers

```toml
[[headers]]
  for = "/*"
  [headers.values]
    X-Robots-Tag = "index"
```

### Use netlify.toml Configuration

```toml
[build]
  command = "npm run build"
  publish = "dist"

[[plugins]]
  package = "netlify-plugin-prerender"
  [plugins.inputs]
    paths = ["/", "/about", "/contact"]
    renderer = "puppeteer"
```

### Fix Timeout Issues

```javascript
// Reduce page complexity for prerender
if (typeof window === 'undefined') {
  // Server-side rendering only
  await loadMinimalData();
}
```

### Exclude Pages from Prerender

```toml
[[redirects]]
  from = "/dashboard/*"
  to = "/index.html"
  status = 200
  # No Prerender header = not prerendered
```

## Examples

```toml
# Prerender configuration
[[redirects]]
  from = "/*"
  to = "/.netlify/prerender/:splat"
  status = 200
  force = true
  conditions = ["Prerender=true"]
```

```html
<!-- Check prerender status -->
<meta name="robots" content="index, follow">
```
