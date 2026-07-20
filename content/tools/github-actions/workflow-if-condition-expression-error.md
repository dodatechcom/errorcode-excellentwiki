---
title: "[Solution] Workflow If Condition Expression Error"
description: "Fix GitHub Actions 'if' condition expression errors in workflow steps or jobs."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

If condition expression errors occur when an `if` condition contains invalid expression syntax:

```
Error: .github/workflows/ci.yml: Invalid expression in if condition
```

## Common Causes

- Using `${{ }}` syntax inside an `if` that already evaluates expressions.
- Incorrect operator usage (`==` vs `=`).
- Referencing undefined variables or contexts.

## How to Fix

**Use the expression syntax correctly:**

```yaml
steps:
  - name: Deploy
    if: github.ref == 'refs/heads/main' && success()
    run: echo "Deploying"

  - name: Skip
    if: ${{ !cancelled() }}
    run: echo "Runs even if earlier steps fail"
```

## Examples

```yaml
# Wrong - invalid operator
if: github.event_name = 'push'

# Correct
if: github.event_name == 'push'
```
