---
title: "[Solution] Python ImportError: fastapi not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: fastapi not found or ModuleNotFoundError: No module named 'fastapi'. Install FastAPI properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: fastapi not found — ModuleNotFoundError Fix

An `ImportError: fastapi not found` or `ModuleNotFoundError: No module named 'fastapi'` means Python cannot locate the FastAPI package.

## What This Error Means

FastAPI is a modern, fast web framework for building APIs. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: FastAPI not installed
from fastapi import FastAPI  # ModuleNotFoundError: No module named 'fastapi'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install fastapi

# With all optional dependencies
pip install fastapi[all]
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install fastapi
python -c "from fastapi import FastAPI; print('OK')"
```

## Related Errors

- {{< relref "importerror-uvicorn" >}} — ImportError: uvicorn
- {{< relref "importerror-pydantic" >}} — ImportError: pydantic
- {{< relref "importerror-starlette" >}} — ImportError: starlette
