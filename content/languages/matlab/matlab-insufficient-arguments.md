---
title: "[Solution] MATLAB Not Enough Input Arguments"
description: "Fix 'Not enough input arguments' when calling MATLAB functions without required parameters."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

"Not enough input arguments" occurs when a function is called without all required input parameters. MATLAB checks argument count at runtime.

## Common Causes

- Missing required function arguments
- Function expects varargin but none provided
- Script calling function incorrectly
- Anonymous function missing bound variables

## How to Fix

```matlab
% WRONG: Function requires 2 args, only 1 provided
function result = add(a, b)
    result = a + b;
end
add(5)   % Error: not enough input arguments

% CORRECT: Provide all arguments
add(5, 3)   % 8
```

```matlab
% CORRECT: Use nargin to check
function result = add(a, b)
    if nargin < 2
        error('Not enough input arguments. Usage: add(a, b)');
    end
    result = a + b;
end
```

## Examples

```matlab
function greet(name, time)
    fprintf('Good %s, %s\n', time, name);
end
greet('Alice')   % Error: not enough input arguments
greet('Alice', 'morning')   % Works
```

## Related Errors

- [Too Many Arguments](matlab-too-many-arguments) - argument count errors
- [Undefined Function](matlab-undefined-function) - function errors
