---
title: "[Solution] Python ImportError: semantic_kernel not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: semantic_kernel not found or ModuleNotFoundError: No module named 'semantic_kernel'. Install semantic-kernel properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: semantic_kernel not found — ModuleNotFoundError Fix

An `ImportError: semantic_kernel not found` or `ModuleNotFoundError: No module named 'semantic_kernel'` means Python cannot locate the semantic-kernel package.

## What This Error Means

semantic-kernel is a SDK for building AI plugins. The package is installed as `semantic-kernel` but imported as `semantic_kernel`.

## Common Causes

```python
# Cause 1: semantic-kernel not installed
import semantic_kernel as sk  # ModuleNotFoundError

# Cause 2: Installed wrong package name
pip install semantic_kernel  # Wrong! Should be semantic-kernel
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install semantic-kernel

# NOT: pip install semantic_kernel
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install semantic-kernel
python -c "import semantic_kernel; print('OK')"
```

## Related Errors

- {{< relref "importerror-langchain" >}} — ImportError: langchain
- {{< relref "importerror-openai" >}} — ImportError: openai
- {{< relref "importerror-transformers" >}} — ImportError: transformers
