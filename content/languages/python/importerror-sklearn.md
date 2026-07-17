---
title: "[Solution] Python ImportError: sklearn not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: sklearn not found or ModuleNotFoundError: No module named 'sklearn'. Install scikit-learn properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: sklearn not found — ModuleNotFoundError Fix

An `ImportError: sklearn not found` or `ModuleNotFoundError: No module named 'sklearn'` means Python cannot locate the scikit-learn package. The package is installed as `scikit-learn` but imported as `sklearn`.

## What This Error Means

scikit-learn is a machine learning library. The package is installed as `scikit-learn` but imported as `sklearn`.

## Common Causes

```python
# Cause 1: scikit-learn not installed
from sklearn import svm  # ModuleNotFoundError: No module named 'sklearn'

# Cause 2: Installed wrong package name
pip install sklearn  # Wrong! Should be scikit-learn
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install scikit-learn

# NOT: pip install sklearn
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install scikit-learn
python -c "import sklearn; print(sklearn.__version__)"
```

## Related Errors

- {{< relref "importerror-numpy" >}} — ImportError: numpy
- {{< relref "importerror-pandas" >}} — ImportError: pandas
- {{< relref "importerror-torch" >}} — ImportError: torch
