---
title: "[Solution] Python ImportError: scrapy not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: scrapy not found or ModuleNotFoundError: No module named 'scrapy'. Install Scrapy properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: scrapy not found — ModuleNotFoundError Fix

An `ImportError: scrapy not found` or `ModuleNotFoundError: No module named 'scrapy'` means Python cannot locate the Scrapy package.

## What This Error Means

Scrapy is an open-source web crawling framework. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: Scrapy not installed
import scrapy  # ModuleNotFoundError: No module named 'scrapy'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install scrapy

# For a specific version
pip install scrapy==2.11.0
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install scrapy
python -c "import scrapy; print(scrapy.__version__)"
```

## Related Errors

- {{< relref "importerror-beautifulsoup" >}} — ImportError: bs4
- {{< relref "importerror-lxml" >}} — ImportError: lxml
- {{< relref "importerror-requests" >}} — ImportError: requests
