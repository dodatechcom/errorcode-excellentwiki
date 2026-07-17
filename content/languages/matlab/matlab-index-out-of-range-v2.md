---
title: "[Solution] MATLAB: Index exceeds array bounds"
description: "Fix MATLAB errors when array indexing goes beyond the array dimensions."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

MATLAB errors "Index exceeds array bounds" when you try to access an element using an index that is larger than the array size or less than 1.

## Common Causes

- Index exceeds array length
- Wrong dimension used for indexing
- Off-by-one error in loops
- Array smaller than expected
- Using 0-based indexing (MATLAB is 1-based)

## How to Fix

```matlab
% WRONG: Index exceeds bounds
arr = [1, 2, 3];
value = arr(5);  % Error: index 5 > length 3

% CORRECT: Check bounds first
arr = [1, 2, 3];
idx = 5;
if idx <= length(arr)
    value = arr(idx);
else
    disp('Index out of bounds');
end
```

```matlab
% WRONG: Loop goes beyond array
arr = [10, 20, 30, 40, 50];
for i = 1:10
    disp(arr(i));  % Error when i > 5
end

% CORRECT: Loop within bounds
arr = [10, 20, 30, 40, 50];
for i = 1:length(arr)
    disp(arr(i));
end
```

```matlab
% CORRECT: Use size instead of hardcoded values
arr = rand(3, 5);
for i = 1:size(arr, 1)
    for j = 1:size(arr, 2)
        arr(i, j) = i + j;
    end
end
```

```matlab
% CORRECT: Dynamic indexing with growth
arr = [];
for i = 1:10
    arr(i) = i^2;  % MATLAB auto-grows array
end
```

## Related Errors

- [Dimension Mismatch](matlab-dimension-mismatch-v2) - dimension errors
- [Undefined Function](matlab-undefined-function-v2) - function errors
- [Insufficient Arguments](matlab-insufficient-args-v2) - missing args
