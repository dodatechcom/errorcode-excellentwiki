---
title: "[Solution] CSS Grid Auto-Flow Not Placing Items — Fix grid-auto-flow"
description: "Fix CSS grid-auto-flow not placing items correctly with this step-by-step solution. Learn why grid items end up in wrong cells and how auto-flow works."
---

## What This Error Means

Your CSS Grid items are not being placed in the expected cells. Items may stack vertically when you expect horizontal placement, skip cells, or overlap because `grid-auto-flow` is not directing them where you intend.

## Why It Happens

`grid-auto-flow` controls how auto-placed grid items fill unoccupied cells. The default value is `row`, which places items left to right, then wraps to the next row. If you have a tall grid and expect items to fill columns first, the default `row` flow is the cause.

The `dense` packing algorithm fills gaps left by larger items, but it can reorder items out of source order. This causes accessibility issues because the visual order differs from the DOM order, which screen readers follow.

Grid items with explicit `grid-column` or `grid-row` placements are not affected by `grid-auto-flow`. If some items have explicit positions and others do not, the auto-placed items may collide with the explicitly placed ones.

## How to Fix It

Set `grid-auto-flow: column` to fill vertically first:

```css
.container {
  display: grid;
  grid-auto-flow: column;
  grid-template-rows: repeat(3, 100px);
}
```

Use `dense` packing to fill gaps, but be cautious with accessibility:

```css
.container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  grid-auto-flow: dense;
}
```

Combine auto-flow with explicit tracks for predictable placement:

```css
.container {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: 100px;
  grid-auto-flow: row;
}
```

For complex layouts, use explicit placement instead of relying on auto-flow:

```css
.item-a {
  grid-column: 1 / 3;
  grid-row: 1 / 2;
}

.item-b {
  grid-column: 3 / 4;
  grid-row: 1 / 3;
}
```

Verify that items do not have conflicting explicit placements that block auto-placed items from filling available cells.

## Common Mistakes

- Using `grid-auto-flow: dense` without realizing it reorders items for visual layout
- Not defining `grid-template-rows` when using column flow, causing items to stretch
- Mixing explicit and auto placements without accounting for cell collisions
- Assuming auto-flow places items in reverse order when it follows source order
- Forgetting that `grid-auto-flow: row dense` fills row gaps but not column gaps

## Related Pages

- [CSS Grid Not Working](/languages/css/css-grid-not-working/)
- [CSS Flexbox Wrap](/languages/css/css-flexbox-wrap/)
- [Flexbox Centering](/languages/css/flexbox-centering/)
- [CSS Masonry Layout](/languages/css/css-masonry-layout/)
- [CSS Container Queries](/languages/css/css-container-queries/)
