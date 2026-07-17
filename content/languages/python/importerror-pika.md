---
title: "[Solution] Python ImportError: pika not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: pika not found or ModuleNotFoundError: No module named 'pika'. Install pika properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: pika not found — ModuleNotFoundError Fix

An `ImportError: pika not found` or `ModuleNotFoundError: No module named 'pika'` means Python cannot locate the pika package.

## What This Error Means

pika is a Python AMQP 0-9-1 client library for RabbitMQ. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: pika not installed
import pika  # ModuleNotFoundError: No module named 'pika'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install pika

# For a specific version
pip install pika==1.3.2
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install pika
python -c "import pika; print(pika.__version__)"
```

## Related Errors

- {{< relref "spring-amqp" >}} — AmqpException (Java)
- {{< relref "importerror-amqp" >}} — ImportError: amqp
- {{< relref "testcontainers-rabbitmq" >}} — RabbitMQContainer startup failed (Java)
