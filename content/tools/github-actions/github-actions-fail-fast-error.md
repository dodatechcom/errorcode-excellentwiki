---
title: "[Solution] GitHub Actions Fail-Fast Error"
description: "Fix GitHub Actions fail-fast strategy errors in matrix builds."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Fail-fast errors occur when `fail-fast` causes unexpected early termination:

```
Error: Build cancelled because one matrix job failed (fail-fast: true)
```

## Common Causes

- Default `fail-fast: true` cancels all jobs on first failure.
- Flaky test in one matrix combination kills all others.

## How to Fix

**Disable fail-fast:**

```yaml
strategy:
  fail-fast: false
  matrix:
    os: [ubuntu-latest, windows-latest, macos-latest]
    node-version: [16, 18, 20]
```

## Examples

```yaml
strategy:
  fail-fast: false
  matrix:
    node-version: [16, 18, 20]
```
