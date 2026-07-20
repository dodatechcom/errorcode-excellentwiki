---
title: "[Solution] GitHub Actions Max Parallel Exceeded"
description: "Fix GitHub Actions max-parallel exceeded errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Max-parallel errors occur when too many matrix jobs run concurrently:

```
Error: Maximum concurrent jobs (200) exceeded for this repository
```

## Common Causes

- Large matrix creating many jobs.
- Multiple workflows running simultaneously.

## How to Fix

**Limit parallel jobs:**

```yaml
strategy:
  max-parallel: 5
  matrix:
    os: [ubuntu-latest, windows-latest, macos-latest]
    node-version: [16, 18, 20]
```

## Examples

```yaml
strategy:
  max-parallel: 3
  matrix:
    shard: [1, 2, 3, 4, 5, 6]
```
