---
title: "Solved JavaScript xo Error — How to Fix"
date: 2026-03-20T18:05:40+00:00
description: "Learn how to resolve JavaScript XO linter opinionated configuration errors."
categories: ["javascript"]
keywords: ["xo error", "xo linter", "eslint config", "code quality", "xo config"]
error_types: ["runtime"]
severities: ["error"]
languages: ["javascript"]
weight: 5
comments: true
---

## Why It Happens

XO errors occur when code doesn't follow the opinionated style rules or configuration conflicts with project needs. XO wraps ESLint with sensible defaults.

Common causes include:
- Inconsistent code style
- Unused imports
- Missing type annotations
- Incorrect spacing
- Unsafe any usage

## Common Error Messages

```
  1:1   error  Unexpected var, use let or const          prefer-const
  2:5   error  Missing semicolon                          semi
  3:10  error  Strings must use singlequote               quotes
```

## How to Fix It

### 1. Run XO

Check and fix code.

```bash
# Check code
npx xo src/

# Auto-fix
npx xo --fix src/

# Check specific files
npx xo src/index.js
```

### 2. Configure XO

Customize rules.

```json
// package.json
{
  "xo": {
    "space": 2,
    "semi": false,
    "rules": {
      "capitalized-comments": "off"
    }
  }
}
```

### 3. Fix Common Issues

```javascript
// ❌ Wrong (XO style)
var name = 'John';
let unused = true;

// ✅ Correct (XO style)
const name = 'John'
```

## Common Scenarios

### Scenario 1: TypeScript

Use with TypeScript:

```json
{
  "xo": {
    "space": 2,
    "typescript": true
  }
}
```

### Scenario 2: React

Use with React:

```json
{
  "xo": {
    "space": 2,
    "extends": ["xo-react"]
  }
}
```

## Prevent It

- Run `npx xo --fix` to auto-fix issues
- Use editor integration for real-time linting
- Add `xo` to pre-commit hooks
- Don't override rules unless necessary
- Use TypeScript for better type safety