---
title: "[Solution] GitHub Actions Artifact Name Conflict"
description: "Fix GitHub Actions artifact name conflict errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Artifact name conflicts occur when uploading an artifact with a name that already exists:

```
Error: Artifact with name 'my-artifact' already exists
```

## Common Causes

- Multiple jobs uploading artifacts with the same name.
- Using a static name without including unique identifiers.

## How to Fix

**Use unique artifact names:**

```yaml
- uses: actions/upload-artifact@v4
  with:
    name: build-${{ runner.os }}-${{ github.run_id }}
    path: ./dist
```

## Examples

```yaml
# Dynamic name with matrix
name: test-results-${{ matrix.os }}-${{ matrix.node-version }}
```
