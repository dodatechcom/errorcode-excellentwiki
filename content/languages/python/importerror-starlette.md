---
title: "[Solution] Python ImportError: starlette not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: starlette not found or ModuleNotFoundError: No module named 'starlette'. Install starlette properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: starlette not found — ModuleNotFoundError Fix

An `ImportError: starlette not found` or `ModuleNotFoundError: No module named 'starlette'` means Python cannot locate the starlette package.

## What This Error Means

starlette is a lightweight ASGI framework/toolkit. It is not part of the standard library and must be installed separately. FastAPI depends on starlette.

## Common Causes

```python
# Cause 1: starlette not installed
from starlette.requests import Request  # ModuleNotFoundError

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install starlette
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install starlette
python -c "from starlette import __version__; print(__version__)"
```

## Related Errors

- {{< relref "importerror-fastapi" >}} — ImportError: fastapi
- {{< relref "importerror-uvicorn" >}} — ImportError: uvicorn
- {{< relref "importerror-pydantic" >}} — ImportError: pydantic
