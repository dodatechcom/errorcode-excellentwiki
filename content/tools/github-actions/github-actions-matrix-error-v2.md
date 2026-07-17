---
title: "GitHub Actions Matrix Strategy Configuration Error"
description: "GitHub Actions matrix strategy configuration is invalid."
tools: ["github-actions"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# GitHub Actions — Matrix Strategy Configuration Error

This error occurs when the GitHub Actions matrix strategy is configured incorrectly. Invalid matrix values, missing properties, or conflicting options cause the workflow to fail.

## Common Causes

- Invalid matrix values or types
- Missing matrix dimensions
- `fail-fast` combined with required matrix entries
- Matrix produces too many combinations
- Expression syntax errors in matrix values

## How to Fix

### Define Valid Matrix

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [16, 18, 20]
        os: [ubuntu-latest, windows-latest]
```

### Configure Fail-Fast

```yaml
strategy:
  fail-fast: false
  matrix:
    node-version: [16, 18, 20]
```

### Include Additional Combinations

```yaml
strategy:
  matrix:
    node-version: [16, 18, 20]
    include:
      - node-version: 20
        experimental: true
```

### Exclude Specific Combinations

```yaml
strategy:
  matrix:
    node-version: [16, 18, 20]
    os: [ubuntu-latest, windows-latest]
    exclude:
      - node-version: 16
        os: windows-latest
```

### Use Matrix in Steps

```yaml
steps:
  - uses: actions/setup-node@v4
    with:
      node-version: ${{ matrix.node-version }}
```

## Examples

```text
Error: The matrix configuration is invalid.
  "node-version" must be a string, number, or array of strings/numbers.
```

## Related Errors

- [GitHub Actions YAML Error]({{< relref "/tools/github-actions/github-actions-yaml-error" >}}) — YAML syntax error
- [GitHub Actions Runner Error]({{< relref "/tools/github-actions/github-actions-runner-error" >}}) — runner issues
- [GitHub Actions Timeout Error]({{< relref "/tools/github-actions/github-actions-timeout-error" >}}) — job timeout
