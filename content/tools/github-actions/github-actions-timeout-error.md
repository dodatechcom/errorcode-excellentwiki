---
title: "GitHub Actions Job Timeout Error"
description: "GitHub Actions job exceeds the maximum execution time limit."
tools: ["github-actions"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# GitHub Actions Job Timeout Error

A GitHub Actions timeout error occurs when a job exceeds the maximum execution time. GitHub-hosted runners have a default timeout of 6 hours for jobs.

## Common Causes

- Long-running build or test process
- Infinite loop in a script
- Network operations hanging
- Large repository checkout taking too long

## How to Fix

### Set Job Timeout

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    timeout-minutes: 30
```

### Set Step Timeout

```yaml
steps:
  - name: Run tests
    run: npm test
    timeout-minutes: 10
```

### Optimize Long-Running Tasks

```yaml
# Use parallel execution
- name: Run tests in parallel
  run: npm run test:parallel
  timeout-minutes: 15
```

### Use Caching to Speed Up Builds

```yaml
- name: Cache node modules
  uses: actions/cache@v4
  with:
    path: ~/.npm
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
```

### Add Timeout to Network Operations

```yaml
- name: Download large file
  run: curl --max-time 60 -L -O https://example.com/large-file.zip
```

## Examples

```yaml
# Job took too long
Error: The job running on runner has exceeded the maximum execution time of 360 minutes.

# Fix: add timeout
jobs:
  build:
    runs-on: ubuntu-latest
    timeout-minutes: 30
```

## Related Errors

- [Runner Error]({{< relref "/tools/github-actions/github-actions-runner-error" >}}) — runner issues
- [Workflow Error]({{< relref "/tools/github-actions/workflow-failed" >}}) — workflow failure
