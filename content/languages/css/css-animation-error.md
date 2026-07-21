---
title: "[Solution] CSS Animation Error"
description: "CSS animation property errors."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Animation Error

CSS animation property errors.

### Common Causes
Wrong keyframe name; missing animation-name

### How to Fix
```css
/* Wrong */
.element { animation: fadeIn 1s; }
/* Correct */
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
.element { animation: fadeIn 1s ease-in-out; }
```

### Examples
```css
@keyframes slideIn {
  from { transform: translateX(-100%); }
  to { transform: translateX(0); }
}
.animate-slide {
  animation: slideIn 0.5s ease-out;
}
```
