---
title: "[Solution] CSS Masonry Layout Not Supported — Fix Grid Masonry Fallback"
description: "Fix CSS masonry layout not supported with this step-by-step solution. Learn about grid masonry, Firefox experimental support, and JavaScript-based fallbacks."
---

## What This Error Means

The CSS masonry layout is not rendering correctly. Items that should fill gaps like a masonry or waterfall layout are displayed in a standard grid with empty spaces, or the layout collapses to a single column.

## Why It Happens

Pure CSS masonry layout is not yet a finalized specification. Firefox has experimental support behind the `layout.css.grid-template-masonry-value.enabled` flag, but Chrome and Safari do not support it. Using `grid-template-rows: masonry` in unsupported browsers causes the declaration to be ignored, and the grid falls back to standard row behavior.

The `masonry` value for `grid-template-rows` or `grid-template-columns` is part of the CSS Grid Level 3 specification but has not been implemented in most browsers. Relying on it in production causes layouts to break for the majority of users.

The most common workaround is using CSS columns, JavaScript-based masonry libraries, or flexbox with column direction. Each approach has tradeoffs in terms of item ordering and responsiveness.

## How to Fix It

Use CSS columns for a pure CSS masonry effect:

```css
.masonry {
  column-count: 3;
  column-gap: 1rem;
}

.masonry .item {
  break-inside: avoid;
  margin-bottom: 1rem;
}
```

Note that CSS columns fill top to bottom, then left to right, which differs from the typical left-to-right masonry order.

Use flexbox with column direction as an alternative:

```css
.masonry {
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  max-height: 1000px;
  gap: 1rem;
}

.masonry .item {
  flex: 1 1 200px;
}
```

For the experimental CSS masonry syntax with a fallback:

```css
.masonry {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}

@supports (grid-template-rows: masonry) {
  .masonry {
    grid-template-rows: masonry;
  }
}
```

Use a JavaScript library like Masonry.js or a CSS-based approach with `grid-row: span` for dynamic item heights:

```css
.masonry {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  grid-auto-rows: 10px;
  gap: 1rem;
}

.item-tall {
  grid-row: span 5;
}

.item-medium {
  grid-row: span 3;
}
```

## Common Mistakes

- Using `grid-template-rows: masonry` without checking browser support
- Not providing a fallback for browsers that ignore the masonry value
- Assuming CSS columns produce the same item ordering as JavaScript masonry
- Using a JavaScript library when CSS columns or grid span would suffice
- Not testing the layout with different content heights and screen sizes
- Ignoring the performance impact of JavaScript-based masonry on large item lists

## Related Pages

- [CSS Grid Not Working](/languages/css/css-grid-not-working/)
- [CSS Grid Auto Flow](/languages/css/css-grid-auto-flow/)
- [CSS Flexbox Wrap](/languages/css/css-flexbox-wrap/)
- [Flexbox Centering](/languages/css/flexbox-centering/)
- [CSS Container Queries](/languages/css/css-container-queries/)
