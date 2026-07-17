---
title: "[Solution] Python ImportError: cryptography not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: cryptography not found or ModuleNotFoundError: No module named 'cryptography'. Install cryptography properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "cryptography", "module-not-found", "pip", "security"]
weight: 5
---

# ImportError: cryptography not found — ModuleNotFoundError Fix

An `ImportError: cryptography not found` or `ModuleNotFoundError: No module named 'cryptography'` means Python cannot locate the cryptography package.

## What This Error Means

Cryptography is a library for encryption and cryptographic primitives. It requires Rust to compile from source.

## Common Causes

```python
# Cause 1: cryptography not installed
from cryptography.fernet import Fernet  # ModuleNotFoundError

# Cause 2: Rust not installed (compilation fails)
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install cryptography

# For a specific version
pip install cryptography==41.0.7
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install cryptography
python -c "import cryptography; print(cryptography.__version__)"
```

## Related Errors

- {{< relref "importerror-paramiko" >}} — ImportError: paramiko
- {{< relref "importerror-cffi" >}} — ImportError: cffi
- {{< relref "importerror-pycparser" >}} — ImportError: pycparser
