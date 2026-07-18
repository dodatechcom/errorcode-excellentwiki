---
title: "Solved JavaScript stylelint Error — How to Fix"
date: 2026-03-20T18:15:00+00:00
description: "Learn how to resolve JavaScript Stylelint CSS linter configuration and rule errors."
categories: ["javascript"]
keywords: ["stylelint error", "css linter", "stylelint config", "css linting", "stylelint rules"]
error_types: ["runtime"]
severities: ["error"]
languages: ["javascript"]
weight: 5
comments: true
---

## Why It Happens

Stylelint errors occur when CSS doesn't follow configured rules, syntax is invalid, or plugins conflict. Stylelint standardizes CSS code style.

Common causes include:
- Invalid CSS syntax
- Unknown property
- Invalid selector
- Missing vendor prefixes
- Inconsistent naming

## Common Error Messages

```
src/styles.css:1:1: Unexpected unknown property "display" (property-no-unknown)
src/styles.css:2:1: Unexpected empty block (block-no-empty)
```

## How to Fix It

### 1. Run Stylelint

Check and fix CSS.

```bash
# Check code
npx stylelint "src/**/*.css"

# Auto-fix
npx stylelint "src/**/*.css" --fix

# Check specific files
npx stylelint src/styles.css
```

### 2. Configure Stylelint

Customize rules.

```javascript
// stylelint.config.js
export default {
  extends: ["stylelint-config-standard"],
  rules: {
    "color-hex-length": "long",
    "font-family-name-quotes": "always-where-recommended",
    "selector-class-pattern": null,
    "selector-id-pattern": null
  },
  ignoreFiles: ["dist/", "node_modules/"]
};
```

### 3. Fix Common Issues

```css
/* ❌ Wrong */
.foo {
  color: #ff0000;
  display: flex;
}

/* ✅ Correct */
.foo {
  color: #ff0000;
  display: flex;
}
```

## Common Scenarios

### Scenario 1: SCSS

Use with SCSS:

```javascript
export default {
  extends: ["stylelint-config-standard-scss"],
  rules: {
    "scss/no-global-function-name": null
  }
};
```

### Scenario 2: Tailwind

Use with Tailwind:

```javascript
export default {
  extends: ["stylelint-config-standard"],
  plugins: ["stylelint-order"],
  rules: {
    "order/properties-alphabetical-order": true
  }
};
```

## Prevent It

- Run `npx stylelint --fix` to auto-fix issues
- Use editor integration for real-time linting
- Add `stylelint` to pre-commit hooks
- Use `stylelint-config-standard` as base
- Ignore generated files in `.stylelintignore`