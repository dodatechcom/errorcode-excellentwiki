---
title: "[Solution] CSS transition-behavior: allow-discrete Not Working"
description: "Fix CSS transition-behavior: allow-discrete not animating display or overlay. Learn about discrete property transitions and browser support."
---

## What This Error Means

Your `transition-behavior: allow-discrete` is not enabling transitions on discrete properties like `display` or `overlay`. These properties normally switch instantly, and `allow-discrete` should let them transition, but the effect is not working.

## Why It Happens

The most common cause is browser support. `transition-behavior: allow-discrete` is only supported in Chrome 117+ and Edge 117+. Firefox and Safari do not support it yet.

Another frequent cause is incorrect syntax. The property must be applied to the `transition` shorthand or as a standalone property alongside the `transition-property`.

Using `allow-discrete` without the corresponding `transition-property` declaration has no effect. The `display` or `overlay` property must be explicitly included in the transition.

The transition duration may be set to `0s`, which makes the discrete transition instant even with `allow-discrete`.

Finally, combining `allow-discrete` with `transition-behavior: normal` on the same property causes conflicting behavior.

## How to Fix It

### Use transition-behavior with explicit transition-property

```css
.element {
  display: block;
  opacity: 1;
  transition: opacity 0.3s, display 0.3s allow-discrete;
}

.element.hidden {
  display: none;
  opacity: 0;
}
```

### Use the standalone property

```css
.element {
  display: block;
  transition-property: display, opacity;
  transition-duration: 0.3s;
  transition-behavior: allow-discrete;
}
```

### Animate popover display

```css
[popover] {
  opacity: 1;
  transition: opacity 0.3s,
              display 0.3s allow-discrete,
              overlay 0.3s allow-discrete;
}

[popover]:not(:popover-open) {
  opacity: 0;
  display: none;
  overlay: none;
}
```

### Use @starting-style for entry animations

```css
.element {
  opacity: 1;
  transition: opacity 0.3s, display 0.3s allow-discrete;
}

.element.hidden {
  display: none;
  opacity: 0;
}

@starting-style {
  .element {
    opacity: 0;
  }
}
```

### Check browser support

```css
@supports (transition-behavior: allow-discrete) {
  .element {
    transition: opacity 0.3s, display 0.3s allow-discrete;
  }
}
```

## Common Mistakes

- Not including `display` or `overlay` in the `transition-property`
- Setting `transition-duration: 0s` when you want a visible transition
- Not checking browser support for `allow-discrete`
- Using `allow-discrete` with properties that are already continuous
- Not combining with `@starting-style` for entry animations

## Related Pages

- [CSS Starting Style](/languages/css/css-starting-style/)
- [CSS Animation Not Playing](/languages/css/css-animation-not-playing/)
- [CSS Transition Not Working](/languages/css/css-transition-not-working/)
