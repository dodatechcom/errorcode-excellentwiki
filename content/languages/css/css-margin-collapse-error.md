---
title: "[Solution] CSS Margin Collapse Error"
description: "Margins collapsing unexpectedly."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Margin Collapse Error

Margins collapsing unexpectedly.

### Common Causes
Block margins collapse vertically

### How to Fix
```css
/* Wrong - margins collapse */
.parent { margin-bottom: 20px; }
.child { margin-top: 20px; }
/* Fix - use padding or border */
.parent { padding-bottom: 20px; }
```

### Examples
```css
.container {
  padding-top: 20px;
}
```
