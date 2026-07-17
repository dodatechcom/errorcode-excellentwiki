---
title: "[Solution] Python ImportError: paramiko not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: paramiko not found or ModuleNotFoundError: No module named 'paramiko'. Install paramiko properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "paramiko", "module-not-found", "pip", "ssh"]
weight: 5
---

# ImportError: paramiko not found — ModuleNotFoundError Fix

An `ImportError: paramiko not found` or `ModuleNotFoundError: No module named 'paramiko'` means Python cannot locate the paramiko package.

## What This Error Means

paramiko is the Python implementation of SSHv2 protocol. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: paramiko not installed
import paramiko  # ModuleNotFoundError: No module named 'paramiko'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install paramiko
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install paramiko
python -c "import paramiko; print(paramiko.__version__)"
```

## Related Errors

- {{< relref "importerror-cryptography" >}} — ImportError: cryptography
- {{< relref "importerror-cffi" >}} — ImportError: cffi
- {{< relref "importerror-docker" >}} — ImportError: docker
