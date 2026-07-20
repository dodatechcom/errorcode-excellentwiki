---
title: "[Solution] Workflow Needs Dependency Cycle Error"
description: "Fix GitHub Actions needs dependency cycle errors in workflow jobs."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Dependency cycle errors occur when jobs reference each other in a circular `needs` chain:

```
Error: Job 'test' needs job 'deploy', but job 'deploy' also needs 'test'
Cycle detected: build -> test -> deploy -> build
```

## Common Causes

- Job A needs Job B, and Job B needs Job A.
- Complex dependency chains that inadvertently create cycles.

## How to Fix

**Restructure jobs to remove the cycle:**

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

  test:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

  deploy:
    needs: [build, test]
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
```

## Examples

```yaml
# Wrong - circular dependency
jobs:
  test:
    needs: deploy
  deploy:
    needs: test

# Correct - linear dependency
jobs:
  test:
    runs-on: ubuntu-latest
  deploy:
    needs: test
    runs-on: ubuntu-latest
```
