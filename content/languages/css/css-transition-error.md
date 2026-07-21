---
title: "[Solution] CSS Transition Error"
description: "CSS transition not working."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Transition Error

CSS transition not working.

### Common Causes
Wrong property; missing duration; no trigger

### How to Fix
```css
/* Wrong */
.element { transition: all; }
/* Correct */
.element { transition: opacity 0.3s ease; }
```

### Examples
```css
.button {
  transition: background-color 0.2s ease;
}
.button:hover {
  background-color: darkblue;
}
```
