---
title: "[Solution] GitHub Actions Pip Install Failed"
description: "Fix GitHub Actions pip install failures in Python workflow."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

pip install failures occur during Python dependency installation:

```
Error: ERROR: Could not find a version that satisfies the requirement
django>=4.2 (from -r requirements.txt)
```

## Common Causes

- Package version not available for the Python version.
- Missing system dependencies (e.g., C extensions).

## How to Fix

**Use proper Python setup:**

```yaml
steps:
  - uses: actions/setup-python@v5
    with:
      python-version: '3.11'
      cache: 'pip'
  - run: pip install -r requirements.txt
```

## Examples

```yaml
steps:
  - uses: actions/setup-python@v5
    with:
      python-version: '3.11'
      cache: 'pip'
  - run: |
      python -m pip install --upgrade pip
      pip install -r requirements.txt
```
