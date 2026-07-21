---
title: "[Solution] CSS Scroll Snap Error"
description: "Scroll snap not working."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Scroll Snap Error

Scroll snap not working.

### Common Causes
Missing overflow; wrong snap type

### How to Fix
```css
.container {
  overflow-x: scroll;
  scroll-snap-type: x mandatory;
}
.item {
  scroll-snap-align: start;
}
```

### Examples
```css
.carousel {
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
}
.slide {
  scroll-snap-align: center;
  min-width: 100%;
}
```
