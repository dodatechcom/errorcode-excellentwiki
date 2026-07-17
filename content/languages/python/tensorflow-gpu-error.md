---
title: "[Solution] TensorFlow CUDA Error: Could Not Create CUDA Runtime Fix"
description: "Fix TensorFlow CUDA error could not create CUDA runtime. Configure GPU visibility, CUDA toolkit, and driver compatibility."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["tensorflow", "cuda", "gpu", "runtime", "gpu-error"]
weight: 5
---

# CUDA Error: Could Not Create CUDA Runtime — TensorFlow Fix

A `tensorflow.python.framework.errors_impl.InternalError: CUDA: could not create CUDA runtime` is raised when TensorFlow cannot initialize the CUDA runtime, preventing GPU-accelerated computation.

## What This Error Means

Common messages:

- `InternalError: CUDA: could not create CUDA runtime`
- `Could not load dynamic library 'libcudart.so'`
- `RuntimeError: CUDA runtime is not available`

TensorFlow attempted to initialize CUDA but failed. This typically indicates a mismatch between TensorFlow, CUDA toolkit, and NVIDIA driver versions, or a GPU not being accessible.

## Common Causes

```python
# Cause 1: CUDA toolkit not installed or not on LD_LIBRARY_PATH
import tensorflow as tf
tf.config.list_physical_devices('GPU')  # Returns empty list

# Cause 2: Driver version incompatible with CUDA version
# Driver 470.x requires CUDA 11.x, not CUDA 12.x

# Cause 3: GPU already claimed by another process
# nvidia-smi shows 100% memory usage from another process

# Cause 4: Docker container without GPU access
# docker run tensorflow/tensorflow  # Missing --gpus flag
```

## How to Fix

### Fix 1: Verify CUDA toolkit and driver compatibility

```bash
# Check NVIDIA driver version
nvidia-smi

# Check CUDA version
nvcc --version

# TensorFlow 2.15 requires CUDA 12.2 and cuDNN 8.9
# TensorFlow 2.10 requires CUDA 11.2 and cuDNN 8.1
```

### Fix 2: Install matching TensorFlow GPU package

```bash
pip install tensorflow[and-cuda]
# Or for specific version:
pip install tensorflow==2.15.0
```

### Fix 3: Set GPU visibility and memory growth

```python
import tensorflow as tf

# List available GPUs
gpus = tf.config.list_physical_devices('GPU')
print(f"Available GPUs: {gpus}")

# Enable memory growth to avoid allocating all VRAM at once
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)
```

### Fix 4: Restrict TensorFlow to specific GPU

```python
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

import tensorflow as tf
```

### Fix 5: Docker with GPU access

```bash
# Wrong — no GPU passthrough
docker run tensorflow/tensorflow

# Correct — pass --gpus flag
docker run --gpus all tensorflow/tensorflow
```

### Fix 6: Set library paths manually

```bash
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
export CUDA_HOME=/usr/local/cuda
```

## Related Errors

- {{< relref "importerror-tensorflow" >}} — TensorFlow import or installation issue.
- {{< relref "torch-cuda-error" >}} — PyTorch CUDA out of memory error.
