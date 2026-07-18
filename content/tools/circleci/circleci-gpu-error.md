---
title: "[Solution] CircleCI GPU Error"
description: "Fix CircleCI gpu errors. Learn why this happens and how to resolve it quickly."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# CircleCI GPU Error

CircleCI GPU errors occur when GPU-enabled jobs fail to provision or execute correctly.

## Why This Happens

- GPU not available
- CUDA version mismatch
- Driver not installed
- Resource class invalid

## Common Error Messages

- `gpu_error`
- `cuda_error`
- `driver_error`
- `gpu_resource_error`

## How to Fix It

### Solution 1: Use GPU resource class

Specify GPU-enabled resource class:

```yaml
jobs:
  train:
    machine:
      image: ubuntu-2204:2023.10.1
    resource_class: gpu.nvidia.small
```

### Solution 2: Install CUDA

Use appropriate CUDA version:

```yaml
- run:
    name: Install CUDA
    command: |
      apt-get update && apt-get install -y nvidia-cuda-toolkit
```

### Solution 3: Verify GPU access

Check GPU availability:

```yaml
- run:
    command: nvidia-smi
```


## Common Scenarios

- **GPU not found:** Check resource class availability.
- **CUDA mismatch:** Use compatible CUDA and driver versions.

## Prevent It

- Use supported GPU classes
- Verify CUDA compatibility
- Monitor GPU usage
