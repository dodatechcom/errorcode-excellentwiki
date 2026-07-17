---
title: "[Solution] Python ImportError: boto3 not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: boto3 not found or ModuleNotFoundError: No module named 'boto3'. Install boto3 properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "boto3", "module-not-found", "pip", "aws"]
weight: 5
---

# ImportError: boto3 not found — ModuleNotFoundError Fix

An `ImportError: boto3 not found` or `ModuleNotFoundError: No module named 'boto3'` means Python cannot locate the boto3 package.

## What This Error Means

boto3 is the AWS SDK for Python. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: boto3 not installed
import boto3  # ModuleNotFoundError: No module named 'boto3'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install boto3

# For a specific version
pip install boto3==1.29.7
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install boto3
python -c "import boto3; print(boto3.__version__)"
```

## Related Errors

- {{< relref "importerror-bedrock" >}} — ImportError: boto3 bedrock
- {{< relref "testcontainers-localstack" >}} — LocalStackContainer startup failed
- {{< relref "importerror-docker" >}} — ImportError: docker
