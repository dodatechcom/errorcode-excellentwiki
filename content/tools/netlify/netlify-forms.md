---
title: "[Solution] Netlify Forms Error"
description: "Fix Netlify Forms errors. Resolve form submission and processing issues."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

Netlify Forms Error can prevent your application from working correctly.

## Common Causes

- Form not detected
- Form action missing
- Form name not set
- Netlify badge required

## How to Fix

### Configure Form

```html
<form name="contact" method="POST" data-netlify="true">
  <input type="hidden" name="form-name" value="contact">
  <input type="text" name="name">
  <input type="email" name="email">
  <button type="submit">Send</button>
</form>
```

