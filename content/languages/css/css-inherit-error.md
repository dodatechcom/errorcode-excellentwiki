---
title: "[Solution] CSS Inherit Error"
description: "inherit/initial/unset not working."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Inherit Error

inherit/initial/unset not working.

### Common Causes
Wrong property context; specificity

### How to Fix
```css
color: inherit;
font-size: initial;
```

### Examples
```css
.link {
  color: inherit;
  text-decoration: underline;
}
```
