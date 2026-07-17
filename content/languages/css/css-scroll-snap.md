---
title: "[Solution] CSS Scroll Snap Not Working — Fix Snap Behavior"
description: "Fix CSS scroll snap not working with this step-by-step solution. Learn about scroll-snap-type, snap alignment, and why scrolling does not snap to elements."
---

## What This Error Means

You enabled CSS scroll snap on a container but scrolling does not snap to elements. The content scrolls freely past snap points and never aligns to the intended positions. The snap behavior appears to be completely disabled.

## Why It Happens

Scroll snap requires both a snap container (the scrollable parent) and snap children (the items that align to snap points). If either is missing the correct properties, snapping will not work.

The most common mistake is setting `scroll-snap-type` on the scroll container but not setting `scroll-snap-align` on the children. Without `scroll-snap-align` on the items, there are no snap points defined and the container has nothing to snap to.

Another issue is that the container must actually be scrollable. If the container has `overflow: hidden` instead of `overflow: auto` or `overflow: scroll`, there is no scroll action to snap. Similarly, if all content fits within the container without overflowing, snapping has nothing to do.

The `scroll-snap-type` value matters. Using `mandatory` forces snapping to exact points which can feel jarring if content does not perfectly fill the viewport. Using `proximity` is more forgiving and snaps only when the scroll position is close to a snap point.

Height and sizing issues can also prevent snapping. If the snap children do not fill the container or have different heights, the snap alignment becomes inconsistent and may not behave as expected.

## How to Fix It

Set `scroll-snap-type` on the container and `scroll-snap-align` on each child:

```css
.carousel {
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  gap: 1rem;
}

.carousel-item {
  flex: 0 0 100%;
  scroll-snap-align: start;
}
```

For a vertical snap container:

```css
.snap-container {
  height: 100vh;
  overflow-y: scroll;
  scroll-snap-type: y mandatory;
}

.snap-section {
  height: 100vh;
  scroll-snap-align: start;
}
```

Use `proximity` for a more natural feel when content does not perfectly fill the viewport:

```css
.scroll-area {
  overflow-y: auto;
  scroll-snap-type: y proximity;
}

.scroll-item {
  min-height: 300px;
  scroll-snap-align: center;
}
```

Remove `overflow: hidden` from the snap container and use `auto` or `scroll` instead. Also ensure the container has a defined height or max-height so it can actually overflow.

For horizontally scrolling galleries, use `scroll-padding` on the container to account for margins or padding on the snap items:

```css
.gallery {
  scroll-snap-type: x mandatory;
  scroll-padding: 0 1rem;
}
```

## Common Mistakes

- Setting `scroll-snap-type` on the container but forgetting `scroll-snap-align` on children
- Using `overflow: hidden` on the snap container which prevents scrolling entirely
- Not giving the container a defined height so it cannot overflow
- Using `mandatory` snap which feels broken when content does not perfectly fill the viewport
- Forgetting that `scroll-snap-align` values of `start`, `center`, and `end` produce very different results
- Not accounting for padding and margins which shift the snap point alignment

## Related Pages

- [Overflow Hidden Bleed](/languages/css/overflow-hidden-bleed/)
- [CSS Unit Mismatch](/languages/css/css-unit-mismatch/)
- [CSS Transition Not Working](/languages/css/css-transition-not-working/)
- [Media Query Not Applying](/languages/css/media-query-not-applying/)
- [CSS Backdrop Filter](/languages/css/css-backdrop-filter/)
