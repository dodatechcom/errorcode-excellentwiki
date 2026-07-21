---
title: "[Solution] CSS Text Transform Error"
description: "Text-transform not applying."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Text Transform Error

Text-transform not applying.

### Common Causes
Wrong value; inline elements

### How to Fix
```css
text-transform: uppercase;
text-transform: lowercase;
text-transform: capitalize;
```

### Examples
```css
.heading {
  text-transform: uppercase;
  letter-spacing: 0.1em;
}
```
