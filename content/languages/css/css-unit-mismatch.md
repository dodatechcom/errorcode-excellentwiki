---
title: "[Solution] CSS Unit Mismatch — Fix Layout Shifts from Mixed Units"
description: "Fix CSS unit mismatches with this step-by-step solution. Learn why mixing px, rem, em, and vh causes layout shifts and how to use units consistently."
---

## What This Error Means

Your layout shifts unexpectedly when the viewport resizes, the user changes font size, or elements are nested inside differently-sized parents. Widths, heights, paddings, and margins are inconsistent across components because different CSS units produce different results in the same context.

## Why It Happens

CSS has several unit types and they behave differently. `px` is always a fixed pixel value. `rem` is relative to the root element font size. `em` is relative to the parent element font size. `vh` and `vw` are relative to the viewport dimensions.

When you mix these units, calculations become unpredictable. A container with `width: 300px` and a child with `width: 50%` expects the parent to have a fixed width. But if the parent uses `max-width: 30rem` and the root font size changes, the percentage calculation shifts.

`em` units compound inside nested elements. If a parent has `font-size: 1.2em` and a child also has `font-size: 1.2em`, the child is actually `1.44em` relative to the root. This cascading multiplication causes text and spacing to grow rapidly in deep nesting.

Viewport units like `vh` and `vw` change with the browser window size. A header with `height: 100vh` will be much taller on a phone than on a desktop monitor. This causes layout shifts when content reflows during resize.

## How to Fix It

Establish a consistent unit system for your project. The most common approach is to use `rem` for spacing and typography and `px` for borders and small fixed values:

```css
:root {
  font-size: 16px;
}

body {
  font-size: 1rem;
  line-height: 1.5;
}

.container {
  max-width: 72rem;
  padding: 2rem;
}

.heading {
  font-size: 2rem;
  margin-bottom: 1rem;
}

.border {
  border: 1px solid #ccc;
}
```

Use `calc()` to safely mix units when necessary:

```css
.sidebar {
  width: calc(100% - 300px);
}
```

Avoid compounding `em` units by using `rem` for font sizes instead:

```css
/* Avoid this */
.parent { font-size: 1.2em; }
.child { font-size: 1.2em; } /* Actually 1.44rem */

/* Prefer this */
.parent { font-size: 1.2rem; }
.child { font-size: 1.2rem; } /* Exactly 1.2rem */
```

For viewport-relative sizing that avoids address bar issues on mobile, use `dvh` (dynamic viewport height) instead of `vh`:

```css
.hero {
  min-height: 100dvh;
}
```

## Common Mistakes

- Using `em` for font sizes in nested elements which compounds unexpectedly
- Mixing `px` and `rem` without a clear convention for which properties use which unit
- Using `vh` on mobile where the browser address bar changes the viewport height
- Not setting a base `font-size` on `:root` which makes `rem` unreliable
- Using percentage widths without a fixed-width parent to reference
- Forgetting that `rem` does not account for parent context and always references root

## Related Pages

- [CSS Grid Not Working](/languages/css/css-grid-not-working/)
- [Media Query Not Applying](/languages/css/media-query-not-applying/)
- [Flexbox Centering](/languages/css/flexbox-centering/)
- [CSS Container Queries](/languages/css/css-container-queries/)
- [Dark Mode Media Query](/languages/css/dark-mode-media-query/)
