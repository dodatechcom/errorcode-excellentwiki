---
title: "[Solution] Python ImportError: plotly not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: plotly not found or ModuleNotFoundError: No module named 'plotly'. Install plotly properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "plotly", "module-not-found", "pip", "visualization"]
weight: 5
---

# ImportError: plotly not found — ModuleNotFoundError Fix

An `ImportError: plotly not found` or `ModuleNotFoundError: No module named 'plotly'` means Python cannot locate the plotly package.

## What This Error Means

plotly is an interactive graphing library. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: plotly not installed
import plotly  # ModuleNotFoundError: No module named 'plotly'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install plotly

# With optional dependencies
pip install plotly[express]
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install plotly
python -c "import plotly; print(plotly.__version__)"
```

## Related Errors

- {{< relref "importerror-matplotlib" >}} — ImportError: matplotlib
- {{< relref "importerror-seaborn" >}} — ImportError: seaborn
- {{< relref "importerror-pandas" >}} — ImportError: pandas
