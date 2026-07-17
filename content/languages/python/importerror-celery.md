---
title: "[Solution] Python ImportError: celery not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: celery not found or ModuleNotFoundError: No module named 'celery'. Install Celery properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "celery", "module-not-found", "pip", "task-queue"]
weight: 5
---

# ImportError: celery not found — ModuleNotFoundError Fix

An `ImportError: celery not found` or `ModuleNotFoundError: No module named 'celery'` means Python cannot locate the Celery package.

## What This Error Means

Celery is a distributed task queue. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: Celery not installed
from celery import Celery  # ModuleNotFoundError: No module named 'celery'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install celery

# With Redis broker support
pip install celery[redis]

# With RabbitMQ broker support
pip install celery[rabbitmq]
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install celery
python -c "import celery; print(celery.__version__)"
```

## Related Errors

- {{< relref "importerror-kombu" >}} — ImportError: kombu
- {{< relref "importerror-amqp" >}} — ImportError: amqp
- {{< relref "importerror-redis-py" >}} — ImportError: redis
