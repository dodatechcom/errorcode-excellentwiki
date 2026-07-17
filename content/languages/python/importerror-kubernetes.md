---
title: "[Solution] Python ImportError: kubernetes not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: kubernetes not found or ModuleNotFoundError: No module named 'kubernetes'. Install kubernetes properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "kubernetes", "module-not-found", "pip", "orchestration"]
weight: 5
---

# ImportError: kubernetes not found — ModuleNotFoundError Fix

An `ImportError: kubernetes not found` or `ModuleNotFoundError: No module named 'kubernetes'` means Python cannot locate the kubernetes package.

## What This Error Means

kubernetes is the official Python client for Kubernetes. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: kubernetes not installed
from kubernetes import client  # ModuleNotFoundError: No module named 'kubernetes'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install kubernetes

# For a specific version
pip install kubernetes==28.1.0
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install kubernetes
python -c "import kubernetes; print(kubernetes.__version__)"
```

## Related Errors

- {{< relref "importerror-docker" >}} — ImportError: docker
- {{< relref "importerror-boto3" >}} — ImportError: boto3
