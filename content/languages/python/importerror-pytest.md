---
title: "[Solution] Python ImportError: pytest not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: pytest not found or ModuleNotFoundError: No module named 'pytest'. Install pytest properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: pytest not found — ModuleNotFoundError Fix

An `ImportError: pytest not found` or `ModuleNotFoundError: No module named 'pytest'` means Python cannot locate the pytest package.

## What This Error Means

pytest is a testing framework. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: pytest not installed
import pytest  # ModuleNotFoundError: No module named 'pytest'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install pytest

# With coverage
pip install pytest-cov

# With async support
pip install pytest-asyncio
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install pytest
python -m pytest --version
```

## Related Errors

- {{< relref "junit5" >}} — JUnit platform launcher error (Java)
- {{< relref "mockito" >}} — Mockito misuse errors (Java)
- {{< relref "testcontainers" >}} — Testcontainers startup failure (Java)
