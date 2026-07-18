---
title: "[Solution] CSS Gradient Not Displaying — Fix Broken Gradient Background"
description: "Fix CSS gradient not displaying with this step-by-step solution. Learn about gradient syntax, browser prefixes, and why gradients appear as solid colors."
---

## What This Error Means

Your CSS gradient background is not rendering. Instead, the element shows a solid color or no background at all. The gradient may appear broken, display only one color, or fail silently in certain browsers.

## Why It Happens

CSS gradients rely on precise syntax. A missing comma, incorrect function name, or wrong number of color stops causes the entire gradient declaration to be invalid. The browser then ignores it and falls back to the next background layer or no background.

Older browsers require vendor prefixes. `linear-gradient` needs `-webkit-linear-gradient` for Safari versions below 12.1 and older Chrome versions. Without the prefix, the gradient fails in those browsers.

Gradients also fail when they are placed after a shorthand `background` property. The shorthand resets all background sub-properties, including `background-image`. If you set `background: #fff` before `background: linear-gradient(...)`, the gradient is overridden.

## How to Fix It

Use the standard gradient syntax with correct color stops:

```css
/* Wrong - missing comma between color stops */
.element {
  background: linear-gradient(to right, red blue);
}

/* Correct */
.element {
  background: linear-gradient(to right, red, blue);
}
```

Add vendor prefixes for older browser support:

```css
.element {
  background: -webkit-linear-gradient(top, #ff6b6b, #4ecdc4);
  background: linear-gradient(to bottom, #ff6b6b, #4ecdc4);
}
```

Do not use shorthand `background` before `background-image`:

```css
/* Wrong - background shorthand resets the gradient */
.element {
  background: #fff;
  background: linear-gradient(to bottom, #ff6b6b, #4ecdc4);
}

/* Correct - use background-color as a separate layer */
.element {
  background-color: #fff;
  background-image: linear-gradient(to bottom, #ff6b6b, #4ecdc4);
}
```

Verify the gradient direction keyword. Common valid values are `to top`, `to bottom`, `to right`, `to left`, and angle values like `45deg`:

```css
.element {
  background: linear-gradient(45deg, #667eea, #764ba2);
}
```

## Common Mistakes

- Missing a comma between color stops in the gradient function
- Using `background` shorthand which resets previously defined gradients
- Not providing vendor prefixes for older browser support
- Using invalid direction keywords like `left to right` instead of `to right`
- Assuming radial-gradient and conic-gradient use the same syntax as linear-gradient
- Placing gradients inside `@supports` queries that do not match the target browser

## Related Pages

- [CSS Backdrop Filter](/languages/css/css-backdrop-filter/)
- [Dark Mode Media Query](/languages/css/dark-mode-media-query/)
- [CSS Variable Scope](/languages/css/css-variable-scope/)
- [Media Query Not Applying](/languages/css/media-query-not-applying/)
- [CSS Transition Not Working](/languages/css/css-transition-not-working/)
