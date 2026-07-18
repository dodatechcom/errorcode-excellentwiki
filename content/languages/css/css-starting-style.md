---
title: "[Solution] CSS @starting-style Not Animating on First Render"
description: "Fix CSS @starting-style not producing entry animations. Learn about entry animations, display transitions, and browser support for @starting-style."
---

## What This Error Means

Your `@starting-style` rule is not producing the expected entry animation. Elements should animate from the starting style to their normal style when first rendered, but they appear without animation or appear in their final state immediately.

## Why It Happens

The most common cause is browser support. `@starting-style` is only supported in Chrome 117+ and Edge 117+. Firefox and Safari do not support it yet.

Another frequent cause is missing `transition` or `transition-behavior` properties. The `@starting-style` rule defines the initial state, but you need a `transition` on the element to animate from that state.

The element must transition from `display: none` or `content-visibility: hidden` for the entry animation to work properly. If the element is already rendered, `@starting-style` has no effect.

Using `@starting-style` without matching `transition` properties means the element jumps to its final state without animating.

Finally, `@starting-style` only applies to the first render. If the element is already in the DOM and visible, the starting style is not used.

## How to Fix It

### Combine @starting-style with transitions

```css
.element {
  opacity: 1;
  transform: translateY(0);
  transition: opacity 0.3s, transform 0.3s;
}

@starting-style {
  .element {
    opacity: 0;
    transform: translateY(20px);
  }
}
```

### Use for popovers and dialogs

```css
[popover] {
  opacity: 1;
  transform: scale(1);
  transition: opacity 0.3s, transform 0.3s,
              display 0.3s allow-discrete,
              overlay 0.3s allow-discrete;
}

[popover]:not(:popover-open) {
  opacity: 0;
  transform: scale(0.9);
}

@starting-style {
  [popover]:popover-open {
    opacity: 0;
    transform: scale(0.9);
  }
}
```

### Use for elements transitioning from display: none

```css
.dialog {
  display: block;
  opacity: 1;
  transition: opacity 0.3s, display 0.3s allow-discrete;
}

.dialog.hidden {
  display: none;
  opacity: 0;
}

@starting-style {
  .dialog {
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

  @starting-style {
    .element {
      opacity: 0;
    }
  }
}
```

### Provide fallback for older browsers

```css
/* Fallback */
.element {
  opacity: 1;
  animation: fadeIn 0.3s ease-in;
}

@keyframes fadeIn {
  from { opacity: 0; }
}

/* Modern */
@supports (animation: transition) {
  .element {
    animation: none;
    transition: opacity 0.3s;
  }
}
```

## Common Mistakes

- Using @starting-style without a matching transition property
- Not using allow-discrete for display/overlay transitions
- Applying @starting-style to elements that are already rendered
- Not checking browser support before using @starting-style
- Assuming @starting-style creates animations without transitions

## Related Pages

- [CSS Transition Behavior](/languages/css/css-transition-behavior/)
- [CSS Animation Not Playing](/languages/css/css-animation-not-playing/)
- [CSS Transition Not Working](/languages/css/css-transition-not-working/)
