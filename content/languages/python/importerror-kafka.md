---
title: "[Solution] Python ImportError: kafka-python not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: kafka-python not found or ModuleNotFoundError: No module named 'kafka'. Install kafka-python properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "kafka", "kafka-python", "module-not-found", "pip", "messaging"]
weight: 5
---

# ImportError: kafka-python not found — ModuleNotFoundError Fix

An `ImportError: kafka-python not found` or `ModuleNotFoundError: No module named 'kafka'` means Python cannot locate the kafka-python package.

## What This Error Means

kafka-python is a Python client library for Apache Kafka. The package is installed as `kafka-python` but imported as `kafka`.

## Common Causes

```python
# Cause 1: kafka-python not installed
from kafka import KafkaConsumer  # ModuleNotFoundError: No module named 'kafka'

# Cause 2: Installed wrong package name
pip install kafka  # Wrong! Should be kafka-python
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install kafka-python

# NOT: pip install kafka

# Alternative: confluent-kafka (faster, C-based)
pip install confluent-kafka
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install kafka-python
python -c "import kafka; print(kafka.__version__)"
```

## Related Errors

- {{< relref "kafka-consumer" >}} — Kafka consumer errors
- {{< relref "testcontainers-kafka" >}} — KafkaContainer startup failed
- {{< relref "importerror-redis-py" >}} — ImportError: redis
