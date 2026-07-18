---
title: "[Solution] CSS :has() Selector Error — How to Fix"
description: "Fix CSS :has() selector errors. Learn how to use the parent selector correctly, combine it with other selectors, and avoid performance pitfalls."
languages: ["css"]
error-types: ["syntax-error"]
severities: ["warning"]
weight: 10
comments: true
---

## Why It Happens

The `:has()` pseudo-class selects elements based on whether they contain specific descendants or meet certain conditions related to their children. When the selector syntax is incorrect or the browser does not support it, styles fail to apply.

The most common cause is incorrect selector syntax inside `:has()`. The selector must be a valid CSS selector, and complex selectors with combinators need proper syntax.

Another frequent cause is browser support limitations. `:has()` is supported in Chrome 105+, Safari 15.4+, and Firefox 121+. Older browsers do not recognize the selector and ignore the entire rule.

The `:has()` selector is limited in what it can match. It cannot match pseudo-elements, and some complex combinators may not work as expected in all browsers.

Performance concerns arise because `:has()` can create selector chains that are difficult for the browser to optimize. While modern browsers handle simple `:has()` selectors well, deeply nested or overly complex selectors can cause slowdowns.

The selector cannot be used in `@supports` to detect support reliably because `:has()` is recognized syntactically even if the browser does not fully support it.

## Common Error Messages

```
CSS Warning: :has() selector not supported in this browser version
```

```
CSS Error: Invalid selector inside :has() — pseudo-elements not allowed
```

```
CSS Warning: :has() with complex combinators may cause performance issues
```

```
CSS Error: Selector ":has()" is not valid CSS
```

## How to Fix It

### Use basic :has() selectors correctly

```css
/* Style a card that contains an image */
.card:has(img) {
  display: grid;
  grid-template-columns: 1fr 1fr;
}

/* Style a form that has an invalid input */
form:has(:invalid) {
  border: 2px solid red;
}

/* Style a list that has more than 5 items */
ul:has(li:nth-child(n+6)) {
  columns: 2;
}
```

### Combine :has() with other selectors

```css
/* Style a section that contains an h2 but not an h3 */
section:has(h2):not(:has(h3)) {
  padding: 2rem;
}

/* Style a parent element based on child state */
.parent:has(.child.active) {
  background: lightblue;
}

/* Style a container that has a specific direct child */
.container:has(> .hero) {
  min-height: 100vh;
}
```

### Add browser fallbacks

```css
/* Fallback for browsers without :has() support */
.card-with-image {
  /* Default styles — always apply */
}

/* Modern browsers override with :has() */
@supports selector(:has(*)) {
  .card:has(img) {
    display: grid;
    grid-template-columns: 1fr 1fr;
  }
}
```

### Use :has() for conditional styling

```css
/* Show a label only when the input has a value */
label:has(+ input:not(:placeholder-shown)) {
  transform: translateY(-1.5rem);
  font-size: 0.75rem;
}

/* Style a navigation that is currently active */
nav:has(.active-link) {
  background: var(--primary-color);
}

/* Adjust layout when a sidebar exists */
.page:has(.sidebar) {
  display: grid;
  grid-template-columns: 250px 1fr;
}
```

### Avoid overly complex :has() chains

```css
/* Avoid — potentially slow */
.page:has(.header:has(.logo:has(img))) {
  /* ... */
}

/* Prefer — simpler and faster */
.page:has(.header .logo img) {
  /* ... */
}
```

## Common Scenarios

- Styling form elements based on whether they contain invalid inputs
- Creating layouts that adapt based on whether certain child elements exist
- Building component styles that change based on child element state

## Prevent It

- Test `:has()` selectors in multiple browsers as support is relatively new
- Keep `:has()` selectors simple and avoid deeply nested selector chains
- Use `@supports selector(:has(*))` to provide fallbacks for older browsers
