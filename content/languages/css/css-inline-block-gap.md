---
title: "[Solution] CSS Inline-Block Gap and Spacing Issue — Fix Unexpected Whitespace"
description: "Fix CSS inline-block spacing gap with this step-by-step solution. Learn why whitespace appears between inline-block elements and how to remove it."
---

## What This Error Means

You have elements set to `display: inline-block` and unwanted gaps or spaces appear between them. These gaps cause layout misalignment, especially in navigation bars, image galleries, and button groups where elements should sit flush against each other.

## Why It Happens

Inline-block elements behave like inline elements with block-level formatting. Because they are treated as inline content, whitespace characters in the HTML source code (spaces, tabs, newlines) are rendered as visible gaps between the elements. A single space in the HTML between two inline-block divs produces a gap equivalent to the font size of the parent element.

This is not a CSS bug. The browser is correctly rendering the whitespace that exists in the markup. The gap width varies depending on the font and font-size of the parent container.

## How to Fix It

Remove whitespace in the HTML by placing tags adjacent to each other:

```html
<!-- Gap appears -->
<div class="box">A</div>
<div class="box">B</div>

<!-- No gap -->
<div class="box">A</div><div class="box">B</div>
```

Use negative margin to counteract the gap:

```css
.box {
  display: inline-block;
  width: 100px;
  margin-right: -4px; /* Adjusts for the whitespace gap */
}
```

Set the parent font-size to zero and reset it on the children:

```css
.container {
  font-size: 0;
}

.container .box {
  display: inline-block;
  font-size: 16px; /* Reset font-size on children */
  width: 100px;
}
```

Use `letter-spacing` or `word-spacing` on the parent:

```css
.container {
  display: flex; /* Alternative: just use flexbox instead */
  gap: 0;
}
```

The cleanest modern approach is replacing inline-block with flexbox:

```css
.container {
  display: flex;
}

.container .box {
  flex: 0 0 100px;
}
```

## Common Mistakes

- Not realizing the gap is caused by whitespace in the HTML source, not CSS
- Using negative margin values that are too aggressive and cause overlapping
- Forgetting to reset font-size on children after setting the parent to font-size: 0
- Switching to flexbox without removing the old inline-block styles that may conflict
- Ignoring the gap on responsive layouts where the parent font-size changes

## Related Pages

- [Flexbox Centering](/languages/css/flexbox-centering/)
- [CSS Flexbox Wrap](/languages/css/css-flexbox-wrap/)
- [CSS Grid Not Working](/languages/css/css-grid-not-working/)
- [CSS Unit Mismatch](/languages/css/css-unit-mismatch/)
- [CSS Specificity Conflict](/languages/css/css-specificity-conflict/)
