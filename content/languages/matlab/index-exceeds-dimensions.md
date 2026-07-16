---
title: "[Solution] MATLAB Index Exceeds Dimensions Error Fix"
description: "Fix 'Index exceeds the number of array elements' when accessing an array beyond its bounds."
languages: ["matlab"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["index-exceeds", "array", "bounds"]
weight: 5
---

# MATLAB Index Exceeds Dimensions Error Fix

This error occurs when you try to access an array element using an index that is larger than the array's size. The message reads: `Index exceeds the number of array elements. Check for incorrect bounds or use non-singleton dimensions.`

## Description

MATLAB arrays are 1-indexed (the first element is at index 1). If you reference an index beyond the array's length — or use 0 or a negative number — MATLAB throws this error. It's the most common MATLAB runtime error.

## Common Causes

- **Off-by-one in loop** — loop goes one past the array length.
- **Using 0 as an index** — MATLAB arrays start at 1, not 0.
- **Mismatched matrix dimensions** — indexing a 2D matrix with 3D indices or vice versa.
- **Array smaller than expected** — an operation produced fewer elements than anticipated.

## How to Fix

### Fix 1: Use `numel` or `length` to bound loops

```matlab
% Wrong — hard-coded upper bound
arr = [10, 20, 30];
for i = 1:4
    disp(arr(i))  % Error at i = 4
end

% Correct — use numel
arr = [10, 20, 30];
for i = 1:numel(arr)
    disp(arr(i))
end
```

### Fix 2: Remember MATLAB is 1-indexed

```matlab
% Wrong — trying to access index 0
arr = [10, 20, 30];
disp(arr(0))  % Error: index must be positive

% Correct — first element is index 1
disp(arr(1))  % Output: 10
```

### Fix 3: Check array size before indexing

```matlab
% Correct — verify dimensions before accessing
A = magic(3);  % 3x3 matrix
[r, c] = size(A);

rowIdx = 5;
colIdx = 2;
if rowIdx <= r && colIdx <= c
    disp(A(rowIdx, colIdx))
else
    disp('Index out of bounds')
end
```

### Fix 4: Preallocate arrays correctly

```matlab
% Wrong — growing array in loop causes index issues
result = [];
for i = 1:100
    result(i) = computeValue(i);  % Works but is slow
end

% Correct — preallocate with correct size
result = zeros(1, 100);
for i = 1:100
    result(i) = computeValue(i);
end
```

## Examples

```matlab
>> A = [1, 2, 3];
>> A(4)
Index exceeds the number of array elements. Index must not exceed 3.

>> A(0)
Index must be positive or zero.

>> M = zeros(2, 2);
>> M(3, 1)
Index exceeds the number of array elements. Check for incorrect bounds.
```

## Related Errors

- [Undefined Function or Variable](undefined-function.md) — calling a function or using a variable that doesn't exist.
