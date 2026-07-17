---
title: "[Solution] Python ImportError: exllamav2 not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: exllamav2 not found or ModuleNotFoundError: No module named 'exllamav2'. Install exllamav2 properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "exllama", "exllamav2", "module-not-found", "pip", "llm"]
weight: 5
---

# ImportError: exllamav2 not found — ModuleNotFoundError Fix

An `ImportError: exllamav2 not found` or `ModuleNotFoundError: No module named 'exllamav2'` means Python cannot locate the exllamav2 package.

## What This Error Means

exllamav2 is a fast inference library for quantized LLMs. It requires CUDA and specific GPU support.

## Common Causes

```python
# Cause 1: exllamav2 not installed
from exllamav2 import ExLlamaV2  # ModuleNotFoundError

# Cause 2: CUDA not available
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install exllamav2
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install exllamav2
python -c "from exllamav2 import ExLlamaV2; print('OK')"
```

## Related Errors

- {{< relref "importerror-gguf" >}} — ImportError: gguf
- {{< relref "importerror-llama-cpp" >}} — ImportError: llama_cpp
- {{< relref "importerror-ctransformers" >}} — ImportError: ctransformers
