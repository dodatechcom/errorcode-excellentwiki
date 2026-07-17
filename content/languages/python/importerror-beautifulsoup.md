---
title: "[Solution] Python ImportError: bs4 not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: bs4 not found or ModuleNotFoundError: No module named 'bs4'. Install BeautifulSoup4 properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "beautifulsoup", "bs4", "module-not-found", "pip", "web-scraping"]
weight: 5
---

# ImportError: bs4 not found — ModuleNotFoundError Fix

An `ImportError: bs4 not found` or `ModuleNotFoundError: No module named 'bs4'` means Python cannot locate the BeautifulSoup4 package.

## What This Error Means

BeautifulSoup4 is a web scraping library. The package is installed as `beautifulsoup4` but imported as `bs4`.

## Common Causes

```python
# Cause 1: bs4 not installed
from bs4 import BeautifulSoup  # ModuleNotFoundError: No module named 'bs4'

# Cause 2: Installed wrong package name
pip install beautifulsoup  # Wrong! Should be beautifulsoup4
```

## How to Fix

### Fix 1: Install with pip (correct package name)

```bash
pip install beautifulsoup4

# NOT: pip install beautifulsoup
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install beautifulsoup4
python -c "from bs4 import BeautifulSoup; print('OK')"
```

## Related Errors

- {{< relref "importerror-lxml" >}} — ImportError: lxml
- {{< relref "importerror-requests" >}} — ImportError: requests
- {{< relref "importerror-scrapy" >}} — ImportError: scrapy
