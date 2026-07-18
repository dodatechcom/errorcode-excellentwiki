---
title: "[Solution] CSS Float Not Clearing Properly — Fix Layout Breaks"
description: "Fix CSS float not clearing with this step-by-step solution. Learn about clear property, clearfix techniques, and how to prevent container collapse."
---

## What This Error Means

Your floated elements are overflowing their parent container or causing subsequent elements to wrap incorrectly. The parent container has collapsed to zero height because it does not account for the floated children inside it.

## Why It Happens

Floated elements are removed from the normal document flow. The parent container only computes its height based on non-floated content. When all children are floated, the parent collapses to zero height, which breaks background colors, borders, and the layout of elements that follow.

The `clear` property prevents an element from sitting beside a floated element. If you forget to apply it, elements below the float will slide up and overlap. Additionally, `overflow: hidden` on a parent creates a new Block Formatting Context, which indirectly contains floats, but it also clips content that extends beyond the box.

The modern solution is the clearfix hack using a pseudo-element. Older approaches like empty divs with `clear: both` are fragile and add unnecessary markup.

## How to Fix It

Use the clearfix pattern on the parent container:

```css
.clearfix::after {
  content: "";
  display: table;
  clear: both;
}
```

Apply it to any container with floated children:

```html
<div class="clearfix">
  <div style="float: left; width: 50%;">Left column</div>
  <div style="float: right; width: 50%;">Right column</div>
</div>
<p>This paragraph is no longer overlapping.</p>
```

You can also use `overflow: hidden` on the parent for a simpler fix, though it clips overflowing content:

```css
.container {
  overflow: hidden;
}
```

For flexbox-based layouts, floats are unnecessary. Replace them entirely:

```css
.container {
  display: flex;
  gap: 1rem;
}
```

If you must use floats and need an element to clear a specific side, use the `clear` property:

```css
.footer {
  clear: both;
}
```

## Common Mistakes

- Forgetting clearfix on a container where all children are floated
- Using `overflow: hidden` on a parent when content needs to overflow visibly
- Not accounting for floats inside responsive breakpoints that change float directions
- Mixing floats with flexbox or grid, causing conflicting layout behavior
- Using empty `<div class="clear"></div>` elements instead of pseudo-element clearfix

## Related Pages

- [Flexbox Centering](/languages/css/flexbox-centering/)
- [CSS Grid Not Working](/languages/css/css-grid-not-working/)
- [Position Absolute Viewport](/languages/css/position-absolute-viewport/)
- [Overflow Hidden Bleed](/languages/css/overflow-hidden-bleed/)
- [CSS Unit Mismatch](/languages/css/css-unit-mismatch/)
