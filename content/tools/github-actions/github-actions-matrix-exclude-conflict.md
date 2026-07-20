---
title: "[Solution] GitHub Actions Matrix Exclude Conflict"
description: "Fix GitHub Actions matrix exclude conflict errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Matrix exclude conflicts occur when exclusion rules are contradictory:

```
Error: Matrix exclude conflict: cannot exclude all combinations
```

## Common Causes

- Exclude rules remove all valid combinations.
- Overly broad exclude patterns.

## How to Fix

**Review exclude rules:**

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest, macos-latest]
    node-version: [16, 18, 20]
    exclude:
      - os: macos-latest
        node-version: 16
```

## Examples

```yaml
exclude:
  - os: macos-latest
    node-version: 16
  - os: windows-latest
    node-version: 18
```
