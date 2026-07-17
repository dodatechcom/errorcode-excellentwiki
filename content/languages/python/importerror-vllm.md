---
title: "[Solution] Python ImportError: vllm not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: vllm not found or ModuleNotFoundError: No module named 'vllm'. Install vllm properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "vllm", "module-not-found", "pip", "llm"]
weight: 5
---

# ImportError: vllm not found — ModuleNotFoundError Fix

An `ImportError: vllm not found` or `ModuleNotFoundError: No module named 'vllm'` means Python cannot locate the vllm package.

## What This Error Means

vllm is a high-throughput LLM serving engine. It requires CUDA and is not part of the standard library.

## Common Causes

```python
# Cause 1: vllm not installed
import vllm  # ModuleNotFoundError: No module named 'vllm'

# Cause 2: CUDA not available
# vllm requires GPU with CUDA support
```

## How to Fix

### Fix 1: Install with pip (requires CUDA)

```bash
pip install vllm
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install vllm
python -c "import vllm; print(vllm.__version__)"
```

## Related Errors

- {{< relref "importerror-vllm2" >}} — ImportError: vllm with CUDA
- {{< relref "importerror-tgi" >}} — ImportError: text-generation-inference
- {{< relref "importerror-ollama" >}} — ImportError: ollama
