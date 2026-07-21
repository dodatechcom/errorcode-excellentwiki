---
title: "[Solution] CSS Writing Mode Error"
description: "Writing-mode layout errors."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Writing Mode Error

Writing-mode layout errors.

### Common Causes
Wrong value; direction confusion

### How to Fix
```css
writing-mode: vertical-rl;
```

### Examples
```css
.vertical-text {
  writing-mode: vertical-rl;
  text-orientation: mixed;
}
```
