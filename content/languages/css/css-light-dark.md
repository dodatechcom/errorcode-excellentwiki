---
title: "[Solution] CSS light-dark() Function Not Working"
description: "Fix CSS light-dark() function not rendering. Learn about light-dark() support, color-scheme, and theme switching in modern CSS."
---

## What This Error Means

Your CSS `light-dark()` function is not producing the expected colors. The function should return different colors based on the element's color scheme, but it returns a single color or fails entirely.

## Why It Happens

The most common cause is browser support. The `light-dark()` function is only supported in Chrome 123+ and Firefox 120+. Safari does not support it yet.

Another frequent cause is missing `color-scheme` declaration. The `light-dark()` function requires the element to have a `color-scheme` value set to `light`, `dark`, or `normal`. Without it, the function does not know which color to return.

The function may return the wrong color because `color-scheme` is inherited from a parent element. If a parent sets `color-scheme: dark`, all descendants use the dark color from `light-dark()`.

Using `light-dark()` with non-color properties does not work. The function only returns color values, not other CSS values.

Finally, the function syntax must be exactly `light-dark(light-color, dark-color)` with exactly two arguments.

## How to Fix It

### Set color-scheme on the element

```css
.element {
  color-scheme: light dark;
  color: light-dark(#000, #fff);
  background: light-dark(#fff, #000);
}
```

### Use color-scheme: normal for user preference

```css
:root {
  color-scheme: normal;  /* Follows system preference */
}

.element {
  color: light-dark(#333, #ddd);
}
```

### Combine with prefers-color-scheme for fallback

```css
/* Fallback for browsers without light-dark() */
.element {
  color: #333;
}

@media (prefers-color-scheme: dark) {
  .element {
    color: #ddd;
  }
}

/* Modern browsers */
@supports (color: light-dark(#000, #fff)) {
  .element {
    color: light-dark(#333, #ddd);
  }
}
```

### Use light-dark() for all theme-sensitive colors

```css
:root {
  color-scheme: light dark;
}

body {
  color: light-dark(#1a1a1a, #e0e0e0);
  background: light-dark(#ffffff, #121212);
  border-color: light-dark(#cccccc, #444444);
}

a {
  color: light-dark(#0066cc, #6699ff);
}
```

### Check browser support

```css
@supports (color: light-dark(#000, #fff)) {
  /* light-dark() is supported */
}
```

## Common Mistakes

- Not setting `color-scheme` on the element or a parent
- Using `light-dark()` with non-color properties
- Not providing a fallback for browsers without support
- Assuming `light-dark()` works without `color-scheme`
- Using the wrong argument order (light first, dark second)

## Related Pages

- [CSS Dark Mode Media Query](/languages/css/dark-mode-media-query/)
- [CSS Variable Scope](/languages/css/css-variable-scope/)
- [CSS Nesting](/languages/css/css-nesting/)
