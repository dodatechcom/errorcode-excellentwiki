---
title: "[Solution] CSS Placeholder Styles Not Applying — ::placeholder Selector"
description: "Fix CSS ::placeholder pseudo-element not styling input placeholders. Learn about vendor prefixes, specificity, and placeholder styling."
---

## What This Error Means

Your `::placeholder` styles are not being applied to input placeholders. The placeholder text appears with default browser styling instead of your custom colors, fonts, or other styles.

## Why It Happens

The most common cause is missing vendor prefixes. While modern browsers support `::placeholder`, older versions require `::-webkit-input-placeholder`, `::-moz-placeholder`, or `::-ms-input-placeholder`.

Another frequent cause is specificity issues. If a browser default stylesheet or a CSS reset sets placeholder styles with higher specificity, your styles may be overridden.

Using `::placeholder` on non-input elements does not work. Placeholders only exist on `<input>`, `<textarea>`, and related form elements.

The placeholder text may be styled by JavaScript. Some libraries set inline styles on placeholder text that override CSS.

Finally, using `color` on the input element itself may not affect the placeholder. The placeholder has its own styling layer that must be targeted with `::placeholder`.

## How to Fix It

### Add all vendor prefixes

```css
input::placeholder {
  color: #999;
  opacity: 1;  /* Firefox adds opacity by default */
}

/* Cross-browser support */
input::-webkit-input-placeholder { color: #999; }
input::-moz-placeholder          { color: #999; opacity: 1; }
input::-ms-input-placeholder     { color: #999; }
```

### Use the modern ::placeholder with fallbacks

```css
input::placeholder {
  color: #999;
  font-style: italic;
}
```

### Set opacity for Firefox

```css
/* Firefox adds opacity to placeholder text */
input::placeholder {
  color: #999;
  opacity: 1;
}
```

### Reset placeholder styles before applying new ones

```css
input::placeholder {
  all: unset;  /* Reset all inherited styles */
  color: #999;
  font-size: 14px;
}
```

### Check for JavaScript interference

```javascript
// Some libraries override placeholder styles
// Check for inline styles on the input
console.log(input.style.cssText);
```

## Common Mistakes

- Forgetting the Firefox opacity fix
- Not including vendor prefixes for older browsers
- Trying to use ::placeholder on non-form elements
- Not accounting for JavaScript libraries that override styles
- Using color on the input element instead of ::placeholder

## Related Pages

- [CSS Pseudo-Element](/languages/css/css-pseudo-element/)
- [CSS Focus Visible](/languages/css/css-focus-visible/)
- [CSS Specificity Conflict](/languages/css/css-specificity-conflict/)
