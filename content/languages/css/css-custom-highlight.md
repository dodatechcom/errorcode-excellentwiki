---
title: "[Solution] CSS Custom Highlight API Not Working"
description: "Fix CSS ::highlight() pseudo-element not highlighting text. Learn about the Highlight API, custom highlights, and browser support."
---

## What This Error Means

Your CSS `::highlight()` pseudo-element is not producing visible highlights on text. The highlight should appear as a colored background behind selected text, but nothing is displayed.

## Why It Happens

The most common cause is browser support. The CSS Custom Highlight API (`::highlight()`) is only supported in Chrome 105+ and Edge 105+. Firefox and Safari do not support it yet.

Another frequent cause is not registering the highlight using the JavaScript Highlights API. CSS `::highlight(name)` requires a corresponding `CSS.highlights.set(name, highlight)` call in JavaScript.

Using an invalid highlight name in CSS that does not match the JavaScript registration causes the highlight to not appear.

The highlight may be applied but not visible because of competing styles. If the highlight's background-color is transparent or the same as the text color, it appears invisible.

Finally, the text range for the highlight may be empty or incorrect, causing nothing to be highlighted.

## How to Fix It

### Register highlights in JavaScript first

```javascript
// Register a custom highlight
const highlight = new Highlight();
CSS.highlights.set('my-highlight', highlight);

// Add a range to the highlight
const range = new Range();
range.setStart(textNode, 0);
range.setEnd(textNode, 10);
highlight.add(range);
```

### Style the highlight in CSS

```css
::highlight(my-highlight) {
  background-color: yellow;
  color: black;
}
```

### Check browser support

```css
@supports (background: highlight) {
  ::highlight(my-highlight) {
    background-color: yellow;
  }
}
```

### Use JavaScript to create highlights programmatically

```javascript
function highlightText(element, start, end, name) {
  const highlight = new Highlight();
  const range = document.createRange();
  range.setStart(element.firstChild, start);
  range.setEnd(element.firstChild, end);
  highlight.add(range);
  CSS.highlights.set(name, highlight);
}
```

### Provide fallback highlighting

```css
/* Fallback — use background color */
mark {
  background-color: yellow;
}

/* Enhanced — use highlight API */
@supports (background: highlight) {
  mark {
    background: transparent;
  }

  ::highlight(mark-highlight) {
    background-color: yellow;
  }
}
```

## Common Mistakes

- Using `::highlight()` without registering the highlight in JavaScript
- Not checking browser support for the Highlight API
- Using highlight names that do not match between CSS and JavaScript
- Not creating valid Range objects for the highlight
- Assuming `::highlight()` works like `<mark>` element

## Related Pages

- [CSS Custom Highlight](/languages/css/css-custom-highlight/)
- [CSS Nesting](/languages/css/css-nesting/)
- [CSS View Transitions](/languages/css/css-view-transitions/)
