---
title: "[Solution] GitHub Actions Continue On Error Behavior"
description: "Fix GitHub Actions continue-on-error behavior issues."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

continue-on-error behavior issues occur when the error handling does not work as expected:

```
Warning: continue-on-error is true but the job still failed
```

## Common Causes

- `continue-on-error` only affects the step, not dependent jobs.
- Job-level `continue-on-error` does not prevent the workflow from reporting failure.

## How to Fix

**Use step-level continue-on-error:**

```yaml
steps:
  - name: Optional step
    continue-on-error: true
    run: flaky-command.sh
```

## Examples

```yaml
strategy:
  matrix:
    include:
      - node-version: 20
        experimental: false
      - node-version: 22
        experimental: true
  fail-fast: false
steps:
  - run: npm test
    continue-on-error: ${{ matrix.experimental }}
```
