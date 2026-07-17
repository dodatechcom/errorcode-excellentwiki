---
title: "[Solution] MATLAB Index Exceeds Array Bounds"
description: "Fix 'Index exceeds array bounds' in MATLAB when accessing elements beyond array dimensions."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["index", "array-bounds", "subscript", "dimension", "matlab"]
weight: 5
---

## What This Error Means

MATLAB uses 1-based indexing. When you access an element beyond the array's size, you get "Index exceeds the number of array elements" error.

## Common Causes

- 0-based indexing (from other languages)
- Off-by-one error in loop bounds
- Array smaller than expected
- Dynamic array shrunk after allocation

## How to Fix

```matlab
% WRONG: 0-based indexing
a = [1, 2, 3];
disp(a(0))   % Error: index exceeds array bounds

% CORRECT: 1-based indexing
disp(a(1))   % 1
```

```matlab
% WRONG: Loop goes past array end
arr = [10, 20, 30];
for i = 1:5
    disp(arr(i))   % Error at i=4
end

% CORRECT: Use array length
for i = 1:length(arr)
    disp(arr(i))
end
```

## Examples

```matlab
a = [1, 2, 3];
a(5)          % Error: index exceeds array bounds
a(end+1) = 4  % Valid: extends array
```

## Related Errors

- [Dimension Mismatch](matlab-dimension-mismatch) - array compatibility
- [Undefined Function](matlab-undefined-function) - function errors
