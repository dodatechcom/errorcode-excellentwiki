---
title: "[Solution] Python ImportError: torch/PyTorch — Missing C Extensions"
description: "Fix Python ImportError: torch. Reinstall PyTorch, match CUDA versions, and resolve missing native libraries."
languages: ["python"]
severities: ["error"]
error_types: ["runtime-error"]
tags: ["importerror", "torch", "pytorch", "cuda", "installation"]
weight: 5
---

# ImportError: torch/PyTorch

An `ImportError: libcudart.so` or `ModuleNotFoundError: No module named 'torch'` indicates PyTorch cannot load its compiled extensions, often due to CUDA version mismatches or missing system libraries.

## Description

PyTorch ships separate builds for CPU-only and CUDA-enabled systems. Installing the wrong variant or having incompatible CUDA versions causes native extension failures.

- `ImportError: libcudart.so.12: cannot open shared object file`
- `ImportError: libcudnn.so.8: cannot open shared object file`
- `ImportError: cannot import name '_C' from 'torch'`

## Common Causes

```python
# Cause 1: PyTorch not installed
import torch  # ModuleNotFoundError

# Cause 2: CPU build installed but CUDA required
import torch  # ImportError: libcudart.so

# Cause 3: CUDA version mismatch
import torch  # ImportError: libcudnn.so.8

# Cause 4: Wrong Python version wheel
import torch  # ImportError from incompatible .so
```

## How to Fix

### Fix 1: Install from PyTorch website (recommended)

```bash
# Visit https://pytorch.org/get-started/locally/ for exact command
# CPU only
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# CUDA 12.4
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```

### Fix 2: Install CUDA toolkit

```bash
# Verify CUDA is available
nvidia-smi
nvcc --version

# Install CUDA toolkit matching your PyTorch build
# https://developer.nvidia.com/cuda-downloads
```

### Fix 3: Force reinstall

```bash
pip uninstall torch torchvision torchaudio -y
pip install torch torchvision torchaudio --no-cache-dir
```

## Related Errors

- [RuntimeError: CUDA out of memory](torch-cuda) — GPU memory exhaustion
- [ImportError: tensorflow](importerror-tensorflow) — similar GPU framework issue
- [InternalError: CUDA](tensorflow-gpu) — TensorFlow GPU failure
