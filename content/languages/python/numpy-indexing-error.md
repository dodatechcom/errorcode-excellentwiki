---
title: "[Solution] Python NumPy Advanced Indexing Error — How to Fix"
description: "Fix Python NumPy advanced indexing errors. Resolve boolean indexing, fancy indexing, and array shape mismatch issues."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python NumPy Advanced Indexing Error

NumPy advanced indexing errors occur when array indexing operations use incompatible shapes, invalid index types, or mismatched boolean masks. These errors are common when transitioning from basic to advanced array operations.

## Why It Happens

NumPy supports basic integer indexing and advanced indexing (boolean arrays, integer arrays). Advanced indexing creates copies, not views, and requires shapes to be broadcastable. Shape mismatches or type errors cause IndexError or ValueError.

## Common Error Messages

- `IndexError: too many indices for array: array is 2-dimensional`
- `IndexError: boolean index did not match indexed array along dimension 0`
- `ValueError: shape mismatch: value array could not be broadcast`
- `IndexError: index 5 is out of bounds for axis 0 with size 5`

## How to Fix It

### Fix 1: Match boolean mask shape to array

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
mask = np.array([True, False, True, False, True])
result = arr[mask]  # [1, 3, 5]
```

### Fix 2: Use np.where for conditional indexing

```python
import numpy as np

arr = np.arange(10)
indices = np.where(arr > 5)
result = arr[indices]  # [6, 7, 8, 9]
```

### Fix 3: Fix broadcast shape for assignment

```python
import numpy as np

arr = np.zeros((3, 4))
arr[0:2, 0:2] = np.array([[1, 2], [3, 4]])
```

### Fix 4: Use np.ix_ for cross-indexing

```python
import numpy as np

arr = np.arange(12).reshape(3, 4)
rows = [0, 2]
cols = [1, 3]
result = arr[np.ix_(rows, cols)]
```

## Common Scenarios

- **DataFrame to NumPy** — Pandas .values returns object arrays causing indexing failures.
- **Image processing** — Boolean masks from thresholding don't match image dimensions.
- **Batch operations** — Index arrays from different sources have incompatible lengths.

## Prevent It

- Always verify array shapes with arr.shape before advanced indexing
- Use np.ix_() for cross-indexing
- Check np.array_equal(mask.shape, arr.shape) before boolean indexing

## Related Errors

- - [IndexError](/languages/python/indexerror/) — list index out of range
- - [ValueError](/languages/python/valueerror/) — invalid argument value
