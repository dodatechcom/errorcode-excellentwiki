---
title: "[Solution] Python ImportError: docker not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: docker not found or ModuleNotFoundError: No module named 'docker'. Install docker-py properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "docker", "module-not-found", "pip", "containers"]
weight: 5
---

# ImportError: docker not found — ModuleNotFoundError Fix

An `ImportError: docker not found` or `ModuleNotFoundError: No module named 'docker'` means Python cannot locate the docker package.

## What This Error Means

docker-py is the Python SDK for Docker. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: docker not installed
import docker  # ModuleNotFoundError: No module named 'docker'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install docker

# For a specific version
pip install docker==6.1.3
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install docker
python -c "import docker; print(docker.__version__)"
```

## Related Errors

- {{< relref "importerror-kubernetes" >}} — ImportError: kubernetes
- {{< relref "testcontainers" >}} — Testcontainers startup failure (Java)
- {{< relref "importerror-boto3" >}} — ImportError: boto3
