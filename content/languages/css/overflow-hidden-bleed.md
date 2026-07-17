---
title: "[Solution] Overflow Hidden Not Containing Children — Fix Overflow Bleed"
description: "Fix overflow hidden not working with this step-by-step solution. Learn about block formatting context, containing blocks, and clipping edge cases."
---

## What This Error Means

You set `overflow: hidden` on a parent element but its children still overflow and become visible outside the parent boundaries. The parent is not clipping its content as expected.

## Why It Happens

`overflow: hidden` creates a new block formatting context which should clip children. However, there are several cases where it fails to contain content.

Absolutely positioned children are not clipped by `overflow: hidden` on a normal (static) positioned parent. An absolutely positioned element is placed relative to its nearest positioned ancestor. If the overflow parent does not have `position: relative` or another positioned value, the absolutely positioned child escapes the overflow clipping.

Fixed positioned elements are never clipped by any parent's overflow. They are always relative to the viewport and exist outside the normal document flow.

Another issue is that `overflow: hidden` only clips content in the block formatting context. If the parent has `display: inline`, overflow clipping does not apply. Inline elements do not create a block formatting context.

Finally, `overflow: hidden` does not prevent content from overflowing in the z-direction. If a child has a higher z-index or is in a different stacking context, it may appear above the parent's clipping boundary.

## How to Fix It

Add `position: relative` to the overflow parent so absolutely positioned children are contained:

```css
.parent {
  position: relative;
  overflow: hidden;
  width: 300px;
  height: 200px;
}

.child {
  position: absolute;
  top: -20px;
  left: -20px;
}
```

Ensure the parent has `display: block` or `display: flex` rather than `display: inline`:

```css
.parent {
  display: block;
  overflow: hidden;
  max-width: 100%;
}
```

For content that must be clipped in all directions including z-axis, use `isolation: isolate` to create a new stacking context:

```css
.parent {
  overflow: hidden;
  isolation: isolate;
}
```

If you need to clip rounded corners, make sure the parent has `border-radius` applied. The overflow clipping respects the border-radius on the parent element:

```css
.parent {
  overflow: hidden;
  border-radius: 12px;
  position: relative;
}
```

## Common Mistakes

- Forgetting `position: relative` on the overflow parent when children are absolutely positioned
- Using `overflow: hidden` on inline elements which do not create a block formatting context
- Expecting `overflow: hidden` to clip fixed positioned children
- Not creating a stacking context when z-axis clipping is needed
- Using `overflow: hidden` to prevent scrolling when `overflow: clip` is more appropriate
- Applying `overflow: hidden` to a flex container without accounting for flex item sizing

## Related Pages

- [Position Absolute Viewport](/languages/css/position-absolute-viewport/)
- [Z-Index Not Working](/languages/css/z-index-not-working/)
- [CSS Grid Not Working](/languages/css/css-grid-not-working/)
- [CSS Backdrop Filter](/languages/css/css-backdrop-filter/)
- [CSS Scroll Snap](/languages/css/css-scroll-snap/)
