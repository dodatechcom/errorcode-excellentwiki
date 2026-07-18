---
title: "[Solution] CSS Parsing Error Missing Semicolons — Fix Syntax Failures"
description: "Fix CSS parsing error from missing semicolons with this step-by-step solution. Learn how browsers handle missing semicolons and how to debug CSS syntax."
---

## What This Error Means

Your CSS file contains a parsing error caused by a missing semicolon at the end of a property declaration. The browser either ignores the entire rule, ignores specific properties, or applies unexpected styles because it cannot determine where one declaration ends and the next begins.

## Why It Happens

CSS uses semicolons to separate property declarations within a rule block. When a semicolon is missing, the browser attempts to parse the next property as part of the previous one. This produces a syntax error, and depending on the browser, it may skip the entire rule or only the malformed declaration.

For example, writing `color: red background: blue` causes the browser to try parsing `background: blue` as part of the `color` value, which fails silently. The `background` property is never applied.

Preprocessors like Sass or Less may mask missing semicolons during compilation, but the compiled CSS output can still contain errors that browsers reject. Minified CSS is especially prone to missing semicolons if a build tool strips them incorrectly.

## How to Fix It

Ensure every property declaration ends with a semicolon:

```css
/* Wrong - missing semicolon */
.card {
  color: red
  background: blue;
}

/* Correct */
.card {
  color: red;
  background: blue;
}
```

The last declaration in a block does not require a semicolon, but always include it for safety:

```css
/* Valid but risky */
.card {
  color: red;
  background: blue
}

/* Safer */
.card {
  color: red;
  background: blue;
}
```

Use a CSS linter like Stylelint to catch missing semicolons automatically:

```bash
npx stylelint "**/*.css"
```

Check browser DevTools for ignored rules. The Console tab shows warnings like "Invalid property value" or "Declaration dropped" that point to the problematic rule.

For minified CSS, verify your build tool preserves semicolons. In a Sass file, ensure each declaration is properly terminated:

```scss
// Sass does not require semicolons in indented syntax
.card
  color: red
  background: blue

// But SCSS syntax does require them
.card {
  color: red;
  background: blue;
}
```

## Common Mistakes

- Omitting the semicolon on the last property before a closing brace, then adding a new property later
- Copying CSS from design tools that produce comments between declarations without semicolons
- Minification tools that strip trailing semicolons but break when lines are joined
- Mixing Sass indented syntax with SCSS syntax in the same project
- Not validating CSS after editing, especially when making quick one-line changes

## Related Pages

- [CSS Specificity Conflict](/languages/css/css-specificity-conflict/)
- [CSS Variable Scope](/languages/css/css-variable-scope/)
- [CSS Transition Not Working](/languages/css/css-transition-not-working/)
- [CSS Backdrop Filter](/languages/css/css-backdrop-filter/)
- [CSS Unit Mismatch](/languages/css/css-unit-mismatch/)
