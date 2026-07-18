---
title: "[Solution] CSS Container Query Syntax Error — How to Fix"
description: "Fix CSS container query syntax errors. Learn the correct @container syntax, container-type declarations, and how browsers parse modern queries."
languages: ["css"]
error-types: ["syntax-error"]
severities: ["error"]
weight: 10
comments: true
---

## Why It Happens

Container queries use the `@container` at-rule to apply styles based on a parent container's size rather than the viewport. Syntax errors in this relatively new feature are common because the syntax has specific requirements that differ from media queries.

The most common cause is missing the `container-type` property on the parent element. Without declaring an element as a container, the `@container` query has nothing to reference and the browser ignores it entirely.

Another frequent cause is using incorrect query syntax within the `@container` block. Unlike media queries, container queries only support sizing conditions like `min-width`, `max-width`, `min-height`, and `max-height`. Using unsupported conditions like `orientation` or `prefers-color-scheme` causes parsing errors.

Container name syntax errors are frequent. If you use `@container sidebar (min-width: 400px)` but the container was declared without `container-name: sidebar`, the query targets the nearest unnamed ancestor container instead of the named one.

The order of properties in the `container-type` declaration matters. Some browsers require `container-type` to be declared before `container-name` for proper parsing, though this is less common in modern browsers.

Anonymous containers (containers without names) can cause confusion because `@container` without a name targets the nearest ancestor container, which may not be the one you intended.

## Common Error Messages

```
CSS Error: Invalid @container rule: missing container-type on parent element
```

```
CSS Warning: Unknown condition "orientation" in @container query
```

```
CSS Error: container-name "sidebar" does not match any declared container
```

```
CSS Warning: @container query ignored — no containing block established
```

## How to Fix It

### Declare the container with proper container-type

```css
.card-wrapper {
  container-type: inline-size;
  container-name: card;
}
```

### Use correct @container syntax with size conditions

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

### Name containers explicitly when multiple exist

```css
.sidebar {
  container-type: inline-size;
  container-name: sidebar;
}

.main-content {
  container-type: inline-size;
  container-name: main;
}

/* Target specific containers */
@container sidebar (min-width: 300px) {
  .sidebar-nav { display: block; }
}

@container main (min-width: 600px) {
  .content-grid { grid-template-columns: 1fr 1fr; }
}
```

### Use size instead of inline-size for height queries

```css
/* For height-based queries, use container-type: size */
.hero-section {
  container-type: size;
  container-name: hero;
  height: 50vh;
}

@container hero (min-height: 400px) {
  .hero-content { padding: 2rem; }
}
```

### Add fallback styles for unsupported browsers

```css
/* Base styles — no container query */
.card {
  display: flex;
  flex-direction: column;
}

/* Modern browsers with container query support */
@supports (container-type: inline-size) {
  .card-wrapper {
    container-type: inline-size;
  }
  
  @container (min-width: 400px) {
    .card {
      display: grid;
      grid-template-columns: 1fr 2fr;
    }
  }
}
```

## Common Scenarios

- Porting media queries to container queries and using media query syntax
- Building responsive components that need to adapt to different container sizes
- Working with nested containers where the wrong container is targeted

## Prevent It

- Always declare `container-type` on the parent element before using `@container`
- Use named containers when multiple containers exist to avoid ambiguity
- Test container queries in multiple browsers as support varies across versions
