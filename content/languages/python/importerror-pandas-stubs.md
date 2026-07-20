---
title: "[Solution] Python ImportError: No module named 'pandas-stubs' — Fix"
description: "Fix Python ImportError: No module named 'pandas-stubs'. Install pandas-stubs with pip and resolve dependency conflicts."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 308
---

# Python ImportError: No module named 'pandas-stubs'

The `ModuleNotFoundError: No module named 'pandas_stubs'` error occurs when type checkers like mypy or pyright cannot locate the pandas-stubs package, which provides type annotations for the pandas library.

## Common Causes

```python
# Cause 1: pandas-stubs not installed for type checking
# mypy reports: error: Library stubs not installed for "pandas"
# ModuleNotFoundError: No module named 'pandas_stubs'

# Cause 2: Installed for wrong Python version
import pandas_stubs  # ModuleNotFoundError

# Cause 3: pandas installed but pandas-stubs missing
# pip install pandas does not install type stubs
```

```python
# Cause 4: pyright/mypy cannot find stubs in virtual env
# stubs installed globally but not in project venv

# Cause 5: Outdated pandas-stubs incompatible with installed pandas
# version mismatch causes import failures
```

## How to Fix

### Fix 1: Install pandas-stubs with pip

```bash
pip install pandas-stubs

# Verify installation
python -c "import pandas_stubs; print('OK')"
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install pandas-stubs
mypy --install-types --non-interactive
```

### Fix 3: Add to project dev dependencies

```bash
# pyproject.toml
[project.optional-dependencies]
typing = ["pandas-stubs"]

# Install
pip install -e ".[typing]"
```

## Examples

```bash
# Type-check with pandas stubs
mypy src/

# pyright automatically uses installed stubs
pyright src/

# Install compatible version with pandas
pip install pandas-stubs pandas==2.1.0
```

```python
# Using pandas-stubs for type hints
import pandas as pd
from pandas import DataFrame

def process_data(df: DataFrame) -> DataFrame:
    return df.groupby("col").sum()
```

## Related Errors

- {{< relref "importerror-pandas" >}} — ImportError: pandas
- {{< relref "importerror-mypy" >}} — ImportError: mypy
- {{< relref "importerror-pyarrow" >}} — ImportError: pyarrow
