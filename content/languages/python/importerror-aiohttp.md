---
title: "[Solution] Python ImportError: aiohttp not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: aiohttp not found or ModuleNotFoundError: No module named 'aiohttp'. Install aiohttp properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "aiohttp", "module-not-found", "pip", "async"]
weight: 5
---

# ImportError: aiohttp not found — ModuleNotFoundError Fix

An `ImportError: aiohttp not found` or `ModuleNotFoundError: No module named 'aiohttp'` means Python cannot locate the aiohttp package.

## What This Error Means

aiohttp is an asynchronous HTTP client/server framework for asyncio.

## Common Causes

```python
# Cause 1: aiohttp not installed
import aiohttp  # ModuleNotFoundError: No module named 'aiohttp'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install aiohttp

# For a specific version
pip install aiohttp==3.9.1
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install aiohttp
python -c "import aiohttp; print(aiohttp.__version__)"
```

## Related Errors

- {{< relref "importerror-httpx" >}} — ImportError: httpx
- {{< relref "importerror-requests" >}} — ImportError: requests
- {{< relref "importerror-fastapi" >}} — ImportError: fastapi
