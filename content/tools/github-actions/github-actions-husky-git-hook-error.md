---
title: "[Solution] GitHub Actions Husky Git Hook Error"
description: "Fix GitHub Actions Husky git hook errors in CI."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Husky errors occur when git hooks interfere with CI operations:

```
Error: husky - .git/husky/pre-commit command not found
```

## Common Causes

- Husky hooks not disabled in CI.
- Hook script references local tools not installed.

## How to Fix

**Disable Husky in CI:**

```yaml
env:
  HUSKY: 0
steps:
  - uses: actions/checkout@v4
  - run: npm ci
```

## Examples

```yaml
steps:
  - uses: actions/checkout@v4
  - run: npm ci
    env:
      HUSKY: 0
```
