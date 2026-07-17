---
title: "[Solution] MATLAB Index Exceeds Array Bounds Error Fix"
description: "Fix 'Index exceeds array bounds' when accessing an element beyond the dimensions of an array."
languages: ["matlab"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# MATLAB Index Exceeds Array Bounds Error Fix

This error occurs when you try to access an array element at an index that is greater than the size of the array. The message reads: `Index exceeds the number of array elements.`

## Description

MATLAB arrays are 1-indexed, meaning the first element is at index 1. Any attempt to access index 0, a negative index, or an index larger than the array's current size will trigger this error. It commonly appears when loops iterate beyond array boundaries or when dynamic resizing is not accounted for.

## Common Causes

- **Loop counter exceeds array length** — `for i = 1:10` on an array with only 5 elements.
- **Using 0 as an index** — `arr(0)` when MATLAB uses 1-based indexing.
- **Mismatched dimensions** — indexing a vector as if it were a 2D matrix.
- **Array smaller than expected** — a function returned fewer elements than anticipated.

## How to Fix

### Fix 1: Use numel or size to bound loops

```matlab
% Wrong — hard-coded bound exceeds array
arr = [10, 20, 30];
for i = 1:5
    disp(arr(i))  % Error at i = 4
end

% Correct — use numel
arr = [10, 20, 30];
for i = 1:numel(arr)
    disp(arr(i))
end
```

### Fix 2: Validate indices before accessing

```matlab
% Wrong — no bounds check
arr = [1, 2, 3];
idx = 5;
value = arr(idx);

% Correct — check bounds first
if idx >= 1 && idx <= numel(arr)
    value = arr(idx);
else
    error('Index %d is out of bounds (array has %d elements)', idx, numel(arr))
end
```

### Fix 3: Use end keyword for dynamic indexing

```matlab
% Wrong — assuming fixed length
arr = rand(1, 10);
lastThree = arr(8:10);  % Works only if length is exactly 10

% Correct — use end
lastThree = arr(end-2:end);
```

### Fix 4: Preallocate arrays to avoid size surprises

```matlab
% Wrong — growing array in loop can cause indexing confusion
for i = 1:100
    result(i) = i^2;
end

% Correct — preallocate
result = zeros(1, 100);
for i = 1:100
    result(i) = i^2;
end
```

## Examples

```matlab
>> A = [1, 2, 3];
>> A(5)
Index exceeds the number of array elements. Index must not exceed 3.

>> A(0)
Array indices must be positive integers or logical values.

>> M = rand(3, 3);
>> M(5, 1)
Index exceeds the number of array elements. Index must not exceed 3.
```

## Related Errors

- [Matrix Dimensions]({{< relref "/languages/matlab/matrix-dimensions" >}}) — matrix dimensions must agree for element-wise operations.
- [Undefined Function]({{< relref "/languages/matlab/undefined-function" >}}) — calling a function that doesn't exist.
