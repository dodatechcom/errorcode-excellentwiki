---
title: "[Solution] MATLAB Not Enough Input Arguments Error Fix"
description: "Fix 'Not enough input arguments' when calling a function with fewer arguments than required."
languages: ["matlab"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# MATLAB Not Enough Input Arguments Error Fix

This error occurs when a function is called with fewer input arguments than its signature requires. The message reads: `Not enough input arguments.`

## Description

MATLAB functions define a specific number of required input arguments. If you call a function with fewer arguments than expected, MATLAB raises this error at the point where the missing argument is first referenced. This commonly happens when calling built-in functions with the wrong syntax or when using custom functions that require specific parameters.

## Common Causes

- **Missing required parameters** — calling `plot(y)` instead of `plot(x, y)`.
- **Forgetting optional arguments** — a function expects at least 2 inputs but only 1 is provided.
- **Calling a script as a function** — a script is executed with the function-call syntax.
- **Using `nargin` without a default** — the function's `nargin` check isn't handled.

## How to Fix

### Fix 1: Provide all required arguments

```matlab
% Wrong — missing x-coordinates
plot(y);

% Correct — provide both x and y
x = 1:10;
y = sin(x);
plot(x, y);
```

### Fix 2: Use nargin to set defaults

```matlab
function result = myFunction(a, b, c)
    % Wrong — assumes all arguments are provided
    result = a + b + c;

    % Correct — provide defaults for optional arguments
    if nargin < 2
        b = 1;
    end
    if nargin < 3
        c = 0;
    end
    result = a + b + c;
end
```

### Fix 3: Check with narginchk

```matlab
function myFunc(a, b, c)
    % Validate number of inputs
    narginchk(2, 3);  % Requires 2, allows up to 3
    
    if nargin < 3
        c = defaultC();
    end
    % Function body...
end
```

### Fix 4: Use varargin for variable-length inputs

```matlab
% Wrong — fixed arguments reject flexible calling
function result = sumAll(a, b)
    result = a + b;
end

% Correct — accept any number of inputs
function result = sumAll(varargin)
    result = sum([varargin{:}]);
end
```

## Examples

```matlab
>> max()
Not enough input arguments.

>> myCustomFunc(42)
Not enough input arguments.  % If myCustomFunc requires 2+ arguments

>> plot()
Not enough input arguments.
```

## Related Errors

- [Undefined Function]({{< relref "/languages/matlab/undefined-function" >}}) — calling a function that doesn't exist.
- [Invalid Identifier]({{< relref "/languages/matlab/invalid-identifier" >}}) — syntax errors in function calls.
