---
title: "Solved JavaScript standard Error — How to Fix"
date: 2026-03-20T18:00:30+00:00
description: "Learn how to resolve JavaScript StandardJS linter style guide errors."
categories: ["javascript"]
keywords: ["standard error", "standardjs", "code style", "linter", "javascript style"]
error_types: ["runtime"]
severities: ["error"]
languages: ["javascript"]
weight: 5
comments: true
---

## Why It Happens

StandardJS errors occur when code doesn't follow the opinionated style guide. Standard provides zero configuration linting.

Common causes include:
- Missing semicolons (standard requires no semicolons)
- Inconsistent indentation
- Unused variables
- Missing space after keywords
- Missing trailing commas

## Common Error Messages

```
  1:1   error  Unexpected var, use let or const          no-var
  2:5   error  Missing semicolon                          semi
  3:10  error  Strings must use singlequote               quotes
```

## How to Fix It

### 1. Run Standard

Check and fix code.

```bash
# Check code
npx standard src/

# Auto-fix
npx standard --fix src/

# Check specific files
npx standard src/index.js src/utils.js
```

### 2. Configure Standard

Customize rules.

```json
// package.json
{
  "standard": {
    "ignore": ["dist/", "coverage/"],
    "plugins": ["promise", "react"]
  }
}
```

### 3. Fix Common Issues

```javascript
// ❌ Wrong (Standard style)
var name = 'John';
if (name == "John") {
  console.log('hello');
}

// ✅ Correct (Standard style)
const name = 'John'
if (name === 'John') {
  console.log('hello')
}
```

## Common Scenarios

### Scenario 1: TypeScript

Use with TypeScript:

```bash
npx standard --parser @typescript-eslint/parser --plugin @typescript-eslint src/
```

### Scenario 2: React

Use with React:

```bash
npx standard --plugin react --parser @babel/eslint-parser src/
```

## Prevent It

- Run `npx standard --fix` to auto-fix issues
- Use editor integration for real-time linting
- Add `standard` to pre-commit hooks
- Don't configure rules (that defeats the purpose)
- Use `// eslint-disable-next-line` sparingly