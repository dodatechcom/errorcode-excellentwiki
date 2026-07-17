---
title: "GitHub Actions Job Timeout Exceeded"
description: "GitHub Actions workflow job exceeds the configured timeout limit."
tools: ["github-actions"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# GitHub Actions — Job Timeout Exceeded

This error occurs when a GitHub Actions job exceeds its configured timeout limit. The default timeout is 360 minutes (6 hours) for GitHub-hosted runners.

## Common Causes

- Long-running test suite
- Infinite loop in build script
- Slow network operations
- Resource-intensive build steps
- Default timeout too short

## How to Fix

### Set Custom Timeout

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    timeout-minutes: 30
    steps:
      - uses: actions/checkout@v4
```

### Reduce Test Suite Duration

```yaml
- run: npm test -- --maxWorkers=4
```

### Add Timeout to Individual Steps

```yaml
steps:
  - name: Run tests
    timeout-minutes: 15
    run: npm test
```

### Optimize Long-Running Steps

```yaml
steps:
  - name: Build
    timeout-minutes: 10
    run: npm run build
```

### Set Repository-Level Timeout

```yaml
# .github/workflows/ci.yml
jobs:
  build:
    timeout-minutes: 60
```

### Use Caching to Reduce Build Time

```yaml
- uses: actions/cache@v4
  with:
    path: ~/.npm
    key: npm-${{ hashFiles('**/package-lock.json') }}
```

## Examples

```text
The job running on runner ubuntu-latest has exceeded the maximum
execution time of 360 minutes.
```

## Related Errors

- [GitHub Actions Runner Error]({{< relref "/tools/github-actions/github-actions-runner-error" >}}) — runner issues
- [GitHub Actions Matrix Error]({{< relref "/tools/github-actions/github-actions-matrix-error" >}}) — matrix strategy issues
- [GitHub Actions Cache Error]({{< relref "/tools/github-actions/github-actions-cache-error" >}}) — cache restore failure
