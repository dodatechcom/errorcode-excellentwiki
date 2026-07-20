---
title: "[Solution] Workflow Steps Requires Uses Or Run Error"
description: "Fix GitHub Actions error when steps must have either 'uses' or 'run'."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Each step in a GitHub Actions workflow must contain either a `uses` (for actions) or `run` (for shell commands) key:

```
Error: .github/workflows/ci.yml: steps[0] must have one of 'uses' or 'run'
```

## Common Causes

- Step defined without `uses` or `run`.
- `uses` and `run` are both missing due to a typo.
- Step has `name` only with no executable content.

## How to Fix

**Add either `uses` or `run` to every step:**

```yaml
steps:
  - name: Checkout code
    uses: actions/checkout@v4

  - name: Run tests
    run: npm test

  - name: Build project
    run: npm run build
```

## Examples

```yaml
# Wrong - no uses or run
steps:
  - name: Checkout code

# Correct - has uses
steps:
  - name: Checkout code
    uses: actions/checkout@v4

# Correct - has run
steps:
  - name: Print hello
    run: echo "Hello"
```
