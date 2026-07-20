---
title: "[Solution] Python ImportError: No module named 'bs4' — Fix"
description: "Fix Python ImportError: No module named 'bs4'. Install beautifulsoup4 with pip and resolve dependency conflicts."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 325
---

# Python ImportError: No module named 'bs4'

Beautiful Soup 4 is an HTML and XML parsing library. The import name is `bs4`, not `beautifulsoup4`. This error occurs when the package is not installed.

## Common Causes

```python
# Cause 1: beautifulsoup4 not installed
from bs4 import BeautifulSoup  # ImportError: No module named 'bs4'

# Cause 2: Confusing install name with import name
# pip install beautifulsoup4 but then: import beautifulsoup4 — ImportError

# Cause 3: Wrong virtual environment
# beautifulsoup4 installed in a different venv

# Cause 4: Only lxml installed without bs4
import lxml  # Works, but from bs4 import BeautifulSoup fails

# Cause 5: pip installed for wrong Python version
python3.12 -c "from bs4 import BeautifulSoup"  # ImportError
```

## How to Fix

### Fix 1: Install beautifulsoup4 with pip

```bash
pip install beautifulsoup4

# For a specific version
pip install beautifulsoup4==4.12.3

# With a parser backend
pip install beautifulsoup4 lxml
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install beautifulsoup4
python -c "from bs4 import BeautifulSoup; print(BeautifulSoup.__module__)"
```

### Fix 3: Install with common companions

```bash
pip install beautifulsoup4 lxml requests
```

## Examples

```python
from bs4 import BeautifulSoup

html = "<html><body><p>Hello</p></body></html>"
soup = BeautifulSoup(html, "html.parser")
print(soup.p.text)
```

## Related Errors

- {{< relref "importerror-lxml" >}} — ImportError: lxml
- {{< relref "importerror-beautifulsoup" >}} — ImportError: beautifulsoup (variant)
- {{< relref "importerror-requests" >}} — ImportError: requests
