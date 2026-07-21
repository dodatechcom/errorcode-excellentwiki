---
title: "[Solution] CSS Initial Letter Error"
description: "Initial-letter property errors."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Initial Letter Error

Initial-letter property errors.

### Common Causes
Wrong syntax; browser support

### How to Fix
```css
.initial-letter {
  initial-letter: 3 1;
}
```

### Examples
```css
p::first-letter {
  initial-letter: 3;
  font-weight: bold;
}
```
