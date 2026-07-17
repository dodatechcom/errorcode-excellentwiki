---
title: "[Solution] Flexbox Centering Not Working — Fix Alignment Issues"
description: "Fix flexbox centering not working with this step-by-step solution. Learn about justify-content, align-items, and common alignment mistakes."
---

## What This Error Means

You are trying to center an element inside a flex container but the child remains stuck to the top-left corner or only centers along one axis. The content is not centered both horizontally and vertically as expected.

## Why It Happens

Flexbox centering requires setting alignment properties on the **parent** container, not the child element. A common mistake is applying `justify-content` or `align-items` to the child, which has no effect on centering.

By default, flex items stretch along the cross axis. This means `align-items` defaults to `stretch` rather than `center`, so vertical centering does not happen automatically. You must explicitly set it.

Another issue is that the flex container needs a defined height. If the container has no height and its content is minimal, there is nothing to center vertically because the container collapses to the content size. The centering is technically working but the container is exactly as tall as its child.

The parent also needs `display: flex` or `display: inline-flex`. Without this, the alignment properties are ignored entirely.

## How to Fix It

To center an element both horizontally and vertically:

```css
.parent {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}
```

Setting `min-height: 100vh` gives the container enough space for vertical centering to be visible. You can also use a specific height like `height: 400px`.

If you only need horizontal centering:

```css
.parent {
  display: flex;
  justify-content: center;
}
```

For vertical centering only:

```css
.parent {
  display: flex;
  align-items: center;
  min-height: 100vh;
}
```

To center a flex item that also has text inside, remember that `text-align` handles inline content while flex alignment handles the flex item box itself.

## Common Mistakes

- Applying centering properties to the child instead of the parent
- Forgetting to set `display: flex` on the parent container
- Not giving the parent a height or min-height so vertical centering has no space to work
- Assuming `margin: 0 auto` works on flex children in all cases
- Using `align-content` instead of `align-items` for single-line flex containers
- Mixing `float` on the child which removes it from normal flex flow

## Related Pages

- [CSS Grid Not Working](/languages/css/css-grid-not-working/)
- [Position Absolute Viewport](/languages/css/position-absolute-viewport/)
- [CSS Specificity Conflict](/languages/css/css-specificity-conflict/)
- [CSS Unit Mismatch](/languages/css/css-unit-mismatch/)
- [CSS Transition Not Working](/languages/css/css-transition-not-working/)
