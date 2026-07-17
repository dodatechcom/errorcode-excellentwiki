---
title: "[Solution] Python ImportError: flask not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: flask not found or ModuleNotFoundError: No module named 'flask'. Install Flask properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "flask", "module-not-found", "pip", "web-framework"]
weight: 5
---

# ImportError: flask not found — ModuleNotFoundError Fix

An `ImportError: flask not found` or `ModuleNotFoundError: No module named 'flask'` means Python cannot locate the Flask package.

## What This Error Means

Flask is a lightweight web framework. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: Flask not installed
from flask import Flask  # ModuleNotFoundError: No module named 'flask'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install flask

# With async support
pip install flask[async]
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install flask
python -c "from flask import Flask; print('OK')"
```

## Related Errors

- {{< relref "importerror-uvicorn" >}} — ImportError: uvicorn
- {{< relref "importerror-fastapi" >}} — ImportError: fastapi
- {{< relref "importerror-pydantic" >}} — ImportError: pydantic
