---
title: "[Solution] CSS :has() Selector Not Working — Fix Browser Support"
description: "Fix CSS :has() selector not working with this step-by-step solution. Learn about browser compatibility, fallback strategies, and parent selection alternatives."
---

## What This Error Means

The CSS `:has()` selector is not matching elements or is causing styles to fail in certain browsers. You are trying to select a parent based on its children or apply conditional styles based on the presence of specific descendants, but the selector does not work.

## Why It Happens

The `:has()` selector is a relatively new addition to CSS. Chrome and Edge added support in version 105, Safari in version 15.4, and Firefox in version 121. Browsers older than these versions do not recognize `:has()` at all and will skip the entire rule containing it.

When a browser encounters an unknown pseudo-class, it drops the entire CSS rule. This means if you have other valid properties in the same rule, they are also discarded. The fallback is not partial application but complete rule removal.

The `:has()` selector also has performance implications. It is sometimes called the "parent selector" but it actually performs a descendant check, which requires the browser to evaluate the entire subtree. Complex `:has()` selectors with multiple conditions can cause layout performance issues on large DOM trees.

Another issue is specificity. The `:has()` selector adds to the specificity of the rule. A selector like `.card:has(.featured)` has the specificity of a class plus a pseudo-class, which may conflict with existing specificity calculations in your stylesheet.

## How to Fix It

Check browser support before using `:has()` in production. If you need to support older browsers, provide a fallback:

```css
/* Fallback for browsers without :has() support */
.card {
  padding: 1rem;
}

/* Enhanced for browsers that support :has() */
.card:has(.badge) {
  padding: 1.5rem;
  border-left: 4px solid #3498db;
}
```

Use feature detection in JavaScript if you need a JavaScript fallback:

```css
@supports selector(:has(*)) {
  .sidebar:has(.active) {
    background-color: #f0f0f0;
  }
}
```

Keep `:has()` selectors as simple as possible for performance:

```css
/* Good - simple check */
.form:has(.error) { border-color: red; }

/* Avoid - complex nested checks */
.page:has(.sidebar) > .content > .article:has(.highlight) { ... }
```

For parent selection that only needs to target the immediate parent based on a child class, consider adding a class to the parent via JavaScript instead of relying on `:has()`.

## Common Mistakes

- Using `:has()` without considering older browsers that will skip the entire rule
- Writing complex `:has()` selectors with multiple nested conditions that hurt performance
- Not testing in Firefox prior to version 121 which had delayed support
- Assuming `:has()` works like jQuery's `.parent()` selector when it is actually a descendant check
- Forgetting that `:has()` adds specificity which can override more specific selectors unexpectedly
- Using `:has()` for critical layout when a simpler class-based approach is more reliable

## Related Pages

- [CSS Container Queries](/languages/css/css-container-queries/)
- [CSS Variable Scope](/languages/css/css-variable-scope/)
- [Media Query Not Applying](/languages/css/media-query-not-applying/)
- [Dark Mode Media Query](/languages/css/dark-mode-media-query/)
- [CSS Specificity Conflict](/languages/css/css-specificity-conflict/)
