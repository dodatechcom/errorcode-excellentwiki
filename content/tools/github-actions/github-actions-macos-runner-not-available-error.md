---
title: "[Solution] GitHub Actions macOS Runner Not Available Error"
description: "Fix GitHub Actions macOS runner availability errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

macOS runner not available errors occur when macOS runners cannot be assigned:

```
Error: No runner matching the specified labels was found: macos-latest
```

## Common Causes

- macOS runner capacity is exhausted.
- Organization plan does not include macOS runners.

## How to Fix

**Use `continue-on-error` to handle unavailability:**

```yaml
strategy:
  fail-fast: false
  matrix:
    os: [ubuntu-latest, macos-latest]
runs-on: ${{ matrix.os }}
continue-on-error: ${{ matrix.os == 'macos-latest' }}
```

## Examples

```yaml
jobs:
  build:
    runs-on: macos-latest
    steps:
      - uses: actions/checkout@v4
```
