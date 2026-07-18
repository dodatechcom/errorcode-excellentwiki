---
title: "[Solution] CSS Text-Overflow Ellipsis Not Truncating Text"
description: "Fix CSS text-overflow: ellipsis not showing truncation. Learn about overflow, white-space, and width constraints for text truncation."
---

## What This Error Means

Your `text-overflow: ellipsis` is not truncating text or showing the ellipsis character. Text may overflow its container, wrap to multiple lines, or simply be cut off without the "..." indicator.

## Why It Happens

The most common cause is missing `overflow: hidden` or `overflow: nowrap`. The `text-overflow` property only works when the overflow is hidden and the text is prevented from wrapping.

Another frequent cause is no width constraint on the element. Without a fixed width, `max-width`, or `width` on the element, the text has unlimited space and never overflows.

The element may have `white-space: normal` which allows text to wrap. For single-line ellipsis, the text must be on one line with `white-space: nowrap`.

Multiple-line truncation requires `-webkit-line-clamp` which is not standard CSS. Without this property, multi-line ellipsis does not work with `text-overflow`.

Using `text-overflow` on inline elements does not work. The element must be a block or inline-block element.

## How to Fix It

### Use all three required properties

```css
.truncate {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  width: 200px;  /* Or max-width */
}
```

### Use max-width for responsive truncation

```css
.truncate {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  max-width: 300px;
  width: 100%;
}
```

### Use -webkit-line-clamp for multi-line truncation

```css
.multi-line-truncate {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}
```

### Ensure the element is a block element

```css
/* Wrong — inline element */
span {
  text-overflow: ellipsis;  /* Does not work */
}

/* Correct — block element */
div {
  display: block;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
```

### Use flexbox for truncation in flex layouts

```css
.flex-item {
  min-width: 0;  /* Allow flex item to shrink */
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
```

## Common Mistakes

- Not including `overflow: hidden` with `text-overflow: ellipsis`
- Not setting `white-space: nowrap` for single-line truncation
- Using `text-overflow` on inline elements instead of block elements
- Not setting a width or max-width on the element
- Trying to use standard CSS for multi-line truncation

## Related Pages

- [CSS Word Break](/languages/css/css-word-break/)
- [CSS Text Overflow](/languages/css/css-text-overflow/)
- [CSS Flexbox Centering](/languages/css/flexbox-centering/)
