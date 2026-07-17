---
title: "[Solution] MATLAB Dimensions of Arrays Are Not Compatible"
description: "Fix 'Dimensions of arrays are not compatible' when performing operations on arrays with mismatched sizes."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["dimension", "mismatch", "array-size", "matrix", "matlab"]
weight: 5
---

## What This Error Means

MATLAB requires arrays to have compatible dimensions for element-wise operations. "Dimensions of arrays are not compatible" means the arrays have different sizes and can't be operated on element-by-element.

## Common Causes

- Element-wise operation on different-sized arrays
- Missing dot operator (.*, ./, .^)
- Matrix multiplication instead of element-wise
- Reshape size mismatch

## How to Fix

```matlab
% WRONG: Different sizes
a = [1, 2, 3];
b = [1, 2];
c = a + b   % Error: dimensions not compatible

% CORRECT: Match sizes
a = [1, 2, 3];
b = [1, 2, 3];
c = a + b   % Works
```

```matlab
% WRONG: Missing dot operator
a = [1, 2, 3];
b = [4, 5, 6];
c = a * b     % Matrix multiply: dimension mismatch

% CORRECT: Element-wise multiply
c = a .* b    % [4, 10, 18]
```

## Examples

```matlab
A = ones(3, 3);
b = [1; 2; 3; 4];   % 4x1 vector
A * b               % Error: dimensions not compatible
```

## Related Errors

- [Index Out of Range](matlab-index-out-of-range) - index errors
- [Insufficient Arguments](matlab-insufficient-arguments) - argument errors
