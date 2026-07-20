---
title: "[Solution] GitHub Actions Jest Failure"
description: "Fix GitHub Actions Jest test failure errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Jest failures occur when JavaScript/TypeScript tests fail:

```
FAIL src/__tests__/api.test.js
  GET /api/users should return 200
    expect(received).toBe(expected)
```

## Common Causes

- Async operations not properly awaited.
- Mock setup issues.
- Flaky tests due to timing.

## How to Fix

**Run Jest with CI-specific options:**

```yaml
steps:
  - uses: actions/setup-node@v4
    with:
      node-version: 20
      cache: 'npm'
  - run: npm ci
  - run: npx jest --ci --forceExit --detectOpenHandles
```

## Examples

```yaml
steps:
  - run: npx jest --ci --coverage --forceExit
  - uses: actions/upload-artifact@v4
    if: failure()
    with:
      name: jest-screenshots
      path: coverage/
```
