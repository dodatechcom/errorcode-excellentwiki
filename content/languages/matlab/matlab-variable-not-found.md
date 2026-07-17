---
title: "[Solution] MATLAB Undefined Function or Variable"
description: "Fix 'Undefined function or variable' when MATLAB cannot find a function or variable by name."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

MATLAB searches for names in order: workspace variables, subfunctions, private functions, class constructors, path functions, built-in functions. "Undefined" means no match found.

## Common Causes

- Typo in function or variable name
- Function not on MATLAB search path
- Variable used before assignment
- Missing toolbox for function
- Case sensitivity (MATLAB is case-sensitive)

## How to Fix

```matlab
% WRONG: Typo
result = LENGHT([1, 2, 3]);   % Undefined function

% CORRECT: Use correct name
result = length([1, 2, 3]);
```

```matlab
% CORRECT: Add function directory to path
addpath('/path/to/function/directory')
savepath
```

## Examples

```matlab
>> result = myFunc(42)
Undefined function or variable 'myFunc'.
>> x = undeclaredVar + 1
Undefined function or variable 'undeclaredVar'.
```

## Related Errors

- [Index Out of Range](matlab-index-out-of-range) - index errors
- [Invalid Function Handle](matlab-invalid-function-handle) - handle errors
