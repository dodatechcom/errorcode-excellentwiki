---
title: "[Solution] CSS Scroll-Behavior Smooth Not Working"
description: "Fix CSS scroll-behavior: smooth not producing smooth scrolling. Learn about scroll containers, overflow, and JavaScript fallbacks."
---

## What This Error Means

Your `scroll-behavior: smooth` is not producing smooth scrolling when navigating to anchor links or using `scrollIntoView()`. The page jumps instantly to the target instead of animating the scroll.

## Why It Happens

The most common cause is not applying `scroll-behavior: smooth` to the correct scroll container. The property must be on the element that scrolls, which is typically the `html` element for page-level scrolling or a specific container with `overflow: auto` or `overflow: scroll`.

Another frequent cause is using JavaScript `window.scrollTo()` without the `behavior: 'smooth'` option. CSS `scroll-behavior` only affects native scroll mechanisms like anchor links and `scrollIntoView()`.

The scroll container may not actually be scrollable. If the container's content does not overflow, there is nothing to scroll and the smooth behavior is not visible.

`prefers-reduced-motion` media query may disable smooth scrolling for users who prefer reduced motion. This is correct behavior but may surprise developers.

Finally, some browsers may not support `scroll-behavior` on the `html` element, or may have it disabled for performance reasons.

## How to Fix It

### Apply scroll-behavior to the correct element

```css
/* For page-level scrolling */
html {
  scroll-behavior: smooth;
}

/* For a specific scroll container */
.scroll-container {
  overflow-y: auto;
  scroll-behavior: smooth;
}
```

### Use JavaScript for programmatic scrolling

```javascript
// Wrong — instant jump
window.scrollTo(0, 500);

// Correct — smooth scroll
window.scrollTo({
  top: 500,
  behavior: 'smooth'
});

// Or use scrollIntoView
element.scrollIntoView({ behavior: 'smooth' });
```

### Handle prefers-reduced-motion

```css
@media (prefers-reduced-motion: no-preference) {
  html {
    scroll-behavior: smooth;
  }
}
```

### Ensure the container is scrollable

```css
.scroll-container {
  height: 400px;
  overflow-y: auto;
  scroll-behavior: smooth;
}
```

### Check for competing scroll behavior

```css
/* Remove any scroll-snap that might interfere */
.container {
  scroll-snap-type: none;
  scroll-behavior: smooth;
}
```

## Common Mistakes

- Applying `scroll-behavior` to the wrong element
- Not using `behavior: 'smooth'` in JavaScript scroll calls
- Forgetting that `prefers-reduced-motion` may disable smooth scrolling
- Combining with scroll-snap which can interfere with smooth behavior
- Not testing on mobile browsers where behavior may differ

## Related Pages

- [CSS Scroll Snap](/languages/css/css-scroll-snap/)
- [CSS Transition Not Working](/languages/css/css-transition-not-working/)
- [CSS Animation Not Playing](/languages/css/css-animation-not-playing/)
