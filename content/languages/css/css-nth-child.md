---
title: "[Solution] CSS nth-child Selector Not Working — Fix Pseudo-class Targeting"
description: "Fix CSS nth-child selector not working with this step-by-step solution. Learn why nth-child does not match elements and how to debug selector logic."
---

## What This Error Means

The `:nth-child()` or `:nth-of-type()` selector is not matching the elements you expect. Styles are applied to the wrong elements, skipped entirely, or the selector appears to have no effect at all.

## Why It Happens

The `:nth-child()` selector counts all sibling elements regardless of type. If the first child is a `<div>` and you target `div:nth-child(2)`, the second child must also be a `<div>` to match. The index is based on position among all siblings, not among siblings of the same type.

`:nth-of-type()` counts only siblings of the same element type. The difference is critical. If you have mixed element types as children, `nth-child` and `nth-of-type` produce different results.

The selector also fails when elements are dynamically inserted or reordered by JavaScript. If the DOM changes after page load, the nth-child positions shift and previously targeted elements no longer match.

Another issue is specificity. A selector like `.list li:nth-child(3)` has higher specificity than `.list li`. If the nth-child rule comes before the base rule in the stylesheet, it may be overridden.

## How to Fix It

Use `:nth-of-type()` when you only want to target specific element types:

```css
/* Targets the 2nd child regardless of type */
li:nth-child(2) { color: red; }

/* Targets the 2nd <li> among all <li> siblings */
li:nth-of-type(2) { color: blue; }
```

Use formula notation for patterns:

```css
/* Every even row */
tr:nth-child(even) { background: #f5f5f5; }

/* Every 3rd item */
.item:nth-child(3n) { margin-top: 2rem; }

/* First 3 items */
.item:nth-child(-n+3) { font-weight: bold; }

/* All items after the 5th */
.item:nth-child(n+6) { opacity: 0.7; }
```

Combine with other selectors for precise targeting:

```css
/* First li inside a .list container */
.list li:first-child { border-top: 2px solid #333; }

/* Last li inside a .list container */
.list li:last-child { border-bottom: 2px solid #333; }
```

If elements are dynamically generated, re-check the DOM in DevTools to verify the actual element order matches your expected indices.

## Common Mistakes

- Confusing `nth-child` with `nth-of-type` when elements have mixed types
- Using `nth-child(1)` when `:first-child` is clearer and more readable
- Assuming the count starts at 0 when it starts at 1
- Not accounting for dynamically added elements that shift child indices
- Overriding nth-child styles with less specific selectors later in the cascade

## Related Pages

- [CSS Has Selector](/languages/css/css-has-selector/)
- [CSS Specificity Conflict](/languages/css/css-specificity-conflict/)
- [CSS Variable Scope](/languages/css/css-variable-scope/)
- [Flexbox Centering](/languages/css/flexbox-centering/)
- [CSS Focus Visible](/languages/css/css-focus-visible/)
