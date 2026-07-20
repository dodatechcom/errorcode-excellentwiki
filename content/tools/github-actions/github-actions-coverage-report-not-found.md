---
title: "[Solution] GitHub Actions Coverage Report Not Found"
description: "Fix GitHub Actions coverage report not found errors after tests."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Coverage report errors occur when the expected coverage file is not generated:

```
Error: No coverage report found at ./coverage/lcov.info
```

## Common Causes

- Test command does not generate coverage.
- Wrong path for coverage report.

## How to Fix

**Configure coverage in your test command:**

```yaml
steps:
  - run: npm test -- --coverage --coverageReporters=lcov
  - uses: codecov/codecov-action@v4
    with:
      files: ./coverage/lcov.info
```

## Examples

```yaml
steps:
  - run: pytest --cov=src --cov-report=xml
  - uses: codecov/codecov-action@v4
    with:
      files: coverage.xml
```
