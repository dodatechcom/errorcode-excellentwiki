---
title: "[Solution] GitHub Actions Matrix Configuration Error"
description: "Fix GitHub Actions matrix configuration errors. Resolve invalid matrix syntax and matrix expansion issues."
tools: ["github-actions"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# GitHub Actions Matrix Configuration Error

A matrix configuration error occurs when the `strategy.matrix` definition is invalid, contains incompatible combinations, or references undefined variables.

## Common Causes

- The matrix values have incompatible type combinations
- A matrix variable is referenced in `runs-on` but not defined
- The matrix produces too many combinations (exceeding limits)
- Invalid YAML syntax in the matrix block

## How to Fix

### Define a Valid Matrix

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [16, 18, 20]
        os: [ubuntu-latest, windows-latest]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
```

### Use Matrix Include/Exclude

```yaml
strategy:
  matrix:
    node: [16, 18, 20]
    os: [ubuntu-latest, windows-latest]
    exclude:
      - node: 16
        os: windows-latest
    include:
      - node: 21
        os: ubuntu-latest
        experimental: true
```

### Fix runs-on Referencing Matrix

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, macos-latest, windows-latest]
runs-on: ${{ matrix.os }}  # must match matrix key
```

### Limit Maximum Jobs

```yaml
strategy:
  fail-fast: false
  matrix:
    node: [16, 18, 20]
  max-parallel: 2
```

## Examples

```yaml
# Invalid runs-on value
runs-on: ${{ matrix.os }}
# matrix defines os: [ubuntu, windows] but ubuntu is not a valid runner
# Fix: use ubuntu-latest, not ubuntu

# Undefined matrix variable
runs-on: ${{ matrix.platform }}
# ERROR: matrix defines 'os', not 'platform'
# Fix: match the variable name in runs-on
```

## Related Errors

- [Env Error]({{< relref "/tools/github-actions/env-error3" >}}) — environment variable not set
- [Cache Error]({{< relref "/tools/github-actions/cache-error4" >}}) — cache restore failure
