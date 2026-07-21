---
title: "[Solution] CSS Ruleset Error"
description: "CSS ruleset with multiple selectors wrong."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Ruleset Error

CSS ruleset with multiple selectors wrong.

### Common Causes
Missing comma; wrong combinator

### How to Fix
```css
/* Wrong */
.h1 .h2 { color: red; }
/* Correct */
h1, h2 { color: red; }
```

### Examples
```css
h1, h2, h3 {
  color: var(--heading-color);
}
```
