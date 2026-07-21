---
title: "[Solution] CSS Counter Error"
description: "CSS counter not incrementing."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Counter Error

CSS counter not incrementing.

### Common Causes
Missing counter-reset; wrong increment

### How to Fix
```css
ol { counter-reset: item; }
li::before { counter-increment: item; content: counter(item) ". "; }
```

### Examples
```css
ol {
  counter-reset: section;
  list-style-type: none;
}
li::before {
  counter-increment: section;
  content: section ". ";
  font-weight: bold;
}
```
