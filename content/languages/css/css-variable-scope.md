---
title: "[Solution] CSS Custom Properties Not Inherited — Fix Variable Scope"
description: "Fix CSS custom properties not inherited with this step-by-step solution. Learn about variable scope, fallback values, and cascade rules."
---

## What This Error Means

CSS custom properties (variables) defined on a parent element are not available to child elements. When you reference a variable with `var()` on a descendant, it resolves to the initial value or fallback instead of the value you defined.

## Why It Happens

CSS custom properties follow the cascade and inheritance model. When you define a variable on an element using `--my-color: red`, it is scoped to that element and inherited by its descendants. However, if you redefine the variable on an ancestor with a different value, or if the variable is defined in a selector that does not match, the child will fall back to the default.

A frequent mistake is defining variables inside a media query or a class that is not currently active. For example, if you define `--primary-color` inside `.dark-theme` but the dark theme class is not applied, the variable is undefined and children will use the fallback.

Another common issue is placing variable definitions on a pseudo-element like `::before` or `::after`. Variables defined there are not inherited by actual child elements because pseudo-elements are not ancestors in the DOM.

## How to Fix It

Define variables on a high-level selector so they cascade to all descendants. The `:root` pseudo-class is ideal for global variables:

```css
:root {
  --primary-color: #3498db;
  --spacing: 1rem;
  --font-size: 16px;
}
```

If you need scoped variables, define them on the container element directly:

```css
.card {
  --card-bg: #ffffff;
  --card-padding: 1.5rem;
  background-color: var(--card-bg);
  padding: var(--card-padding);
}
```

Always provide a fallback value in case the variable is not defined:

```css
.element {
  color: var(--primary-color, #333333);
}
```

Check for typos. A variable named `--priamry-color` in the definition and `--primary-color` in usage will not match and the fallback will be used.

## Common Mistakes

- Defining variables inside media queries that are not currently active
- Placing variable definitions on pseudo-elements instead of the actual element
- Typos in variable names between definition and usage
- Expecting variables to cross shadow DOM boundaries
- Overriding variables in nested selectors and expecting children to use the original
- Forgetting that custom properties are case-sensitive (`--Color` and `--color` are different)

## Related Pages

- [CSS Specificity Conflict](/languages/css/css-specificity-conflict/)
- [Dark Mode Media Query](/languages/css/dark-mode-media-query/)
- [CSS Container Queries](/languages/css/css-container-queries/)
- [Media Query Not Applying](/languages/css/media-query-not-applying/)
- [CSS Has Selector](/languages/css/css-has-selector/)
