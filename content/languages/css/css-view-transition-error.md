---
title: "[Solution] CSS View Transition API Error — How to Fix"
description: "Fix CSS View Transition API errors. Learn how to use view-transition-name, ::view-transition pseudo-elements, and cross-document transitions correctly."
languages: ["css"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
comments: true
---

## Why It Happens

The View Transition API creates smooth animated transitions between different DOM states or page navigations. When the API is used incorrectly, transitions either do not trigger, animate the wrong elements, or produce visual glitches.

The most common cause is missing `view-transition-name` on the elements you want to animate. Without unique names, the browser cannot match elements between the old and new states.

Another frequent cause is duplicate `view-transition-name` values. Each transition name must be unique across the entire document. If two elements share the same name, only one will transition correctly.

Cross-document transitions require specific server configuration. The `@view-transition` at-rule must be used with `navigation: auto` and the server must return the correct headers for the transition to work.

The `::view-transition` pseudo-elements only work during an active transition. Styling them outside of a transition has no effect and the browser ignores the rules.

JavaScript-triggered transitions require calling `document.startViewTransition()`. If you modify the DOM without wrapping the change in this function, no transition occurs.

The transition is blocked if the old and new states have incompatible layout. If the transition name is on an element whose position or size changes dramatically, the default cross-fade may look broken.

## Common Error Messages

```
CSS Warning: view-transition-name "hero" applied to multiple elements
```

```
JS Error: Failed to execute 'startViewTransition' — document not ready
```

```
CSS Warning: ::view-transition-* pseudo-element has no effect outside transition
```

```
CSS Error: view-transition-name not set on target element
```

## How to Fix It

### Assign unique view-transition-name to elements

```css
.hero-image {
  view-transition-name: hero;
}

.page-title {
  view-transition-name: title;
}

.sidebar {
  view-transition-name: sidebar;
}

/* Each name must be unique */
```

### Use JavaScript to trigger transitions

```javascript
// Trigger a view transition on state change
function updateContent(newContent) {
  if (!document.startViewTransition) {
    // Fallback for browsers without support
    setContent(newContent);
    return;
  }
  
  document.startViewTransition(() => {
    setContent(newContent);
  });
}
```

### Style transition pseudo-elements

```css
/* Default transition */
::view-transition-old(hero) {
  animation: fade-out 0.3s ease-out;
}

::view-transition-new(hero) {
  animation: fade-in 0.3s ease-in;
}

/* Custom animations */
@keyframes fade-out {
  from { opacity: 1; transform: scale(1); }
  to { opacity: 0; transform: scale(0.9); }
}

@keyframes fade-in {
  from { opacity: 0; transform: scale(1.1); }
  to { opacity: 1; transform: scale(1); }
}
```

### Configure cross-document transitions

```css
/* In both documents */
@view-transition {
  navigation: auto;
}

/* Style the root transition */
::view-transition-root(root) {
  animation: none;
  mix-blend-mode: normal;
}
```

### Handle named transitions for specific elements

```css
/* Only transition specific elements */
.card {
  view-transition-name: card-1;
}

/* Exclude elements from transition */
.no-transition {
  view-transition-name: none;
}

/* Use custom transition classes */
.card.transitioning {
  view-transition-class: card;
}

::view-transition-group(card) {
  animation-duration: 0.5s;
}
```

## Common Scenarios

- Building a single-page app with animated page transitions
- Creating morphing animations between different layouts
- Implementing cross-document transitions for multi-page applications

## Prevent It

- Always assign unique `view-transition-name` values to elements you want to animate
- Use `document.startViewTransition()` in JavaScript to trigger transitions programmatically
- Test transitions in Chrome 111+ and check for fallback behavior in unsupported browsers
