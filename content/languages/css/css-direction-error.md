---
title: "[Solution] CSS Direction Error"
description: "RTL/LTR direction issues."
languages: ["css"]
error-types: ["language-error"]
severities: ["error"]
---

# CSS Direction Error

RTL/LTR direction issues.

### Common Causes
Missing direction; logical properties

### How to Fix
```css
direction: rtl;
unicode-bidi: bidi-override;
```

### Examples
```css
[dir="rtl"] .container {
  text-align: right;
}
```
