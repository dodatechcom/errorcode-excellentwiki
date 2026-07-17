---
title: "[Solution] MATLAB: Undefined function or variable in scope"
description: "Fix MATLAB errors when variables or functions are not found in the current workspace scope."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

MATLAB errors "Undefined function or variable" when referencing a name that doesn't exist in the current workspace, function scope, or MATLAB path.

## Common Causes

- Variable defined in different workspace
- Function-local variable not accessible
- Variable cleared with clear command
- Workspace mismatch (base vs function)
- Variable name typo

## How to Fix

```matlab
% WRONG: Variable in different workspace
function result = example()
    x = 5;  % Local to function
end

% In command window:
disp(x);  % Error: x not in base workspace

% CORRECT: Return variable from function
function [result, x] = example()
    x = 5;
    result = x * 2;
end
```

```matlab
% WRONG: Using evalin incorrectly
function example()
    evalin('base', 'x = 10');  % Sets x in base workspace
end

% CORRECT: Use proper workspace sharing
function example()
    assignin('base', 'x', 10);  % Safer than evalin
end
```

```matlab
% CORRECT: Check variable existence
if exist('myVar', 'var')
    disp(myVar);
else
    myVar = defaultValue;
end
```

```matlab
% CORRECT: Use persistent variables carefully
function result = counter()
    persistent count;
    if isempty(count)
        count = 0;
    end
    count = count + 1;
    result = count;
end
```

```matlab
% CORRECT: Global variables (use sparingly)
global myGlobalVar;
myGlobalVar = 100;
```

## Related Errors

- [Undefined Function](matlab-undefined-function-v2) - function errors
- [Invalid Function Handle](matlab-invalid-function-handle-v2) - handle issues
- [Index Out of Range](matlab-index-out-of-range-v2) - array bounds
