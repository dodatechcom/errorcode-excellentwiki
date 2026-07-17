---
title: "[Solution] Python ImportError: vllm with CUDA not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: vllm with CUDA not found. Install vllm with proper CUDA support."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: vllm with CUDA not found — ModuleNotFoundError Fix

This error occurs when trying to use vllm but CUDA is not properly configured or vllm cannot find the CUDA runtime.

## What This Error Means

vllm requires CUDA to run. The error can mean CUDA is not installed, not compatible, or vllm cannot find the CUDA libraries.

## Common Causes

```python
# Cause 1: CUDA not installed
import vllm  # ImportError: CUDA not found

# Cause 2: CUDA version mismatch
# vllm requires specific CUDA version

# Cause 3: GPU not available
```

## How to Fix

### Fix 1: Verify CUDA installation

```bash
nvidia-smi
nvcc --version
```

### Fix 2: Install vllm with correct CUDA version

```bash
# For CUDA 12.1
pip install vllm

# Check CUDA compatibility
python -c "import torch; print(torch.cuda.is_available())"
```

### Fix 3: Install PyTorch with CUDA first

```bash
pip install torch --index-url https://download.pytorch.org/whl/cu121
pip install vllm
```

## Related Errors

- {{< relref "importerror-vllm" >}} — ImportError: vllm
- {{< relref "importerror-tgi" >}} — ImportError: text-generation-inference
- {{< relref "importerror-torch" >}} — ImportError: torch
