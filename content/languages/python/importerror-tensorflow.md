---
title: "[Solution] Python ImportError: tensorflow — Missing C Extensions"
description: "Fix Python ImportError: tensorflow. Reinstall TensorFlow, resolve CUDA/GPU issues, and fix incompatible protobuf versions."
languages: ["python"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 5
---

# ImportError: tensorflow

An `ImportError: cannot import name 'X' from 'tensorflow'` or `ModuleNotFoundError: No module named 'tensorflow'` occurs when TensorFlow cannot be imported due to missing packages, version mismatches, or GPU driver issues.

## Description

TensorFlow has multiple dependencies (protobuf, h5py, grpcio, numpy) and GPU builds require CUDA/cuDNN. Common variants:

- `ImportError: cannot import name 'distutils' from 'numpy'`
- `ImportError: dll load failed while importing _pywrap_tensorflow` (Windows)
- `ImportError: libcudart.so.11.0: cannot open shared object file`

## Common Causes

```python
# Cause 1: TensorFlow not installed
import tensorflow as tf  # ModuleNotFoundError

# Cause 2: Incompatible protobuf version
import tensorflow as tf  # ImportError: cannot google.protobuf

# Cause 3: GPU build without CUDA installed
import tensorflow as tf  # ImportError: libcudart.so

# Cause 4: Python version not supported
import tensorflow as tf  # ImportError on Python 3.12
```

## How to Fix

### Fix 1: Install TensorFlow for your platform

```bash
# CPU only
pip install tensorflow

# GPU support (Linux only, requires CUDA 12.x)
pip install tensorflow[and-cuda]

# macOS Apple Silicon
pip install tensorflow-macos tensorflow-metal
```

### Fix 2: Fix protobuf version conflicts

```bash
pip install --upgrade protobuf tensorflow
# Or pin a compatible version
pip install protobuf>=3.20,<5 tensorflow
```

### Fix 3: Verify GPU availability

```python
import tensorflow as tf
print(tf.config.list_physical_devices("GPU"))
```

## Related Errors

- [RuntimeError: CUDA out of memory](torch-cuda) — GPU memory exhaustion
- [ImportError: numpy — Missing C Extensions](importerror-numpy) — related native extension issue
- [InternalError: CUDA](tensorflow-gpu) — GPU runtime failure
