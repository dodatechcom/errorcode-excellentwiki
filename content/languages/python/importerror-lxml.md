---
title: "[Solution] Python ImportError: lxml not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: lxml not found or ModuleNotFoundError: No module named 'lxml'. Install lxml properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: lxml not found — ModuleNotFoundError Fix

An `ImportError: lxml not found` or `ModuleNotFoundError: No module named 'lxml'` means Python cannot locate the lxml package.

## What This Error Means

lxml is a Python binding for C libraries libxml2 and libxslt. It requires system-level dependencies to compile.

## Common Causes

```python
# Cause 1: lxml not installed
from lxml import etree  # ModuleNotFoundError: No module named 'lxml'

# Cause 2: Missing system dependencies
# pip install lxml fails with compilation errors
```

## How to Fix

### Fix 1: Install with pip

```bash
# Install system dependencies first (Ubuntu/Debian)
sudo apt-get install libxml2-dev libxslt-dev python3-dev

# Then install lxml
pip install lxml
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install lxml
python -c "from lxml import etree; print('OK')"
```

## Related Errors

- {{< relref "importerror-beautifulsoup" >}} — ImportError: bs4
- {{< relref "importerror-cffi" >}} — ImportError: cffi
- {{< relref "importerror-pycparser" >}} — ImportError: pycparser
