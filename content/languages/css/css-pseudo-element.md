---
title: "[Solution] CSS Pseudo-Element Content Not Showing — ::before and ::after"
description: "Fix CSS ::before and ::after pseudo-elements not displaying. Learn about required properties, display types, and content requirements."
---

## What This Error Means

Your `::before` and `::after` pseudo-elements are not appearing on the page. The elements should be generated content but they are invisible or missing entirely.

## Why It Happens

The most common cause is missing the `content` property. Pseudo-elements require `content` to be set, even if it is an empty string. Without `content`, the pseudo-element does not render.

Another frequent cause is the parent element being a self-closing tag like `<img>`, `<input>`, or `<br>`. These elements cannot have children, including pseudo-elements.

Setting `display: none` on the pseudo-element or its parent hides it. Even if the pseudo-element is correctly defined, it will not appear if display is set to none.

The parent element having `overflow: hidden` may clip pseudo-elements that extend outside the parent's boundaries.

Using pseudo-elements on replaced elements (like `<img>`) does not work because replaced elements cannot have generated content.

Finally, the `content` property with `attr()` may fail if the attribute does not exist on the element.

## How to Fix It

### Always include the content property

```css
.element::before {
  content: "";
  display: block;
  width: 10px;
  height: 10px;
  background: red;
}
```

### Use display block or inline-block

```css
.element::after {
  content: " (required)";
  color: red;
  display: inline;
}
```

### Add pseudo-elements to non-replaced elements

```css
/* Wrong — img is a replaced element */
img::before { content: ""; }

/* Correct — div is not a replaced element */
div::before { content: ""; }
```

### Use attr() for dynamic content

```css
.element::before {
  content: attr(data-label);
  font-weight: bold;
}
```

### Handle overflow for positioned pseudo-elements

```css
.parent {
  position: relative;
  overflow: visible;
}

.parent::before {
  content: "";
  position: absolute;
  top: -10px;
  left: 0;
  width: 100%;
  height: 10px;
  background: blue;
}
```

## Common Mistakes

- Forgetting the `content` property
- Using pseudo-elements on self-closing tags
- Not setting `position` when using absolute positioning on pseudo-elements
- Not setting `display` when the pseudo-element needs block layout
- Using empty `content` without any other styling to make it visible

## Related Pages

- [CSS Placeholder Style](/languages/css/css-placeholder-style/)
- [CSS Text Overflow](/languages/css/css-text-overflow/)
- [CSS Position Sticky](/languages/css/css-position-sticky/)
