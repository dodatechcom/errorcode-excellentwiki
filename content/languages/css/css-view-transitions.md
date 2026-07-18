---
title: "[Solution] CSS View Transitions API Not Working — Fix Page Animations"
description: "Fix CSS View Transitions API not working with this step-by-step solution. Learn about view-transition-name, cross-document transitions, and browser support."
---

## What This Error Means

The CSS View Transitions API is not producing the expected animation between page states or navigation. Elements that should animate between old and new positions are not transitioning, or the transition is not triggering at all.

## Why It Happens

View transitions require the `view-transition-name` property on elements that should animate. Without it, the browser does not capture the element state for the transition. Each transitioning element must have a unique `view-transition-name` value.

For cross-document (MPA) transitions, the server must respond with a `Sec-CH-View-Mode` header or the page must include a `<meta>` tag. The `@view-transition` at-rule must be present in the CSS to opt in to cross-document transitions.

Browser support is limited. Chrome 111+ supports document transitions, and Chrome 126+ supports element-level transitions. Firefox and Safari do not yet support the View Transitions API.

The transition also fails if the element is not rendered at the time of the snapshot. Elements with `display: none` or elements not yet in the DOM cannot be captured.

## How to Fix It

Add `view-transition-name` to elements that should animate:

```css
.hero-image {
  view-transition-name: hero;
}

.page-title {
  view-transition-name: title;
}
```

Trigger transitions in JavaScript for single-page applications:

```css
::view-transition-old(hero) {
  animation: fade-out 0.3s ease-in;
}

::view-transition-new(hero) {
  animation: fade-in 0.3s ease-out;
}
```

Enable cross-document transitions:

```css
@view-transition {
  navigation: auto;
}
```

Style the transition pseudo-elements:

```css
::view-transition-old(page) {
  animation: slide-out-left 0.3s ease-in forwards;
}

::view-transition-new(page) {
  animation: slide-in-right 0.3s ease-out forwards;
}
```

Disable transitions for specific elements:

```css
.no-transition {
  view-transition-name: none;
}
```

Provide a reduced-motion preference:

```css
@media (prefers-reduced-motion: reduce) {
  ::view-transition-old(*),
  ::view-transition-new(*) {
    animation: none;
  }
}
```

## Common Mistakes

- Forgetting to set `view-transition-name` on the elements that should animate
- Using duplicate `view-transition-name` values on multiple elements in the same document
- Not including the `@view-transition` at-rule for cross-document transitions
- Assuming support in Firefox or Safari which do not yet implement the API
- Animating elements with `display: none` which cannot be captured for the transition
- Not respecting `prefers-reduced-motion` for accessibility

## Related Pages

- [CSS Animation Not Playing](/languages/css/css-animation-not-playing/)
- [CSS Transition Not Working](/languages/css/css-transition-not-working/)
- [CSS Transform 3D](/languages/css/css-transform-3d/)
- [CSS Anchor Positioning](/languages/css/css-anchor-positioning/)
- [Dark Mode Media Query](/languages/css/dark-mode-media-query/)
