---
title: "[Solution] Workflow Jobs Syntax Error"
description: "Fix GitHub Actions jobs syntax errors when the jobs section is malformed."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Jobs syntax errors occur when the `jobs` section of the workflow is invalid:

```
Error: Invalid workflow file .github/workflows/ci.yml
jobs should be a map, got a string
```

## Common Causes

- `jobs` is defined as a string instead of a map of job objects.
- Missing job name or ID.
- Incorrect nesting under `jobs`.

## How to Fix

**Ensure `jobs` is a map:**

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

  test:
    runs-on: ubuntu-latest
    needs: build
    steps:
      - uses: actions/checkout@v4
```

## Examples

```yaml
# Wrong - jobs is a string
jobs: "build"

# Correct - jobs is a map
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
```
