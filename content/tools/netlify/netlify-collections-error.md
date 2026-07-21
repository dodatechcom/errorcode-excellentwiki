---
title: "[Solution] Netlify CMS Collections Error"
description: "Fix Netlify CMS collections errors. Resolve collection configuration issues."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

Netlify CMS Collections Error can prevent your application from working correctly.

## Common Causes

- Collection not found
- Field missing
- Folder does not exist
- Slug pattern invalid

## How to Fix

### Configure Collection

```yaml
collections:
  - name: posts
    folder: content/posts
    slug: "{{year}}-{{month}}-{{day}}-{{slug}}"
    fields:
      - { name: title, widget: string }
```

