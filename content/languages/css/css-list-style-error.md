---
title: "[Solution] CSS List Style Error"
description: "List-style-type errors."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS List Style Error

List-style-type errors.

### Common Causes
Wrong value; not removing default

### How to Fix
```css
ul { list-style-type: none; padding: 0; }
```

### Examples
```css
.nav { list-style: none; margin: 0; padding: 0; }
```
