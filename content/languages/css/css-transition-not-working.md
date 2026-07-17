---
title: "[Solution] CSS Transition Not Working — Fix Animation Issues"
description: "Fix CSS transitions not working with this step-by-step solution. Learn about transition properties, trigger events, and why animations do not fire on load."
---

## What This Error Means

You defined a CSS transition on an element but it is not animating when the property changes. The element snaps instantly to its new state instead of smoothly transitioning between values.

## Why It Happens

A CSS transition requires three parts: a property to transition, a duration, and a trigger. If any part is missing, the transition will not fire.

The most common mistake is defining the transition on the element but triggering the change on a different state or a different element. For example, if you define the transition on `.button` but change the background color inside `.button:hover`, the transition is defined correctly. However, if you define both the transition and the color change inside `.hover` only, there is no transition defined for the non-hover state so the browser does not know to animate.

Another frequent issue is trying to transition properties that cannot be animated. Properties like `display`, `font-family`, and `float` do not support transitions. When you change `display: none` to `display: block`, it happens instantly because the browser treats it as a discrete property change.

The `transition` shorthand must come before or alongside the property change. If the transition is defined with a delay, the animation waits before starting which may appear as if it never happened.

## How to Fix It

Define the transition on the base state of the element, not inside the hover or active state:

```css
.button {
  background-color: #3498db;
  transition: background-color 0.3s ease;
}

.button:hover {
  background-color: #2980b9;
}
```

Use the shorthand to set property, duration, timing function, and delay:

```css
.card {
  transform: translateY(0);
  transition: transform 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.card:hover {
  transform: translateY(-8px);
}
```

To transition multiple properties, list them separated by commas:

```css
.element {
  transition: opacity 0.3s ease, transform 0.3s ease, box-shadow 0.5s ease;
}
```

For transitions that should play on page load, use CSS animations instead of transitions since transitions require a property change trigger:

```css
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.element {
  animation: fadeIn 0.5s ease forwards;
}
```

## Common Mistakes

- Defining the transition inside the `:hover` state instead of the base state
- Trying to transition `display`, `visibility`, or `font-family` which are not animatable
- Setting `transition: all 0.3s` which may cause performance issues and unexpected animations
- Forgetting to set a duration which defaults to 0s making the transition instant
- Not using `will-change` for performance on expensive animations like transforms and opacity
- Using JavaScript to toggle a class that removes the transition before it can play

## Related Pages

- [Flexbox Centering](/languages/css/flexbox-centering/)
- [Z-Index Not Working](/languages/css/z-index-not-working/)
- [CSS Container Queries](/languages/css/css-container-queries/)
- [CSS Has Selector](/languages/css/css-has-selector/)
- [CSS Scroll Snap](/languages/css/css-scroll-snap/)
