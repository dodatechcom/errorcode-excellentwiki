---
title: "[Solution] MATLAB: Undefined function or variable 'X'"
description: "Fix MATLAB errors when functions or variables are undefined, including missing files and path issues."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

MATLAB errors "Undefined function or variable" when it cannot find a function or variable in the current workspace or MATLAB path. This can be due to missing files, path issues, or scope problems.

## Common Causes

- Function file not on MATLAB path
- Typo in function or variable name
- Function defined in different workspace
- Missing function file
- Package/namespace issues
- Case sensitivity (on some systems)

## How to Fix

```matlab
% WRONG: Function not on path
result = myFunction(5);  % Error: Undefined function 'myFunction'

% CORRECT: Add function to path
addpath('/path/to/functions');
result = myFunction(5);
```

```matlab
% WRONG: Variable not in scope
function result = example()
    x = 5;  % Local variable
end

function other()
    disp(x);  % Error: x not defined here
end

% CORRECT: Pass variable as argument
function result = example()
    x = 5;
    other(x);
end

function other(x)
    disp(x);
end
```

```matlab
% CORRECT: Check if function exists
if exist('myFunction', 'file') == 2
    result = myFunction(5);
else
    error('Function myFunction not found');
end
```

```matlab
% CORRECT: Use full path
fullPath = fullfile('/path', 'to', 'functions', 'myFunction.m');
if exist(fullPath, 'file')
    run(fullPath);
end
```

## Related Errors

- [Index Out of Range](matlab-index-out-of-range-v2) - array bounds
- [Invalid Function Handle](matlab-invalid-function-handle-v2) - handle issues
- [Variable Not Found](matlab-variable-not-found-v2) - scope issues
