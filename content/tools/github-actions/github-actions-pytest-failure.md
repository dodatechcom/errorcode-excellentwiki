---
title: "[Solution] GitHub Actions Pytest Failure"
description: "Fix GitHub Actions pytest failure errors in Python workflow."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Pytest failures occur when Python tests fail:

```
FAILED tests/test_app.py::test_login - AssertionError
===== 1 failed, 42 passed in 0.5s =====
```

## Common Causes

- Test assertions failing.
- Missing test fixtures or setup.
- Database not available.

## How to Fix

**Run pytest with proper configuration:**

```yaml
steps:
  - uses: actions/setup-python@v5
    with:
      python-version: '3.11'
      cache: 'pip'
  - run: pip install -r requirements.txt
  - run: pytest --tb=short --junitxml=results.xml
```

## Examples

```yaml
steps:
  - run: pytest -v --tb=short -x
    env:
      DATABASE_URL: postgres://user:pass@localhost/test
```
