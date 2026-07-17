---
title: "[Solution] CSS Backdrop Filter Not Working — Fix Frosted Glass Effect"
description: "Fix backdrop-filter not working with this step-by-step solution. Learn about browser support, fallback strategies, and why the blur effect does not appear."
---

## What This Error Means

You applied `backdrop-filter: blur()` to create a frosted glass effect but the background remains fully visible with no blur or color adjustment. The backdrop filter appears to have no visual effect at all.

## Why It Happens

The `backdrop-filter` property is not supported in all browsers. Internet Explorer does not support it at all. Older versions of Firefox before version 103 did not support it. Even in browsers that support it, there are conditions that prevent it from working.

The most common cause is a missing background on the element with the backdrop filter. The element must have a background with some level of transparency. If the element has `background-color: white` with full opacity, the backdrop filter has nothing to show because the solid background completely covers the content behind it.

The element also needs to be above the content it is blurring. If the backdrop filter element is behind the content in the stacking order, there is no backdrop to filter. The element needs a higher stacking position than the content it should blur.

The `backdrop-filter` property also requires the element to have its own stacking context. Adding `position: relative` with a `z-index` or using `backdrop-filter` itself creates a stacking context, but if the element is in a lower stacking context than the content behind it, the filter will not apply to that content.

## How to Fix It

Give the element a semi-transparent background so the blur is visible:

```css
.glass-panel {
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  background-color: rgba(255, 255, 255, 0.25);
  border-radius: 12px;
  padding: 2rem;
}
```

Ensure the element is positioned above the background content:

```css
.hero-image {
  position: relative;
  z-index: 1;
}

.hero-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  background-color: rgba(0, 0, 0, 0.3);
  z-index: 2;
}
```

Always include the `-webkit-` prefix for Safari support:

```css
.overlay {
  -webkit-backdrop-filter: blur(10px) saturate(180%);
  backdrop-filter: blur(10px) saturate(180%);
  background-color: rgba(255, 255, 255, 0.65);
}
```

Provide a solid color fallback for browsers that do not support `backdrop-filter`:

```css
.overlay {
  background-color: rgba(255, 255, 255, 0.85);
}

@supports (backdrop-filter: blur(1px)) {
  .overlay {
    backdrop-filter: blur(10px);
    background-color: rgba(255, 255, 255, 0.4);
  }
}
```

Note that `backdrop-filter` does not work on elements inside a container with `overflow: hidden` in some browsers, and it can cause performance issues on mobile when applied to large areas.

## Common Mistakes

- Forgetting the `-webkit-backdrop-filter` prefix for Safari compatibility
- Setting a fully opaque background which hides the blur effect completely
- Not giving the element a stacking context so it sits behind the content it should blur
- Using `backdrop-filter` on large elements which causes performance issues on mobile
- Applying `backdrop-filter` inside `overflow: hidden` containers which may not render correctly
- Not providing a solid color fallback for unsupported browsers

## Related Pages

- [Z-Index Not Working](/languages/css/z-index-not-working/)
- [Position Absolute Viewport](/languages/css/position-absolute-viewport/)
- [Overflow Hidden Bleed](/languages/css/overflow-hidden-bleed/)
- [CSS Has Selector](/languages/css/css-has-selector/)
- [Dark Mode Media Query](/languages/css/dark-mode-media-query/)
