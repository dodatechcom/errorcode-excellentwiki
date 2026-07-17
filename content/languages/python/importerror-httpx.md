---
title: "[Solution] Python ImportError: httpx not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: httpx not found or ModuleNotFoundError: No module named 'httpx'. Install httpx properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: httpx not found — ModuleNotFoundError Fix

An `ImportError: httpx not found` or `ModuleNotFoundError: No module named 'httpx'` means Python cannot locate the httpx package.

## What This Error Means

httpx is a fully featured HTTP client for Python 3. It supports async and sync APIs.

## Common Causes

```python
# Cause 1: httpx not installed
import httpx  # ModuleNotFoundError: No module named 'httpx'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install httpx

# With HTTP/2 support
pip install httpx[http2]
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install httpx
python -c "import httpx; print(httpx.__version__)"
```

## Related Errors

- {{< relref "importerror-requests" >}} — ImportError: requests
- {{< relref "importerror-aiohttp" >}} — ImportError: aiohttp
- {{< relref "importerror-fastapi" >}} — ImportError: fastapi
