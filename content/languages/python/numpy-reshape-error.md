---
title: "[Solution] NumPy ValueError: Cannot Reshape Array Fix"
description: "Fix NumPy ValueError cannot reshape array of size X into shape Y. Check array dimensions and total element count."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["numpy", "reshape", "valueerror", "array", "dimensions"]
weight: 5
---

# ValueError: Cannot Reshape Array — NumPy Fix

A `ValueError: cannot reshape array of size X into shape (Y, Z)` is raised when the total number of elements in the array does not match the product of the target shape dimensions.

## What This Error Means

Common messages:

- `ValueError: cannot reshape array of size 150 into shape (10,10)`
- `ValueError: cannot reshape array of size 784 into shape (28,28,4)`

NumPy's `reshape()` requires that the total element count is exactly divisible by the target shape. A shape of `(10, 10)` requires exactly 100 elements, not 150.

## Common Causes

```python
import numpy as np

# Cause 1: Mismatched dimensions with data size
data = np.arange(150)
data.reshape(10, 10)  # 150 != 10*10 (100)

# Cause 2: Off-by-one in computed shape
data = np.arange(785)
data.reshape(28, 28, 1)  # 785 != 28*28*1 (784)

# Cause 3: Wrong number of dimensions
data = np.arange(24)
data.reshape(4, 4)  # 24 != 4*4 (16)

# Cause 4: Loading flat data with incorrect expected shape
flat = np.fromfile("image.bin", dtype=np.uint8)
flat.reshape(480, 640, 3)  # File has wrong byte count
```

## How to Fix

### Fix 1: Verify element count before reshaping

```python
data = np.arange(150)
target_shape = (10, 10)

if data.size != np.prod(target_shape):
    print(f"Size mismatch: {data.size} vs {target_shape}")
else:
    data.reshape(target_shape)
```

### Fix 2: Use -1 for inferred dimension

```python
data = np.arange(150)

# Let NumPy infer the second dimension
data.reshape(15, -1)  # (15, 10)
data.reshape(-1, 10)  # (15, 10)
data.reshape(5, -1)   # (5, 30)
```

### Fix 3: Pad or truncate to match target shape

```python
data = np.arange(150)
target = 10 * 10  # 100

# Truncate
truncated = data[:target].reshape(10, 10)

# Pad with zeros
padded = np.pad(data, (0, data.size - target)).reshape(10, 10)
```

### Fix 4: Flatten before reshaping to ensure contiguous layout

```python
data = np.arange(150)
data.reshape(15, 10)  # Works
data.ravel().reshape(15, 10)  # Also works, guaranteed contiguous
```

### Fix 5: Handle file loading mismatches

```python
import os

expected = 28 * 28 * 3  # 2352 bytes
actual = os.path.getsize("image.bin")

if actual != expected:
    print(f"File has {actual} bytes, expected {expected}")
else:
    data = np.fromfile("image.bin", dtype=np.uint8).reshape(28, 28, 3)
```

## Related Errors

- {{< relref "valueerror" >}} — General Python ValueError.
- {{< relref "memoryerror" >}} — Out-of-memory when creating large arrays.
