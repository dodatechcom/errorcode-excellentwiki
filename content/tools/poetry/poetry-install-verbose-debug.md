---
title: "[Solution] Poetry Install Verbose Debug -- Fix Using Verbose Mode for Debugging"
description: "Fix Poetry install verbose debug issues when using -vvv to debug install failures. Interpret verbose output to identify root causes."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This is not a specific failure but guides you on using Poetry's verbose output to debug install issues. Verbose mode reveals hidden problems.

## Common Causes

- Install fails without clear error message
- Need to see which package triggers the failure
- Network or authentication issues are not visible
- Resolver is stuck or taking too long

## How to Fix

### 1. Enable Maximum Verbosity

```bash
poetry install -vvv
```

### 2. Trace HTTP Requests

```bash
POETRY_HTTP_TIMEOUT=300 poetry install -vvv 2>&1 | tee poetry-debug.log
```

### 3. Show Resolver Debug Info

```bash
poetry lock -vvv 2>&1 | grep -i "conflict\|error\|failed"
```

### 4. Check Installed State

```bash
poetry show --outdated
poetry check
```

## Examples

```bash
$ poetry install -vvv
Using virtualenv: /home/user/.cache/pypoetry/virtualenvs/myproject-py3.11
Installing dependencies from lock file
  Installing requests (2.31.0)
  1: Downloading requests-2.31.0-py3-none-any.whl (62 kB)
  Installing urllib3 (2.0.7)
  ...
```
