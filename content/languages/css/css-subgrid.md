---
title: "[Solution] CSS Subgrid Not Working in Firefox"
description: "Fix CSS subgrid not rendering in Firefox or other browsers. Learn about subgrid support, grid alignment, and fallback layouts."
---

## What This Error Means

Your `grid-template-columns: subgrid` or `grid-template-rows: subgrid` is not working. The nested grid items are not aligning with the parent grid tracks as expected.

## Why It Happens

The most common cause is browser compatibility. `subgrid` is supported in Firefox 71+ and Chrome 117+, but not in older versions. Safari added support in 16.0.

Another frequent cause is using `subgrid` on the wrong axis. `subgrid` must be applied to either columns, rows, or both. If you apply it to the wrong axis, the alignment does not work.

The parent grid must have explicit tracks for subgrid to reference. If the parent uses `grid-template-columns: repeat(auto-fill, minmax(200px, 1fr))`, the subgrid may not have predictable tracks to follow.

Nested grids that are not direct children of the grid container do not participate in subgrid. Only direct children can use `subgrid`.

Finally, the subgrid element must itself be a grid container with `display: grid`.

## How to Fix It

### Use subgrid on direct children only

```css
.parent-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}

.child-grid {
  display: grid;
  grid-template-columns: subgrid;
  grid-column: span 3;
}
```

### Apply subgrid to the correct axis

```css
/* Subgrid on columns */
.child-grid {
  display: grid;
  grid-template-columns: subgrid;
  grid-column: 1 / -1;
}

/* Subgrid on both axes */
.child-grid {
  display: grid;
  grid-template-columns: subgrid;
  grid-template-rows: subgrid;
  grid-column: 1 / -1;
  grid-row: 1 / -1;
}
```

### Provide fallback for older browsers

```css
.child-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}

@supports (grid-template-columns: subgrid) {
  .child-grid {
    grid-template-columns: subgrid;
  }
}
```

### Use grid span for the child

```css
.child-grid {
  display: grid;
  grid-template-columns: subgrid;
  grid-column: span 3;  /* Match parent column span */
}
```

### Check caniuse.com for current support

```css
/* Use progressive enhancement */
.child-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}

@supports (grid-template-columns: subgrid) {
  .child-grid {
    grid-template-columns: subgrid;
  }
}
```

## Common Mistakes

- Not checking browser support before using subgrid
- Applying subgrid to elements that are not direct grid children
- Not spanning the full width of the parent grid
- Using subgrid on the wrong axis
- Not providing a fallback for browsers without support

## Related Pages

- [CSS Grid Not Working](/languages/css/css-grid-not-working/)
- [CSS Grid Template Error](/languages/css/css-grid-template-error/)
- [CSS Flexbox Centering](/languages/css/flexbox-centering/)
