---
title: "GitHub Actions Matrix Strategy Error"
description: "GitHub Actions matrix strategy configuration error prevents parallel job execution."
tools: ["github-actions"]
error-types: ["build-error"]
severities: ["error"]
tags: ["github-actions", "matrix", "strategy", "parallel", "combination"]
weight: 5
---

# GitHub Actions Matrix Strategy Error

A matrix strategy error occurs when the GitHub Actions matrix configuration is invalid, causing the workflow to fail during job creation. The matrix defines combinations of inputs for parallel job execution.

## Common Causes

- Invalid matrix values (null, empty array)
- Matrix variable not properly referenced
- Too many combinations exceeding rate limits
- Matrix values contain invalid characters

## How to Fix

### Define Valid Matrix

```yaml
jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        node-version: [16, 18, 20]
      fail-fast: false
```

### Fix Matrix Variable References

```yaml
# Correct
- run: node --version
  env:
    NODE_VERSION: ${{ matrix.node-version }}

# Wrong
- run: node --version
  env:
    NODE_VERSION: ${{ matrix.nodeversion }}  # Missing hyphen
```

### Use Matrix Include/Exclude

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest]
    node: [16, 18]
    include:
      - os: ubuntu-latest
        node: 20
        experimental: true
    exclude:
      - os: windows-latest
        node: 16
```

### Set Maximum Concurrency

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest]
  max-parallel: 2
```

### Use Matrix Output in Subsequent Jobs

```yaml
jobs:
  build:
    strategy:
      matrix:
        target: [app1, app2]
    outputs:
      version: ${{ steps.build.outputs.version }}
```

## Examples

```yaml
# Error: matrix contains null value
strategy:
  matrix:
    node: [16, null, 20]  # Invalid

# Fix: remove null
strategy:
  matrix:
    node: [16, 18, 20]
```

## Related Errors

- [YAML Error]({{< relref "/tools/github-actions/github-actions-yaml-error" >}}) — YAML syntax error
- [Environment Error]({{< relref "/tools/github-actions/github-actions-env-error" >}}) — environment variable error
