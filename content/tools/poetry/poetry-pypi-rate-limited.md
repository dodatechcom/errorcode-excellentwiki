---
title: "[Solution] Poetry PyPI Rate Limited -- Fix Too Many Requests from PyPI"
description: "Fix Poetry PyPI rate limited errors when PyPI returns 429 Too Many Requests. Add delays and use local caching."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means PyPI is rate-limiting your requests because you are making too many in a short time. Poetry cannot download packages.

## Common Causes

- Running many parallel installs on CI
- Multiple Poetry processes running simultaneously
- Using a shared IP with many developers
- Aggressive retry loops

## How to Fix

### 1. Disable Parallel Installation

```bash
poetry config installer.parallel false
```

### 2. Add Retry Delay

```bash
poetry config installer.max-workers 1
```

### 3. Use a Cache Server

```bash
# Use a local PyPI mirror
poetry config repositories.local http://localhost:8080/simple/
```

### 4. Wait and Retry

```bash
sleep 60
poetry install
```

## Examples

```bash
$ poetry install
HTTPError: 429 Too Many Requests from https://pypi.org/simple/

$ poetry config installer.parallel false
$ poetry config installer.max-workers 1
$ poetry install
Installing dependencies from lock file...
```
