---
title: "Solved JavaScript jshint Error — How to Fix"
date: 2026-03-20T18:10:50+00:00
description: "Learn how to resolve JavaScript JSHint linter configuration and warning errors."
categories: ["javascript"]
keywords: ["jshint error", "jshint config", "code quality", "javascript linter", "jshint warnings"]
error_types: ["runtime"]
severities: ["error"]
languages: ["javascript"]
weight: 5
comments: true
---

## Why It Happens

JSHint errors occur when code doesn't follow configured rules or uses features not recognized. JSHint is a more flexible linter than ESLint.

Common causes include:
- Undefined variables
- Missing semicolons
- Unused variables
- Missing == checks
- ES6+ features not enabled

## Common Error Messages

```
src/index.js: line 1, col 5, 'define' is not defined.
src/index.js: line 2, col 1, Missing semicolon.
src/index.js: line 3, col 1, 'myFunc' is defined but never used.
```

## How to Fix It

### 1. Run JSHint

Check code.

```bash
# Check code
npx jshint src/

# Check specific files
npx jshint src/index.js

# Auto-fix (limited)
npx jshint --fix src/
```

### 2. Configure JSHint

Customize rules.

```json
// .jshintrc
{
  "curly": true,
  "eqeqeq": true,
  "immed": true,
  "latedef": "nofunc",
  "newcap": true,
  "noarg": true,
  "undef": true,
  "unused": true,
  "strict": true,
  "globals": {
    "window": true,
    "document": true
  },
  "esversion": 11
}
```

### 3. Fix Common Issues

```javascript
// ❌ Wrong
var name = 'John'
if (name == "John") {
  console.log('hello')
}

// ✅ Correct
var name = 'John'
if (name === 'John') {
  console.log('hello')
}
```

## Common Scenarios

### Scenario 1: Browser Code

Configure for browser:

```json
{
  "browser": true,
  "devel": true,
  "esversion": 11
}
```

### Scenario 2: Node.js

Configure for Node.js:

```json
{
  "node": true,
  "esversion": 11
}
```

## Prevent It

- Run `npx jshint` to check code
- Use editor integration for real-time linting
- Add `jshint` to CI pipeline
- Use `/* jshint ignore:start */` for specific sections
- Keep `.jshintrc` in project root