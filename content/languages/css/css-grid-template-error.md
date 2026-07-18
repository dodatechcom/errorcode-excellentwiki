---
title: "[Solution] CSS Grid Template Areas Not Matching — Layout Broken"
description: "Fix CSS grid-template-areas errors when areas don't match. Learn about grid area naming, implicit tracks, and template syntax."
---

## What This Error Means

Your `grid-template-areas` layout is not rendering correctly. Items may be missing, overlapping, or placed in unexpected positions. The grid container has named areas defined, but the visual result does not match the intended layout.

## Why It Happens

The most common cause is a mismatch between the `grid-template-areas` string and the actual grid items. If a named area is referenced in the template but no child has that `grid-area` name, the area appears empty.

Another frequent cause is incorrect string formatting in `grid-template-areas`. Each row must have the same number of names, and periods (`.`) represent empty cells. Missing periods or extra names cause the template to be invalid.

Child elements with `grid-area` names that do not match any area in the template are placed automatically by the grid algorithm, which may not be the intended position.

Multiple rows in the template must have consistent column counts. If one row has 3 names and another has 4, the template is invalid and the grid falls back to implicit placement.

Finally, combining `grid-template-areas` with `grid-template-columns` or `grid-template-rows` can cause conflicts if the sizes do not match the template layout.

## How to Fix It

### Ensure grid-area names match the template

```css
.container {
  display: grid;
  grid-template-areas:
    "header header"
    "sidebar main"
    "footer footer";
  grid-template-columns: 200px 1fr;
  grid-template-rows: auto 1fr auto;
}

.header  { grid-area: header; }
.sidebar { grid-area: sidebar; }
.main    { grid-area: main; }
.footer  { grid-area: footer; }
```

### Use periods for empty cells

```css
.container {
  display: grid;
  grid-template-areas:
    "header  header  header"
    "sidebar .       main"
    "footer  footer  footer";
}
```

### Verify column count matches across rows

```css
/* Wrong — inconsistent column count */
grid-template-areas:
  "a b c"
  "a b";  /* Only 2 columns */

/* Correct — same count */
grid-template-areas:
  "a b c"
  "a b c";
```

### Use grid-area shorthand for placement

```css
.item {
  grid-area: 1 / 1 / 2 / 3;  /* row-start / col-start / row-end / col-end */
}
```

### Check browser DevTools for grid overlay

```css
/* Enable grid overlay in DevTools */
.container {
  outline: 2px solid red;  /* Temporary debug aid */
}
```

## Common Mistakes

- Misspelling grid-area names between the template and child elements
- Having different numbers of column names in different rows
- Not using periods for intentionally empty cells
- Forgetting to set `display: grid` on the container
- Mixing grid-template-areas with explicit grid placement on children

## Related Pages

- [CSS Grid Not Working](/languages/css/css-grid-not-working/)
- [CSS Flexbox Centering](/languages/css/flexbox-centering/)
- [CSS Unit Mismatch](/languages/css/css-unit-mismatch/)
