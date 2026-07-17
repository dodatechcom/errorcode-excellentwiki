---
title: "[Solution] Python ImportError: requests not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: requests not found or ModuleNotFoundError: No module named 'requests'. Install Requests properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "requests", "module-not-found", "pip", "http"]
weight: 5
---

# ImportError: requests not found — ModuleNotFoundError Fix

An `ImportError: requests not found` or `ModuleNotFoundError: No module named 'requests'` means Python cannot locate the Requests package.

## What This Error Means

Requests is a popular HTTP library. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: requests not installed
import requests  # ModuleNotFoundError: No module named 'requests'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install requests

# For a specific version
pip install requests==2.31.0
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install requests
python -c "import requests; print(requests.__version__)"
```

## Related Errors

- {{< relref "importerror-httpx" >}} — ImportError: httpx
- {{< relref "importerror-aiohttp" >}} — ImportError: aiohttp
- {{< relref "importerror-pika" >}} — ImportError: pika
