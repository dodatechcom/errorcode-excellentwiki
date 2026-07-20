---
title: "[Solution] GitHub Actions Job Timeout"
description: "Fix GitHub Actions job timeout exceeded errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Job timeout errors occur when a job exceeds the default 6-hour timeout:

```
Error: The job running on runner has exceeded the maximum execution time
```

## Common Causes

- Long-running test suite.
- Infinite loop in workflow script.
- Network timeout causing hang.

## How to Fix

**Set explicit timeout:**

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    timeout-minutes: 30
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm test
```

## Examples

```yaml
# Default is 360 minutes (6 hours)
jobs:
  test:
    timeout-minutes: 60
```
