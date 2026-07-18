---
title: "[Solution] CSS Anchor Positioning Error — How to Fix"
description: "Fix CSS anchor positioning errors. Learn how to define anchors, position elements relative to them, and handle fallback positioning in modern CSS."
languages: ["css"]
error-types: ["syntax-error"]
severities: ["error"]
weight: 10
comments: true
---

## Why It Happens

CSS anchor positioning allows you to position elements relative to other elements called anchors. When the anchor relationship is not properly defined or the positioning properties are incorrect, the positioned element either does not appear or appears in the wrong location.

The most common cause is missing the `anchor-name` property on the anchor element. Without an anchor name, the positioned element has nothing to reference.

Another frequent cause is using `position-anchor` on the wrong element. The element being positioned must have `position-anchor` set to the name of its anchor, not the other way around.

The `anchor()` function in positioning properties must be used with valid anchor names. If the name in `top: anchor(bottom)` does not match any declared `anchor-name`, the positioning fails.

Inset properties like `top`, `right`, `bottom`, and `left` used with anchor positioning override normal positioning. If you use both `position: absolute` and `anchor()` functions, the anchor positioning takes precedence.

Fallback positioning using `position-try-fallbacks` requires valid try blocks. If the try block references an anchor that does not exist, the fallback is ignored.

The anchor element must be in the DOM and visible for positioning to work. Anchors that are hidden with `display: none` or removed from the document cannot be used as positioning references.

## Common Error Messages

```
CSS Error: anchor-name "tooltip-anchor" not found on any element
```

```
CSS Error: position-anchor "button-anchor" does not match declared anchor-name
```

```
CSS Warning: anchor() function references non-existent anchor "missing-anchor"
```

```
CSS Error: position-try-fallbacks references invalid anchor or fallback name
```

## How to Fix It

### Declare anchor-name on the anchor element

```css
.button {
  anchor-name: --my-button;
}

.tooltip {
  position: fixed;
  position-anchor: --my-button;
  top: anchor(bottom);
  left: anchor(center);
}
```

### Use the correct position-anchor relationship

```css
/* Anchor element */
.trigger {
  anchor-name: --trigger;
  position: relative;
}

/* Positioned element */
.popup {
  position: fixed;
  position-anchor: --trigger;
  top: anchor(bottom);
  left: anchor(left);
  margin-top: 8px;
}
```

### Add fallback positioning

```css
.tooltip {
  position: fixed;
  position-anchor: --my-button;
  top: anchor(bottom);
  left: anchor(center);
  transform: translateX(-50%);
  
  /* Fallback if no space below */
  position-try-fallbacks: flip-block, flip-inline;
}

@position-try flip-block {
  top: anchor(top);
  bottom: anchor(bottom);
}
```

### Handle multiple anchors

```css
.card {
  anchor-name: --card;
}

.card-title {
  anchor-name: --card-title;
}

/* Position relative to card */
.card-badge {
  position: absolute;
  position-anchor: --card;
  top: anchor(top);
  right: anchor(right);
}

/* Position relative to card title */
.card-subtitle {
  position: absolute;
  position-anchor: --card-title;
  top: anchor(bottom);
  left: anchor(left);
}
```

### Use anchor scopes for isolation

```css
/* Each scope has its own anchor names */
.scope-1 {
  anchor-scope: --my-anchor;
}

.scope-2 {
  anchor-scope: --my-anchor;
}

/* Different anchors in different scopes */
.scope-1 .anchor { anchor-name: --my-anchor; }
.scope-1 .tooltip { position-anchor: --my-anchor; }

.scope-2 .anchor { anchor-name: --my-anchor; }
.scope-2 .tooltip { position-anchor: --my-anchor; }
```

## Common Scenarios

- Building tooltips that appear near their trigger buttons
- Creating dropdown menus that position themselves relative to menu items
- Implementing popover components that need fallback positioning when space is limited

## Prevent It

- Always declare `anchor-name` on the anchor element before using it in positioning
- Use the `position-try-fallbacks` property to handle edge cases where the anchor is off-screen
- Test anchor positioning in Chrome 125+ as this feature is still experimental in other browsers
