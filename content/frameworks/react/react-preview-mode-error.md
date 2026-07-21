---
title: "[Solution] React Preview Mode Error"
description: "Preview mode not working."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Preview mode not working.

## Common Causes

Not enabled.

## How to Fix

Enable preview.

## Example

```javascript
// pages/api/preview.js
export default function handler(req, res) {
  res.setPreviewData({});
  res.redirect(req.query.redirect);
}
```
