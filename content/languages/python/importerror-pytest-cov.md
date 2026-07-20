---
title: "[Solution] Python ImportError: No module named 'pytest_cov' — Fix"
description: "Fix Python ImportError: No module named 'pytest_cov'. Install pytest-cov with pip and resolve dependency conflicts."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 301
---

# Python ImportError: No module named 'pytest_cov'

The `ModuleNotFoundError: No module named 'pytest_cov'` error occurs when Python cannot locate the pytest-cov package, which provides coverage reporting for pytest test runs.

## Common Causes

```python
# Cause 1: pytest-cov not installed
# Running: pytest --cov=mymodule
# E     ModuleNotFoundError: No module named 'pytest_cov'

# Cause 2: Installed for wrong Python version or virtual environment
import pytest_cov  # ModuleNotFoundError

# Cause 3: Package name vs import name mismatch
# pip install pytest-cov → import pytest_cov
```

```python
# Cause 4: Using --cov flag without pytest-cov installed
# pytest --cov=src tests/
# ModuleNotFoundError: No module named 'pytest_cov'

# Cause 5: Plugin not registered in pytest
# pytest cannot find the cov plugin
```

## How to Fix

### Fix 1: Install pytest-cov with pip

```bash
pip install pytest-cov

# Verify installation
python -c "import pytest_cov; print(pytest_cov.__version__)"
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install pytest-cov
pytest --co -q | grep cov
```

### Fix 3: Add to project requirements

```bash
# requirements-dev.txt
pytest-cov

# Install from requirements
pip install -r requirements-dev.txt
```

## Examples

```bash
# Basic coverage run
pytest --cov=mymodule tests/

# Coverage with report
pytest --cov=mymodule --cov-report=html tests/

# Coverage with fail threshold
pytest --cov=mymodule --cov-fail-under=80 tests/
```

```python
# conftest.py — automatic coverage setup
import pytest_cov

def pytest_configure(config):
    config.addinivalue_line(
        "markers", "cov: mark test with coverage options"
    )
```

## Related Errors

- {{< relref "importerror-pytest" >}} — ImportError: pytest
- {{< relref "importerror-coverage" >}} — ImportError: coverage
- {{< relref "importerror-tqdm" >}} — ImportError: tqdm
