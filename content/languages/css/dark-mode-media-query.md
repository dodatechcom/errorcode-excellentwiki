---
title: "[Solution] prefers-color-scheme Not Working — Fix Dark Mode Media Query"
description: "Fix prefers-color-scheme not working with this step-by-step solution. Learn about media query syntax, browser support, and how to implement dark mode CSS."
---

## What This Error Means

Your `prefers-color-scheme` media query is not responding to the user's operating system color scheme setting. The page always stays in light mode (or always stays in dark mode) regardless of the system preference.

## Why It Happens

The `prefers-color-scheme` media query requires the correct syntax with the `no-preference`, `light`, or `dark` values. A common mistake is writing `prefers-color-scheme: dark-mode` or using incorrect capitalization.

The media query also depends on the operating system setting. If the user has their OS set to light mode and you only define styles for `prefers-color-scheme: dark`, the media query will never match because the condition is not met. You need to define both light and dark styles or provide a default that covers the unmatched case.

Another issue is that the media query must be at the top level of the stylesheet. Placing it inside another at-rule or nesting it in a way the browser does not support can cause it to be ignored.

Browser support is broad but not universal. Internet Explorer and older versions of Safari before 12.1 do not support this media query. In those browsers the media query is simply ignored and the default (usually light) styles apply.

## How to Fix It

Define the media query with the correct value and ensure both modes are covered:

```css
/* Default (light mode) */
body {
  background-color: #ffffff;
  color: #333333;
}

/* Dark mode when system preference is dark */
@media (prefers-color-scheme: dark) {
  body {
    background-color: #1a1a2e;
    color: #e0e0e0;
  }
}
```

For the reverse approach where dark is the default:

```css
body {
  background-color: #1a1a2e;
  color: #e0e0e0;
}

@media (prefers-color-scheme: light) {
  body {
    background-color: #ffffff;
    color: #333333;
  }
}
```

You can also combine the media query with a class-based toggle for users who want to override the system setting:

```css
:root {
  --bg: #ffffff;
  --text: #333333;
}

[data-theme="dark"] {
  --bg: #1a1a2e;
  --text: #e0e0e0;
}

@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg: #1a1a2e;
    --text: #e0e0e0;
  }
}
```

Test by toggling the color scheme in your OS settings or using DevTools emulation under the Rendering panel.

## Common Mistakes

- Writing `prefers-color-scheme: dark-mode` instead of `prefers-color-scheme: dark`
- Only defining dark mode styles without providing light mode defaults
- Placing the media query inside another at-rule that may not match
- Not accounting for users who manually set their OS to a different mode than expected
- Assuming all browsers support the feature when older browsers ignore it silently
- Using inline styles that override the media query cascade

## Related Pages

- [CSS Variable Scope](/languages/css/css-variable-scope/)
- [Media Query Not Applying](/languages/css/media-query-not-applying/)
- [CSS Specificity Conflict](/languages/css/css-specificity-conflict/)
- [CSS Has Selector](/languages/css/css-has-selector/)
- [CSS Container Queries](/languages/css/css-container-queries/)
