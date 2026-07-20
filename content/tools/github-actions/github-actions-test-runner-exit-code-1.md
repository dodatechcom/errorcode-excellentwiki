---
title: "[Solution] GitHub Actions Test Runner Exit Code 1"
description: "Fix GitHub Actions test runner exit code 1 failures."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Test runner failures return exit code 1, indicating test failures:

```
Error: Process completed with exit code 1.
FAIL src/__tests__/auth.test.ts (12.345 s)
```

## Common Causes

- Test assertions failing.
- Flaky tests due to timing or network issues.
- Missing test environment configuration.

## How to Fix

**Configure test environment:**

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_PASSWORD: test
        ports:
          - 5432:5432
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm test
        env:
          DATABASE_URL: postgres://postgres:test@localhost:5432/test
```

## Examples

```yaml
steps:
  - run: npm test -- --reporter=junit --output-reporter=test-results.xml
  - uses: actions/upload-artifact@v4
    if: failure()
    with:
      name: test-results
      path: test-results.xml
```
