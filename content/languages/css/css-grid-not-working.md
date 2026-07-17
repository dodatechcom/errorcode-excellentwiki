---
title: "[Solution] CSS Grid Not Working — Fix Layout Issues"
description: "Fix CSS grid not working with this step-by-step solution. Learn about display property, implicit tracks, and browser compatibility issues."
---

## What This Error Means

Your CSS Grid layout is not rendering as expected. Items may be stacked vertically, overflowing their container, or ignoring the defined columns and rows. The grid is either not being applied at all or producing unexpected visual results.

## Why It Happens

The most common cause is forgetting to set `display: grid` or `display: inline-grid` on the container element. Without this property, the browser treats the element as a regular block container and ignores all grid-related properties on children.

Another frequent issue is missing `grid-template-columns` or `grid-template-rows`. A grid container with no explicit track definitions will place all items into a single column, which looks identical to normal block layout.

Child elements may also fail to participate in the grid if they are not direct children. CSS Grid only works on direct descendants of the grid container. If your items are wrapped in extra `<div>` elements, they will not be placed into grid cells.

Finally, a typo in property names such as `grid-template-colums` instead of `grid-template-columns` will silently fail because the browser ignores unrecognized properties.

## How to Fix It

Make sure the container has `display: grid` and at least one track definition:

```css
.container {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 1rem;
}
```

If you need items to auto-fill available space, use `auto-fit` or `auto-fill`:

```css
.container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
}
```

Ensure grid items are direct children of the grid container. Remove wrapper elements or target them explicitly:

```html
<div class="container">
  <div class="item">One</div>
  <div class="item">Two</div>
  <div class="item">Three</div>
</div>
```

Use browser DevTools to inspect the element. Under the Computed or Layout panel you can see whether `display: grid` is actually applied and check for any overridden values.

## Common Mistakes

- Forgetting `display: grid` on the parent container entirely
- Targeting wrapped children instead of direct descendants of the grid
- Using `repeat(3, 1fr)` when you need `auto-fit` for responsive behavior
- Mixing grid properties with `float` which can cause conflicts
- Assuming `grid-gap` works in older browsers when the modern syntax is `gap`
- Not setting a height on the container when using `grid-template-rows`

## Related Pages

- [Flexbox Centering](/languages/css/flexbox-centering/)
- [CSS Unit Mismatch](/languages/css/css-unit-mismatch/)
- [Media Query Not Applying](/languages/css/media-query-not-applying/)
- [CSS Specificity Conflict](/languages/css/css-specificity-conflict/)
- [Overflow Hidden Bleed](/languages/css/overflow-hidden-bleed/)
