---
title: "[Solution] CSS Animation Not Playing — Fix Keyframes Not Triggering"
description: "Fix CSS animation not playing with this step-by-step solution. Learn why keyframes do not trigger, how animation-fill-mode works, and animation debugging tips."
---

## What This Error Means

Your CSS animation is defined but never plays. The element either stays in its initial state or jumps directly to the final state without any visible transition. The keyframes exist in the stylesheet but the browser never executes them.

## Why It Happens

CSS animations require the `animation-name` property to reference a valid `@keyframes` rule. If the name is misspelled or the keyframes rule does not exist, the animation silently fails. The `animation-duration` must also be greater than zero. A duration of `0s` or an omitted duration prevents the animation from playing.

Another common issue is `animation-fill-mode`. The default value `none` means the element reverts to its original state before and after the animation. If the animation runs quickly or the duration is short, you may not see it at all. Setting `animation-fill-mode: forwards` keeps the element at the final keyframe state after the animation completes.

Animations also do not play on elements that are `display: none` or not yet in the DOM. If you toggle visibility after a delay, the animation may have already finished.

## How to Fix It

Ensure the animation name matches the keyframes rule exactly:

```css
/* Wrong - name mismatch */
@keyframes fade-in {
  from { opacity: 0; }
  to { opacity: 1; }
}

.box {
  animation: fadeIn 1s ease-in-out; /* Wrong name */
}

/* Correct */
.box {
  animation: fade-in 1s ease-in-out;
}
```

Set a duration greater than zero:

```css
.box {
  animation: slide-in 0.5s ease-in-out forwards;
}
```

Use `animation-fill-mode` to control behavior before and after the animation:

```css
.box {
  animation: fade-in 1s ease-in-out forwards;
  /* forwards = stay at final keyframe after animation */
  /* both = apply first keyframe before, last keyframe after */
  /* backwards = apply first keyframe before animation starts */
}
```

Debug with DevTools. Open the Animations panel in Chrome DevTools under the Elements tab to inspect running animations, pause them, and see the computed keyframes.

Trigger animations with class toggles:

```css
.box {
  opacity: 0;
  transition: opacity 0.3s;
}

.box.visible {
  opacity: 1;
}
```

## Common Mistakes

- Misspelling the animation name so it does not match the keyframes rule
- Setting `animation-duration: 0s` or omitting it entirely
- Not using `animation-fill-mode: forwards` when you need the final state to persist
- Applying animation to `display: none` elements that are removed from layout
- Expecting animations to replay when scrolling without using `animation-iteration-count` or JavaScript triggers
- Overriding animation properties with shorthand that resets earlier declarations

## Related Pages

- [CSS Transition Not Working](/languages/css/css-transition-not-working/)
- [CSS Transform 3D](/languages/css/css-transform-3d/)
- [CSS Variable Scope](/languages/css/css-variable-scope/)
- [Z-Index Not Working](/languages/css/z-index-not-working/)
- [CSS Scroll Snap](/languages/css/css-scroll-snap/)
