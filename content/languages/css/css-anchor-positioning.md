---
title: "[Solution] CSS Anchor Positioning Not Working — Fix Popover Placement"
description: "Fix CSS anchor positioning not working with this step-by-step solution. Learn about anchor(), position-anchor, and fallback positioning for popover elements."
---

## What This Error Means

The CSS anchor positioning API is not placing your popover, tooltip, or dropdown element relative to its anchor element. The positioned element appears at its default position or is hidden because the browser does not support or properly execute anchor positioning.

## Why It Happens

CSS anchor positioning is a new specification with limited browser support. Chrome 125 and Edge 125 added support, but Firefox and Safari do not yet support it. In unsupported browsers, the `anchor()` function and `position-anchor` property are ignored.

The positioned element must have `position: fixed` or `position: absolute` for anchor positioning to work. Without a positioned context, the anchor references have no effect.

The anchor element must be identified with `anchor-name`. If the anchor element lacks this property, the positioned element cannot reference it. Additionally, if the anchor element is removed from the DOM or hidden with `display: none`, the anchor reference breaks.

`position-anchor` on the positioned element must match the `anchor-name` on the anchor element. A mismatch causes the positioning to fail silently.

## How to Fix It

Define the anchor element with `anchor-name`:

```css
.tooltip-trigger {
  anchor-name: --trigger;
}
```

Position the popover relative to the anchor:

```css
.tooltip {
  position: fixed;
  position-anchor: --trigger;
  top: anchor(bottom);
  left: anchor(center);
  translate: -50% 8px;
}
```

Provide fallback positioning for unsupported browsers:

```css
.tooltip {
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
}

@supports (position-anchor: --trigger) {
  .tooltip {
    position: fixed;
    position-anchor: --trigger;
    top: anchor(bottom);
    left: anchor(center);
    translate: -50% 8px;
  }
}
```

Use inset-area for predefined zones:

```css
.tooltip {
  position: fixed;
  position-anchor: --trigger;
  inset-area: bottom;
}
```

Verify both elements exist in the same scrolling context. Anchor positioning does not work across different scroll containers.

## Common Mistakes

- Not setting `anchor-name` on the anchor element
- Mismatched names between `position-anchor` and `anchor-name`
- Using anchor positioning without `position: fixed` or `position: absolute`
- Forgetting a fallback for browsers that do not support the API
- Placing anchor and positioned elements in different scroll containers
- Assuming anchor positioning works with `position: relative` which is not supported

## Related Pages

- [Position Absolute Viewport](/languages/css/position-absolute-viewport/)
- [CSS Position Sticky](/languages/css/css-position-sticky/)
- [Z-Index Not Working](/languages/css/z-index-not-working/)
- [CSS View Transitions](/languages/css/css-view-transitions/)
- [CSS Has Selector](/languages/css/css-has-selector/)
