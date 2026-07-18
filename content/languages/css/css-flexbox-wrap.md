---
title: "[Solution] CSS Flexbox Wrap Not Working — Fix Item Overflow"
description: "Fix CSS flex-wrap not working with this step-by-step solution. Learn why flex items overflow instead of wrapping and how to configure flex containers."
---

## What This Error Means

Your flex container is not wrapping its children to the next line. Instead, all flex items are squeezed onto a single row or column, causing overflow, horizontal scrolling, or items that shrink to illegible sizes.

## Why It Happens

By default, `flex-wrap` is set to `no-wrap`. This forces all flex items to stay on one line regardless of how much space they need. The browser compresses or overflows items to fit the container width. Setting `display: flex` alone does not enable wrapping.

Another cause is a fixed `width` or `min-width` on flex items that combined exceeds the container width. Even with `flex-wrap: wrap`, items with explicit dimensions will not wrap if the container has `overflow: hidden` or if a parent constraint prevents the container from expanding.

Flex items also have a default `min-width: auto` behavior, which prevents them from shrinking below their content size. This can prevent wrapping in tight containers.

## How to Fix It

Enable wrapping on the flex container:

```css
.container {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}
```

Use `flex-basis` to control when items wrap:

```css
.container {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}

.container .item {
  flex: 1 1 200px; /* Items will wrap when below 200px */
}
```

If items are still not wrapping, check for `min-width` constraints:

```css
.container .item {
  flex: 1 1 200px;
  min-width: 0; /* Override default min-width: auto */
}
```

Use `wrap-reverse` to wrap items in reverse order:

```css
.container {
  display: flex;
  flex-wrap: wrap-reverse;
}
```

For grid-based wrapping, consider CSS Grid as an alternative:

```css
.container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 1rem;
}
```

## Common Mistakes

- Forgetting to set `flex-wrap: wrap` since the default is `no-wrap`
- Setting `overflow: hidden` on the flex container which clips wrapped items
- Using fixed `width` values on items instead of `flex-basis` for responsive wrapping
- Not accounting for `min-width: auto` on flex items preventing shrink and wrap
- Mixing `flex-wrap` with `flex-direction: column` which changes the wrap axis

## Related Pages

- [Flexbox Centering](/languages/css/flexbox-centering/)
- [CSS Grid Not Working](/languages/css/css-grid-not-working/)
- [CSS Inline-Block Gap](/languages/css/css-inline-block-gap/)
- [Overflow Hidden Bleed](/languages/css/overflow-hidden-bleed/)
- [CSS Scroll Snap](/languages/css/css-scroll-snap/)
