---
title: "[Solution] Workflow Container Syntax Error"
description: "Fix GitHub Actions container syntax errors in job configuration."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Container syntax errors occur when the `container` configuration is malformed:

```
Error: .github/workflows/ci.yml: Invalid container configuration
```

## Common Causes

- Missing `image` key under `container`.
- Invalid `credentials` format.
- Port mapping syntax errors.

## How to Fix

**Use proper container syntax:**

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    container:
      image: node:20
      env:
        NODE_ENV: test
      ports:
        - 8080:8080
      volumes:
        - /tmp:/tmp
      options: --cpus 1
    steps:
      - uses: actions/checkout@v4
      - run: node --version
```

## Examples

```yaml
# Wrong - missing image
container:
  env:
    NODE_ENV: test

# Correct
container:
  image: node:20
  env:
    NODE_ENV: test
```
