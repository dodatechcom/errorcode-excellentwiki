---
title: "[Solution] CSS :focus-visible Not Showing Outline — Fix Keyboard Focus Ring"
description: "Fix CSS focus-visible not showing outline with this step-by-step solution. Learn when focus-visible activates, how to style focus rings, and accessibility tips."
---

## What This Error Means

The `:focus-visible` pseudo-class is not showing the expected focus outline on interactive elements. Users who navigate with a keyboard cannot see which element is currently focused, which is an accessibility violation.

## Why It Happens

`:focus-visible` only activates when the browser determines the user is using keyboard navigation. Clicking an element with a mouse does not trigger `:focus-visible` in most browsers. If you are testing by clicking, the outline will not appear.

Some CSS resets or frameworks remove the default outline with `outline: none` or `outline: 0` without providing a `:focus-visible` replacement. This leaves keyboard users with no visible focus indicator.

Browser support is broad but not universal. Chrome, Edge, Firefox, and Safari all support `:focus-visible` in modern versions. Older browsers fall back to the regular `:focus` pseudo-class, which activates on both mouse and keyboard focus.

The `outline` property is also affected by `overflow: hidden` on parent elements. If the focus ring extends beyond the parent bounds, it may be clipped.

## How to Fix It

Provide a focus-visible style that only appears for keyboard users:

```css
/* Remove default outline for mouse users */
:focus:not(:focus-visible) {
  outline: none;
}

/* Show outline for keyboard users */
:focus-visible {
  outline: 2px solid #4a90d9;
  outline-offset: 2px;
}
```

Style focus states for specific interactive elements:

```css
button:focus-visible {
  outline: 3px solid #ff6b6b;
  outline-offset: 2px;
}

a:focus-visible {
  outline: 2px dashed #4ecdc4;
  outline-offset: 4px;
}

input:focus-visible {
  outline: 2px solid #667eea;
  outline-offset: 1px;
  box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.25);
}
```

Provide a `:focus` fallback for browsers without `:focus-visible` support:

```css
:focus {
  outline: 2px solid #4a90d9;
  outline-offset: 2px;
}

:focus:not(:focus-visible) {
  outline: none;
}

:focus-visible {
  outline: 2px solid #4a90d9;
  outline-offset: 2px;
}
```

Use `outline` with `outline-offset` for spacing between the element and the ring.

## Common Mistakes

- Removing `outline: none` without providing a `:focus-visible` replacement
- Testing focus-visible by clicking instead of using the Tab key
- Setting `outline: 0` in a CSS reset without considering keyboard accessibility
- Using `box-shadow` as a focus indicator without also providing a visible `outline`
- Assuming all users can see thin or low-contrast focus rings

## Related Pages

- [CSS Specificity Conflict](/languages/css/css-specificity-conflict/)
- [CSS Has Selector](/languages/css/css-has-selector/)
- [Z-Index Not Working](/languages/css/z-index-not-working/)
- [CSS Nth Child](/languages/css/css-nth-child/)
- [Dark Mode Media Query](/languages/css/dark-mode-media-query/)
