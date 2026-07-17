---
title: "[Solution] GitHub Actions Job Exceeded Timeout"
description: "Fix GitHub Actions timeout errors. Resolve jobs that exceed the configured timeout limit."
tools: ["github-actions"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# GitHub Actions Job Exceeded Timeout

A job timeout error occurs when a workflow job runs longer than the configured `timeout-minutes` value. The default timeout is 360 minutes (6 hours) for GitHub-hosted runners.

## Common Causes

- A step in the job is stuck (e.g., waiting for user input)
- The build or test suite is genuinely slow
- A network dependency is hanging (e.g., package registry unreachable)
- An infinite loop in a script step

## How to Fix

### Set an Appropriate Timeout

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    timeout-minutes: 30
    steps:
      - uses: actions/checkout@v4
      - run: npm ci && npm test
```

### Identify the Slow Step

```yaml
# Break long jobs into timed steps
jobs:
  build:
    steps:
      - name: Install dependencies
        timeout-minutes: 5
        run: npm ci
      - name: Run tests
        timeout-minutes: 20
        run: npm test
```

### Increase Timeout for Long-Running Jobs

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    timeout-minutes: 120  # 2 hours for large deployments
```

### Add Timeout to Shell Commands

```yaml
steps:
  - name: Run slow process
    run: |
      timeout 600 ./long-running-script.sh
```

## Examples

```yaml
# Default 360min timeout exceeded
# Error: The job running on runner has exceeded the maximum execution time
# Fix: set timeout-minutes: 30 or fix the hanging step

# Stuck package install
# Error: Job timed out after 30 minutes
# Fix: use --prefer-offline or check registry availability
```

## Related Errors

- [Matrix Error]({{< relref "/tools/github-actions/matrix-error" >}}) — matrix configuration issue
- [Step Failed]({{< relref "/tools/github-actions/step-failed" >}}) — individual step failure
