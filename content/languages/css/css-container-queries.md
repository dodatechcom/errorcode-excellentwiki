---
title: "[Solution] CSS Container Queries Not Applying — Fix Container Styles"
description: "Fix CSS container queries not working with this step-by-step solution. Learn about container types, naming containers, and why queries do not trigger."
---

## What This Error Means

You defined a container query but the styles inside it are not being applied. The component does not respond to its container size changes even though the viewport is clearly different. The container query appears to be completely ignored.

## Why It Happens

Container queries require the parent element to be declared as a container using the `container-type` property. Without this declaration, the browser does not track that element's dimensions and the `@container` query has nothing to reference.

A common mistake is setting `container-type: inline-size` on the wrong element. The container must be an ancestor of the element you want to style. If the container is a sibling or a descendant of the target element, the query will not match.

Another issue is that `container-type: inline-size` only tracks the inline (horizontal) dimension by default. If you are checking `min-height` in a container query, it will not work unless you also set `container-type: size` which tracks both dimensions. However, `size` affects layout because it prevents the container from being sized by its content.

The `container-type` property creates a containment context. This means the element becomes a formatting context root which can affect its layout. Inline elements become block-level, and the element may need explicit width and height to behave correctly.

## How to Fix It

Declare the container on the parent element:

```css
.card-wrapper {
  container-type: inline-size;
  container-name: card;
}
```

Name your containers when you have multiple to avoid ambiguity:

```css
.sidebar {
  container-type: inline-size;
  container-name: sidebar;
}

.main-content {
  container-type: inline-size;
  container-name: main;
}
```

Reference the container name in the query:

```css
@container card (min-width: 400px) {
  .card {
    display: grid;
    grid-template-columns: 1fr 2fr;
    gap: 1rem;
  }
}

@container card (max-width: 399px) {
  .card {
    display: flex;
    flex-direction: column;
  }
}
```

Without a name, the query targets the nearest ancestor container:

```css
@container (min-width: 400px) {
  .card {
    display: grid;
    grid-template-columns: 1fr 1fr;
  }
}
```

For vertical container queries using `container-type: size`, be aware this may break your layout if the container has content-based sizing. Use `min-height` or `height` on the container to give it explicit dimensions.

## Common Mistakes

- Forgetting to set `container-type` on the parent element entirely
- Using `container-type: size` when `inline-size` is sufficient to avoid layout side effects
- Placing the container declaration on the wrong element in the DOM tree
- Trying to use `min-height` or `max-height` queries with `container-type: inline-size` which only tracks width
- Not naming containers when multiple exist which causes the wrong container to be matched
- Assuming container queries work in browsers older than Chrome 105, Safari 16, and Firefox 110

## Related Pages

- [Media Query Not Applying](/languages/css/media-query-not-applying/)
- [CSS Grid Not Working](/languages/css/css-grid-not-working/)
- [CSS Unit Mismatch](/languages/css/css-unit-mismatch/)
- [CSS Has Selector](/languages/css/css-has-selector/)
- [CSS Variable Scope](/languages/css/css-variable-scope/)
