---
title: "[Solution] CSS Table Display Error"
description: "Table display and layout errors."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Table Display Error

Table display and layout errors.

### Common Causes
Wrong display; missing collapse

### How to Fix
```css
table { border-collapse: collapse; width: 100%; }
th, td { border: 1px solid #ddd; padding: 8px; }
```

### Examples
```css
.table-responsive {
  overflow-x: auto;
}
```
