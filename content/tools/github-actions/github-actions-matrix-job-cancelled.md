---
title: "[Solution] GitHub Actions Matrix Job Cancelled"
description: "Fix GitHub Actions matrix job cancelled unexpectedly."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Matrix job cancellation occurs when a matrix job is unexpectedly cancelled:

```
Error: The operation was cancelled
```

## Common Causes

- Workflow was manually cancelled.
- Concurrency group cancelled the job.
- `fail-fast: true` cancelled other jobs.

## How to Fix

**Use concurrency groups carefully:**

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: ${{ github.ref != 'refs/heads/main' }}
```

## Examples

```yaml
concurrency:
  group: build-${{ github.ref }}
  cancel-in-progress: ${{ github.ref != 'refs/heads/main' }}
```
