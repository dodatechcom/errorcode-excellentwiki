---
title: "[Solution] Python ImportError: kombu not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: kombu not found or ModuleNotFoundError: No module named 'kombu'. Install kombu properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "kombu", "module-not-found", "pip", "messaging"]
weight: 5
---

# ImportError: kombu not found — ModuleNotFoundError Fix

An `ImportError: kombu not found` or `ModuleNotFoundError: No module named 'kombu'` means Python cannot locate the kombu package.

## What This Error Means

kombu is a messaging library for Python. It is a dependency of Celery. It is not part of the standard library.

## Common Causes

```python
# Cause 1: kombu not installed
import kombu  # ModuleNotFoundError: No module named 'kombu'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install kombu

# With Redis support
pip install kombu[redis]
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install kombu
python -c "import kombu; print(kombu.__version__)"
```

## Related Errors

- {{< relref "importerror-celery" >}} — ImportError: celery
- {{< relref "importerror-celery2" >}} — ImportError: kombu
- {{< relref "importerror-amqp" >}} — ImportError: amqp
