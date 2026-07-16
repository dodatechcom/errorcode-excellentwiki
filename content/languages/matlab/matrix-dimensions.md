---
title: "[Solution] MATLAB Matrix Dimensions Must Agree Error Fix"
description: "Fix 'Matrix dimensions must agree' when performing element-wise operations on arrays of incompatible size."
languages: ["matlab"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["matrix-dimensions", "dimension-mismatch", "matlab"]
weight: 5
---

# MATLAB Matrix Dimensions Must Agree Error Fix

This error occurs when element-wise arithmetic operators (`+`, `-`, `.*`, `./`) or certain functions are applied to arrays whose dimensions do not match. The message reads: `Matrix dimensions must agree.`

## Description

MATLAB requires that operands in element-wise operations have the same size, or one is a scalar (which broadcasts automatically). When you try to add, subtract, or multiply arrays of incompatible shapes — such as a 3×3 matrix and a 1×3 row vector — MATLAB raises this error. It does not apply to matrix multiplication (`*`), which has its own dimension rules.

## Common Causes

- **Adding vectors of different lengths** — `[1,2,3] + [1,2,3,4]`.
- **Mismatched row vs. column orientation** — `ones(3,1) + ones(1,3)` without explicit broadcasting.
- **Incorrect transpose** — forgetting to transpose a vector to match dimensions.
- **Mixing 2D matrices with 3D arrays** — operating on arrays with different numbers of dimensions.

## How to Fix

### Fix 1: Ensure both arrays have the same size

```matlab
% Wrong — different lengths
A = [1, 2, 3];
B = [10, 20, 30, 40];
C = A + B;  % Matrix dimensions must agree

% Correct — match lengths
A = [1, 2, 3];
B = [10, 20, 30];
C = A + B;
```

### Fix 2: Transpose vectors to match orientation

```matlab
% Wrong — column + row
A = [1; 2; 3];      % 3×1
B = [10, 20, 30];   % 1×3
C = A + B;  % Matrix dimensions must agree

% Correct — use compatible shapes
C = A + B';  % Both are 3×1

% Or use broadcasting (R2016b+)
C = A + B;  % Implicit expansion works in newer versions
```

### Fix 3: Use size to validate dimensions

```matlab
% Wrong — assuming compatible sizes
A = rand(4, 5);
B = rand(4, 3);
C = A .* B;  % Matrix dimensions must agree

% Correct — check before operation
if all(size(A) == size(B))
    C = A .* B;
else
    error('A is %s but B is %s', mat2str(size(A)), mat2str(size(B)))
end
```

### Fix 4: Repmat for explicit expansion

```matlab
% Wrong — dimension mismatch
A = [1; 2; 3];       % 3×1
B = [10, 20, 30, 40];  % 1×4
C = A + B;  % Error in older MATLAB

% Correct — use repmat
A_expanded = repmat(A, 1, 4);   % 3×4
B_expanded = repmat(B, 3, 1);   % 3×4
C = A_expanded + B_expanded;
```

## Examples

```matlab
>> [1,2] + [1,2,3]
Matrix dimensions must agree.

>> eye(3) + ones(2)
Matrix dimensions must agree.

>> rand(3,1) .* rand(1,3)
Matrix dimensions must agree. (Pre-2016b)
```

## Related Errors

- [Index Out of Bounds]({{< relref "/languages/matlab/index-out-of-bounds" >}}) — accessing an array element beyond its dimensions.
- [Invalid Identifier]({{< relref "/languages/matlab/invalid-identifier" >}}) — syntax error in MATLAB expressions.
