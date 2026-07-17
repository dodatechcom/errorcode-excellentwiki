---
title: "[Solution] Python ImportError: pydantic not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: pydantic not found or ModuleNotFoundError: No module named 'pydantic'. Install pydantic properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: pydantic not found — ModuleNotFoundError Fix

An `ImportError: pydantic not found` or `ModuleNotFoundError: No module named 'pydantic'` means Python cannot locate the pydantic package.

## What This Error Means

pydantic is a data validation library using Python type annotations. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: pydantic not installed
from pydantic import BaseModel  # ModuleNotFoundError: No module named 'pydantic'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install pydantic

# For a specific version
pip install pydantic==2.5.3
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install pydantic
python -c "import pydantic; print(pydantic.__version__)"
```

## Related Errors

- {{< relref "importerror-fastapi" >}} — ImportError: fastapi
- {{< relref "importerror-sqlmodel" >}} — ImportError: sqlmodel
- {{< relref "importerror-uvicorn" >}} — ImportError: uvicorn
