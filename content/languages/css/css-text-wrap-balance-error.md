---
title: "[Solution] CSS text-wrap balance Error — How to Fix"
description: "Fix CSS text-wrap balance errors. Learn how to use text-wrap: balance for even line lengths, browser support, and fallback strategies for headlines."
languages: ["css"]
error-types: ["syntax-error"]
severities: ["warning"]
weight: 10
comments: true
---

## Why It Happens

The `text-wrap: balance` property tells the browser to distribute text across lines as evenly as possible. When the property is not applied correctly or the browser does not support it, headlines and paragraphs may have uneven line lengths.

The most common cause is browser support limitations. `text-wrap: balance` is supported in Chrome 114+, Firefox 121+, and Safari 17.4+. Older browsers ignore the property entirely.

Another frequent cause is incorrect property placement. `text-wrap: balance` must be applied to the text container element, not to individual text nodes or parent elements that do not directly contain the text.

The property only works on block-level elements. Applying it to inline elements or flex/grid children may not produce the expected results because the text wrapping context is different.

The property has performance implications for large amounts of text. Browsers may limit the balancing to a certain number of lines (typically 6) for performance reasons, which means very long paragraphs may not balance fully.

Using `text-wrap: balance` with `overflow: hidden` or `text-overflow: ellipsis` can cause conflicts because the balancing algorithm may produce different line breaks than expected.

## Common Error Messages

```
CSS Warning: text-wrap: balance not supported in this browser
```

```
CSS Error: text-wrap property not applicable to inline element
```

```
CSS Warning: text-wrap: balance limited to 6 lines for performance
```

```
CSS Error: text-wrap conflicts with white-space: nowrap
```

## How to Fix It

### Apply text-wrap: balance to block-level elements

```css
/* Correct — applied to the heading */
h1 {
  text-wrap: balance;
}

/* Wrong — applied to a span inside the heading */
h1 span {
  text-wrap: balance; /* May not work as expected */
}
```

### Use with appropriate text properties

```css
/* Good combination */
h1 {
  text-wrap: balance;
  max-width: 600px; /* Helps the balancing algorithm */
  margin: 0 auto;
}

/* Avoid conflicting properties */
h1 {
  text-wrap: balance;
  white-space: normal; /* Ensure wrapping is allowed */
  overflow-wrap: break-word; /* Allow long words to break */
}
```

### Provide fallback for unsupported browsers

```css
/* Base styles — balanced for modern browsers */
h1 {
  font-size: 2.5rem;
  line-height: 1.2;
  text-wrap: balance;
}

/* Fallback — older browsers get normal wrapping */
@supports not (text-wrap: balance) {
  h1 {
    text-wrap: pretty; /* Fallback — less aggressive balancing */
  }
}

/* Ultimate fallback — no text-wrap at all */
@supports not (text-wrap: balance) and not (text-wrap: pretty) {
  h1 {
    /* Normal wrapping — may be uneven */
  }
}
```

### Balance specific text elements

```css
/* Balance headlines and short paragraphs */
h1, h2, h3 {
  text-wrap: balance;
}

/* Balance short paragraphs only — long text stays normal */
.article-intro {
  text-wrap: balance;
  max-width: 40ch;
}

/* Avoid balancing long body text */
.article-body {
  text-wrap: pretty; /* Softer balancing for readability */
}

/* Never balance code or preformatted text */
pre, code {
  text-wrap: nowrap;
}
```

### Handle responsive balancing

```css
h1 {
  text-wrap: balance;
  font-size: clamp(1.5rem, 4vw, 3rem);
  max-width: 90vw;
}

/* On very narrow screens, the balancing may produce odd results */
@media (max-width: 480px) {
  h1 {
    text-wrap: pretty; /* Less aggressive on small screens */
    hyphens: auto; /* Help with long words */
  }
}
```

## Common Scenarios

- Improving the visual appearance of headlines and page titles
- Making card titles and section headings look more balanced
- Creating cleaner typography for hero sections and marketing pages

## Prevent It

- Only apply `text-wrap: balance` to short text like headlines and titles, not long paragraphs
- Test in multiple browsers as support is still being added
- Use `text-wrap: pretty` as a fallback for browsers that support `text-wrap` but not `balance`
