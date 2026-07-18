---
title: "[Solution] CSS Position Sticky Not Working — Fix Sticky Element"
description: "Fix CSS position sticky not working with this step-by-step solution. Learn why sticky elements scroll away and how to configure the sticky positioning."
---

## What This Error Means

You set `position: sticky` on an element but it behaves like `position: relative` and scrolls away with the page. The element never sticks to the viewport edge as expected.

## Why It Happens

`position: sticky` requires both a `top`, `bottom`, `left`, or `right` value and a scrolling ancestor that is not `overflow: hidden`, `overflow: scroll` (on the axis), or `overflow: auto` with clipping behavior. If any ancestor has `overflow: hidden` or `overflow: auto`, the sticky element sticks within that ancestor instead of the viewport.

The most common cause is an ancestor with `overflow: hidden` or `overflow: auto`. This creates a new scroll context. The sticky element sticks relative to the nearest scrolling ancestor, not the viewport. If that ancestor is smaller than the viewport, the sticky effect is invisible.

Another issue is that the sticky element must have a defined `top` or `bottom` value. Without it, the element has nothing to stick to and defaults to relative positioning.

The parent container must also be taller than the sticky element. If the parent and child are the same height, there is no room for the element to scroll and then stick.

## How to Fix It

Add a `top` or `bottom` value to the sticky element:

```css
.navbar {
  position: sticky;
  top: 0;
  z-index: 100;
}
```

Check ancestors for `overflow` properties that break sticky:

```css
/* This breaks sticky on all descendants */
.parent {
  overflow: hidden; /* Remove this */
}

/* This is fine */
.parent {
  overflow: visible;
}
```

Ensure the sticky element's parent has enough height to scroll through:

```html
<div class="scroll-container" style="height: 2000px;">
  <div class="sticky-header" style="position: sticky; top: 0;">
    I stick here
  </div>
  <p>Scrolling content...</p>
</div>
```

If you need a sticky sidebar, verify no ancestor constrains the overflow:

```css
.sidebar {
  position: sticky;
  top: 1rem;
}

/* Check each ancestor up to the scrolling container */
.page-wrapper {
  overflow: visible; /* Must not clip the sidebar */
}
```

## Common Mistakes

- Not providing a `top` or `bottom` value for the sticky element
- Having `overflow: hidden` or `overflow: auto` on a parent that creates a scroll context
- The parent container is the same height as the sticky child, leaving no scroll room
- Using sticky inside a table element where `overflow` does not apply
- Forgetting `z-index` which causes the sticky element to be covered by other content
- Assuming sticky works inside an iframe without checking the iframe scroll context

## Related Pages

- [Position Absolute Viewport](/languages/css/position-absolute-viewport/)
- [Overflow Hidden Bleed](/languages/css/overflow-hidden-bleed/)
- [CSS Scroll Snap](/languages/css/css-scroll-snap/)
- [CSS Grid Not Working](/languages/css/css-grid-not-working/)
- [Z-Index Not Working](/languages/css/z-index-not-working/)
