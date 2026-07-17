---
title: "[Solution] Python ImportError: uvicorn not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: uvicorn not found or ModuleNotFoundError: No module named 'uvicorn'. Install uvicorn properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "uvicorn", "module-not-found", "pip", "asgi"]
weight: 5
---

# ImportError: uvicorn not found — ModuleNotFoundError Fix

An `ImportError: uvicorn not found` or `ModuleNotFoundError: No module named 'uvicorn'` means Python cannot locate the uvicorn package.

## What This Error Means

uvicorn is an ASGI web server. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: uvicorn not installed
# Command: uvicorn main:app
# ModuleNotFoundError: No module named 'uvicorn'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install uvicorn

# With standard extras
pip install uvicorn[standard]
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install uvicorn
uvicorn --version
```

## Related Errors

- {{< relref "importerror-fastapi" >}} — ImportError: fastapi
- {{< relref "importerror-starlette" >}} — ImportError: starlette
- {{< relref "importerror-pydantic" >}} — ImportError: pydantic
