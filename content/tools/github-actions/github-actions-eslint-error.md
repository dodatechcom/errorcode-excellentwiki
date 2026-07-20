---
title: "[Solution] GitHub Actions ESLint Error"
description: "Fix GitHub Actions ESLint errors in CI workflow."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

ESLint errors cause CI failures when code does not pass linting:

```
Error: src/index.ts
  10:5  error  Unexpected any  @typescript-eslint/no-explicit-any
```

## Common Causes

- New lint rules added to the project.
- Code pushed without running linter locally.

## How to Fix

**Run ESLint in the workflow:**

```yaml
steps:
  - uses: actions/setup-node@v4
    with:
      node-version: 20
      cache: 'npm'
  - run: npm ci
  - run: npx eslint . --ext .ts,.js
```

## Examples

```yaml
steps:
  - run: npx eslint . --max-warnings=0
  - run: npx prettier --check .
```
