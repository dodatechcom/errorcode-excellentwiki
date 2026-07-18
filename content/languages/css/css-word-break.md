---
title: "[Solution] CSS Word-Break Not Wrapping Long Words"
description: "Fix CSS word-break: break-all not wrapping text properly. Learn about word-wrap, overflow-wrap, and line-breaking strategies."
---

## What This Error Means

Your `word-break: break-all` is not wrapping long words or URLs as expected. Text may overflow its container or break at unexpected positions. The word-breaking behavior does not match the intended layout.

## Why It Happens

The most common cause is using `word-break` instead of `overflow-wrap`. These properties have different behaviors: `word-break: break-all` breaks words at any character, while `overflow-wrap: break-word` only breaks words when they would overflow.

Another frequent cause is combining `word-break` with `white-space: nowrap`. If white-space is set to nowrap, words will not wrap regardless of the word-break setting.

Using `word-break: normal` (the default) may not break very long words. The default behavior only breaks at normal word break opportunities.

The element may have `overflow: visible` which allows text to extend beyond the container instead of wrapping. For word-breaking to be visible, overflow must be hidden or scroll.

Finally, some CSS resets or frameworks may override word-break behavior with their own defaults.

## How to Fix It

### Use overflow-wrap for natural word breaking

```css
.text {
  overflow-wrap: break-word;
  word-wrap: break-word;  /* Legacy alias */
}
```

### Use word-break for aggressive breaking

```css
.text {
  word-break: break-all;  /* Breaks at any character */
}
```

### Use hyphens for language-appropriate breaking

```css
.text {
  hyphens: auto;
  -webkit-hyphens: auto;
  -ms-hyphens: auto;
  lang: en;
}
```

### Combine with overflow for proper truncation

```css
.container {
  max-width: 300px;
  overflow-wrap: break-word;
  overflow: hidden;
}
```

### Handle preformatted text

```css
pre {
  white-space: pre-wrap;
  overflow-wrap: break-word;
  word-break: break-word;
}
```

## Common Mistakes

- Confusing `word-break` with `overflow-wrap`
- Not setting `overflow: hidden` to make word-breaking visible
- Using `word-break: break-all` when `overflow-wrap: break-word` would be better
- Not handling preformatted text with `white-space: pre-wrap`
- Forgetting that `word-wrap` is an alias for `overflow-wrap`

## Related Pages

- [CSS Text Overflow](/languages/css/css-text-overflow/)
- [CSS Column Count](/languages/css/css-column-count/)
- [CSS Flexbox Centering](/languages/css/flexbox-centering/)
