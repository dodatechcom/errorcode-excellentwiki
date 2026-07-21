---
title: "[Solution] CSS Viewport Error"
description: "Viewport meta tag issues."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Viewport Error

Viewport meta tag issues.

### Common Causes
Missing; wrong content; not responsive

### How to Fix
```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

### Examples
```css
@media (max-width: 480px) {
  .container { padding: 10px; }
}
```
