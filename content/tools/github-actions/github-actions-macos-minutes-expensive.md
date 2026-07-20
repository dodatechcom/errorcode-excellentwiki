---
title: "[Solution] GitHub Actions macOS Minutes Expensive"
description: "Fix GitHub Actions macOS runner minutes cost concerns."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

macOS minutes are billed at a higher rate, causing billing surprises:

```
Warning: macOS runner minutes are charged at 10x the Linux rate
```

## Common Causes

- macOS runners cost 10x Linux minutes.
- Large matrix with macOS targets.

## How to Fix

**Limit macOS builds:**

```yaml
strategy:
  matrix:
    os: [ubuntu-latest]
    include:
      - os: macos-latest
        node-version: 20
```

## Examples

```yaml
jobs:
  macos-test:
    runs-on: macos-latest
    if: github.ref == 'refs/heads/main'
```
