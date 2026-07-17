---
title: "[Solution] Python ImportError: matplotlib not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: matplotlib not found or ModuleNotFoundError: No module named 'matplotlib'. Install matplotlib properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: matplotlib not found — ModuleNotFoundError Fix

An `ImportError: matplotlib not found` or `ModuleNotFoundError: No module named 'matplotlib'` means Python cannot locate the matplotlib package.

## What This Error Means

matplotlib is a plotting library. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: matplotlib not installed
import matplotlib  # ModuleNotFoundError: No module named 'matplotlib'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install matplotlib

# For a specific version
pip install matplotlib==3.8.2
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install matplotlib
python -c "import matplotlib; print(matplotlib.__version__)"
```

## Related Errors

- {{< relref "importerror-plotly" >}} — ImportError: plotly
- {{< relref "importerror-seaborn" >}} — ImportError: seaborn
- {{< relref "importerror-numpy" >}} — ImportError: numpy
