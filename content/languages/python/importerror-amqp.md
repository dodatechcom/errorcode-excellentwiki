---
title: "[Solution] Python ImportError: amqp not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: amqp not found or ModuleNotFoundError: No module named 'amqp'. Install amqp properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "amqp", "module-not-found", "pip", "messaging"]
weight: 5
---

# ImportError: amqp not found — ModuleNotFoundError Fix

An `ImportError: amqp not found` or `ModuleNotFoundError: No module named 'amqp'` means Python cannot locate the amqp package.

## What This Error Means

amqp is a Python AMQP client library. It is a dependency of kombu and Celery. It is not part of the standard library.

## Common Causes

```python
# Cause 1: amqp not installed
import amqp  # ModuleNotFoundError: No module named 'amqp'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install amqp
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install amqp
python -c "import amqp; print(amqp.__version__)"
```

## Related Errors

- {{< relref "importerror-celery" >}} — ImportError: celery
- {{< relref "importerror-celery2" >}} — ImportError: kombu
- {{< relref "spring-amqp" >}} — AmqpException (Java)
