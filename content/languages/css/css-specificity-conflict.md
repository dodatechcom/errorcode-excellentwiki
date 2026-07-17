---
title: "[Solution] CSS Specificity Wars — Fix !important and Selector Conflicts"
description: "Fix CSS specificity conflicts with this step-by-step solution. Learn about specificity calculation, !important overrides, and maintaining a clean cascade."
---

## What This Error Means

Your styles are not being applied even though the CSS rule looks correct. Another rule with higher specificity is overriding it, or you have resorted to `!important` and now cannot override that rule either. The cascade has become a conflict between competing selectors.

## Why It Happens

CSS specificity determines which rule wins when multiple rules target the same element. Inline styles beat ID selectors, ID selectors beat class selectors, and class selectors beat element selectors. A rule like `#header .nav a` has higher specificity than `.nav a` because it includes an ID.

When two rules have equal specificity, the one defined later in the stylesheet wins. This can cause confusion when you add a rule expecting it to override an existing one but it appears earlier in the file.

The `!important` declaration bypasses specificity entirely and always wins. However, once you use `!important` on a property, overriding it requires either another `!important` or an inline style. This creates an escalation where every rule needs `!important` to compete, making the codebase difficult to maintain.

## How to Fix It

Reduce specificity by using simpler selectors. Prefer class selectors over ID selectors and avoid deeply nested selectors:

```css
/* High specificity - avoid */
#sidebar .widget .title { color: blue; }

/* Lower specificity - prefer */
.card-title { color: blue; }
```

Use CSS layers to manage the cascade explicitly. Define your base, component, and utility layers in order:

```css
@layer base, components, utilities;

@layer base {
  p { font-size: 1rem; }
}

@layer components {
  .intro { font-size: 1.25rem; }
}
```

Remove `!important` from your stylesheets and restructure selectors to use proper specificity. If you inherited a codebase full of `!important` rules, you can use `revert` or `revert-layer` as a reset:

```css
/* Override an !important without using another !important */
.element {
  color: initial;
}
```

Use DevTools to see which rules are matching and which are being overridden. The Computed panel shows the final applied value and the specificity of the winning rule.

## Common Mistakes

- Using `!important` as a quick fix which creates override chains
- Writing overly specific selectors like `body .container .wrapper .element`
- Not understanding that inline styles have the highest specificity
- Forgetting that `!important` on different properties does not conflict with each other
- Assuming order in the file does not matter when specificity is equal
- Mixing frameworks with custom styles where framework selectors are very specific

## Related Pages

- [CSS Variable Scope](/languages/css/css-variable-scope/)
- [Z-Index Not Working](/languages/css/z-index-not-working/)
- [CSS Grid Not Working](/languages/css/css-grid-not-working/)
- [Flexbox Centering](/languages/css/flexbox-centering/)
- [Media Query Not Applying](/languages/css/media-query-not-applying/)
