---
title: "[Solution] MATLAB: Matrix dimensions must agree"
description: "Fix MATLAB errors when matrix operations have mismatched dimensions."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["dimensions", "matrix", "mismatch", "size", "array", "matlab"]
weight: 5
---

## What This Error Means

MATLAB errors "Matrix dimensions must agree" when performing element-wise operations on arrays of different sizes, or when matrix multiplication dimensions are incompatible.

## Common Causes

- Element-wise operation on different-sized arrays
- Matrix multiplication dimension mismatch
- Broadcasting not applicable
- Incorrect matrix transpose
- Scalar vs vector mismatch

## How to Fix

```matlab
% WRONG: Different sized arrays
A = [1, 2, 3];
B = [1, 2];
C = A + B;  % Error: dimensions don't match

% CORRECT: Ensure matching dimensions
A = [1, 2, 3];
B = [1, 2, 3];
C = A + B;  % Works: both 1x3
```

```matlab
% WRONG: Matrix multiplication dimensions
A = [1, 2, 3];      % 1x3
B = [1, 2, 3];      % 1x3
C = A * B;           % Error: 1x3 * 1x3 invalid

% CORRECT: Match dimensions for multiplication
A = [1, 2, 3];      % 1x3
B = [1; 2; 3];      % 3x1
C = A * B;           % Works: 1x3 * 3x1 = 1x1
```

```matlab
% CORRECT: Use element-wise operations
A = [1, 2, 3];
B = [4, 5, 6];
C = A .* B;          % Element-wise multiply
D = A ./ B;          % Element-wise divide
```

```matlab
% CORRECT: Use size checking
function result = safeMultiply(A, B)
    if size(A, 2) ~= size(B, 1)
        error('Matrix dimensions must agree');
    end
    result = A * B;
end
```

## Related Errors

- [Index Out of Range](matlab-index-out-of-range-v2) - array bounds
- [Invalid Function Handle](matlab-invalid-function-handle-v2) - function issues
- [Too Many Arguments](matlab-too-many-args-v2) - argument errors
