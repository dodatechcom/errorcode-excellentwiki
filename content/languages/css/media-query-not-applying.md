---
title: "[Solution] Media Query Not Applying — Fix Responsive Breakpoints"
description: "Fix media queries not applying with this step-by-step solution. Learn about viewport meta tag, breakpoint ordering, and syntax errors that prevent responsive styles."
---

## What This Error Means

Your media queries are not triggering at the expected viewport widths. Styles inside the media query block never apply, or they apply at the wrong screen sizes. Your responsive design is not responding to viewport changes.

## Why It Happens

The most common cause is a missing viewport meta tag in the HTML `<head>`. Without this tag, mobile browsers render the page at a desktop width and then scale it down. The viewport remains at 980px or similar regardless of the actual device width, so your breakpoints never trigger.

Another issue is incorrect media query syntax. A missing colon after `@media`, using `width` instead of `max-width` or `min-width`, or forgetting parentheses around the condition will cause the entire block to be ignored by the browser.

The order of breakpoints matters. If you define `min-width: 768px` before `min-width: 1024px`, the smaller breakpoint styles will apply at larger widths too because 1024 is greater than 768. Always use `min-width` queries in ascending order and `max-width` queries in descending order.

A subtle issue is that the browser rounds or snaps to pixel boundaries. A breakpoint at `768.5px` will behave differently across browsers because viewport widths are measured in whole pixels.

## How to Fix It

Add the viewport meta tag to your HTML head:

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

Fix media query syntax. Use proper min-width or max-width with correct value formats:

```css
/* Wrong */
@media (width: 768px) { ... }
@media (maxwidth: 768px) { ... }

/* Correct */
@media (max-width: 767px) { ... }
@media (min-width: 768px) { ... }
```

Order your breakpoints from smallest to largest using `min-width`:

```css
/* Mobile first approach */
.container { padding: 1rem; }

@media (min-width: 576px) {
  .container { padding: 2rem; }
}

@media (min-width: 768px) {
  .container { padding: 3rem; }
}
```

Avoid chaining conditions that may conflict:

```css
/* This only applies between 768px and 1024px */
@media (min-width: 768px) and (max-width: 1024px) {
  .sidebar { display: none; }
}
```

Test with browser DevTools responsive mode by entering specific pixel widths rather than just resizing the window.

## Common Mistakes

- Missing the viewport meta tag entirely on the page
- Using `width` instead of `min-width` or `max-width`
- Writing `@media screen and (max-width: 768px)` when `@media (max-width: 768px)` is sufficient for most cases
- Not accounting for the scrollbar width which reduces available viewport width
- Placing media queries inside other at-rules that may not match
- Using `device-width` instead of `width` which measures the physical screen not the viewport

## Related Pages

- [CSS Unit Mismatch](/languages/css/css-unit-mismatch/)
- [CSS Grid Not Working](/languages/css/css-grid-not-working/)
- [Dark Mode Media Query](/languages/css/dark-mode-media-query/)
- [CSS Container Queries](/languages/css/css-container-queries/)
- [CSS Scroll Snap](/languages/css/css-scroll-snap/)
