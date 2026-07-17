---
title: "[Solution] Z-Index Not Working — Fix Stacking Context Issues"
description: "Fix z-index not working with this step-by-step solution. Learn about stacking contexts, layering rules, and why higher z-index values get hidden."
---

## What This Error Means

You set a high `z-index` value on an element but it still appears behind another element with a lower `z-index`. Increasing the value has no effect. The element refuses to layer on top as expected.

## Why It Happens

`z-index` only works on positioned elements (`position: relative`, `absolute`, `fixed`, or `sticky`) or flex/grid children. If the element has `position: static` (the default), `z-index` is ignored completely.

The deeper issue is **stacking contexts**. Certain CSS properties create a new stacking context on an element, and all descendants are contained within it. These properties include `opacity` values less than 1, `transform`, `filter`, `will-change`, and `position` with z-index on the same element. Once a stacking context is formed, no descendant can escape it. A `z-index: 9999` inside a stacking context with `z-index: 1` will still appear below an element with `z-index: 2` in the parent stacking context.

This is why a modal with a very high z-index can appear behind a tooltip. If the modal is inside a container that creates a stacking context, the entire modal is trapped at the container's level in the parent stacking order.

## How to Fix It

First ensure the element has a positioned value:

```css
.overlay {
  position: relative;
  z-index: 10;
}
```

Or for elements that need to be on top of everything:

```css
.modal {
  position: fixed;
  z-index: 9999;
}
```

Check the ancestor chain for stacking context triggers. Remove unnecessary `opacity`, `transform`, or `will-change` from parent elements if they are accidentally creating stacking contexts:

```css
/* This creates a stacking context on .wrapper */
.wrapper {
  transform: translateZ(0);
  z-index: 1;
}
```

Use DevTools to inspect the computed stacking order. In the Layers or 3D View panel you can see which stacking contexts exist and how elements are layered within them.

If you need an element to always appear on top, place it as a direct child of `<body>` to minimize stacking context traps.

## Common Mistakes

- Setting `z-index` without `position: relative` or another positioned value
- Not realizing `opacity` below 1 creates a stacking context on the parent
- Assuming `z-index: 9999` will always be on top regardless of stacking contexts
- Using `transform` or `filter` on a parent which traps all descendants
- Forgetting that `position: sticky` also creates a stacking context
- Creating deeply nested stacking contexts that prevent children from reaching the top

## Related Pages

- [Position Absolute Viewport](/languages/css/position-absolute-viewport/)
- [CSS Backdrop Filter](/languages/css/css-backdrop-filter/)
- [CSS Specificity Conflict](/languages/css/css-specificity-conflict/)
- [Overflow Hidden Bleed](/languages/css/overflow-hidden-bleed/)
- [CSS Container Queries](/languages/css/css-container-queries/)
