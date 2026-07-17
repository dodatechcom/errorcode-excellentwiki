---
title: "[Solution] Python ImportError: llama_cpp not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: llama_cpp not found or ModuleNotFoundError: No module named 'llama_cpp'. Install llama-cpp-python properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: llama_cpp not found — ModuleNotFoundError Fix

An `ImportError: llama_cpp not found` or `ModuleNotFoundError: No module named 'llama_cpp'` means Python cannot locate the llama-cpp-python package.

## What This Error Means

llama-cpp-python is a Python binding for llama.cpp. The package is installed as `llama-cpp-python` but imported as `llama_cpp`.

## Common Causes

```python
# Cause 1: llama-cpp-python not installed
from llama_cpp import Llama  # ModuleNotFoundError

# Cause 2: CMake not installed (compilation fails)
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install llama-cpp-python
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install llama-cpp-python
python -c "from llama_cpp import Llama; print('OK')"
```

## Related Errors

- {{< relref "importerror-ctransformers" >}} — ImportError: ctransformers
- {{< relref "importerror-gguf" >}} — ImportError: gguf
- {{< relref "importerror-exllama" >}} — ImportError: exllamav2
