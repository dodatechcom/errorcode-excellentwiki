---
title: "[Solution] CSS content-visibility Error — How to Fix"
description: "Fix CSS content-visibility errors. Learn how to use content-visibility for rendering performance, handle browser support, and avoid layout issues with skip content."
languages: ["css"]
error-types: ["runtime-error"]
severities: ["warning"]
weight: 10
comments: true
---

## Why It Happens

The `content-visibility` property allows the browser to skip rendering of off-screen content, improving page load performance. When used incorrectly, it causes hidden content, broken layouts, or elements that never become visible.

The most common cause is setting `content-visibility: hidden` on elements that should be visible. Unlike `visibility: hidden`, `content-visibility: hidden` completely skips rendering, so the element has no box and cannot be interacted with.

Another frequent cause is missing `contain-intrinsic-size` when using `content-visibility: auto`. Without this property, collapsed elements have zero height, causing layout shifts when they become visible.

The `auto` value only works when the element is off-screen. If you want to hide content that is on-screen, you need `content-visibility: hidden` instead of `content-visibility: auto`.

Elements with `content-visibility: hidden` cannot receive focus or be part of the accessibility tree. This can break keyboard navigation and screen reader functionality.

The property interacts with `overflow` in unexpected ways. If the element has `overflow: hidden`, the skipped content may not be accessible even when scrolled into view.

Positioned elements with `content-visibility: auto` may have incorrect positioning calculations because the browser does not know their size until they are rendered.

## Common Error Messages

```
CSS Warning: content-visibility: hidden makes element inaccessible to assistive technology
```

```
CSS Error: content-visibility: auto without contain-intrinsic-size causes layout shifts
```

```
CSS Warning: Skipped content with content-visibility: auto not rendered until scrolled into view
```

```
CSS Error: content-visibility conflicts with display: none or visibility: hidden
```

## How to Fix It

### Use content-visibility: auto for performance

```css
/* Skip rendering of off-screen sections */
.section {
  content-visibility: auto;
  contain-intrinsic-size: 0 500px; /* Estimated height */
}

/* Each section will only render when scrolled into view */
```

### Add contain-intrinsic-size for proper sizing

```css
/* Without contain-intrinsic-size, collapsed sections have zero height */
.section {
  content-visibility: auto;
  contain-intrinsic-size: 0 800px; /* width 0, height 800px */
}

/* For elements with specific dimensions */
.card {
  content-visibility: auto;
  contain-intrinsic-size: 300px 200px;
}

/* For elements with variable heights */
.article {
  content-visibility: auto;
  contain-intrinsic-size: auto 500px; /* Let browser estimate height */
}
```

### Handle accessibility correctly

```css
/* content-visibility: hidden removes from accessibility tree */
.hidden-section {
  content-visibility: hidden;
  /* Use visibility: hidden instead if you need accessibility */
}

/* Better approach — use visibility: hidden for accessibility */
.accessible-hidden {
  visibility: hidden;
  position: absolute;
}
```

### Apply to long pages with many sections

```css
/* Optimize a long page with many sections */
main > section {
  content-visibility: auto;
  contain-intrinsic-size: 0 600px;
  padding: 2rem;
}

/* Do not apply to navigation or header */
header, nav {
  content-visibility: visible; /* Always render */
}
```

### Handle interactions with positioned elements

```css
/* Sticky header needs visible content */
.sticky-header {
  content-visibility: visible;
  position: sticky;
  top: 0;
}

/* Modal overlay must be visible when triggered */
.modal-overlay {
  content-visibility: auto;
  contain-intrinsic-size: 0 100vh;
}

/* When modal is active, force render */
.modal-overlay.active {
  content-visibility: visible;
}
```

## Common Scenarios

- Optimizing a long blog page with many sections that load slowly
- Building an infinite scroll feed where only visible items should render
- Improving initial page load time by deferring rendering of below-fold content

## Prevent It

- Always include `contain-intrinsic-size` when using `content-visibility: auto` to prevent layout shifts
- Avoid using `content-visibility: hidden` on interactive elements that need keyboard or screen reader access
- Test with `content-visibility: visible` first, then add `auto` selectively for performance
