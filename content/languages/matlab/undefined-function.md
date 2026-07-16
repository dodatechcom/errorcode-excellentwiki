---
title: "[Solution] MATLAB Undefined Function or Variable Error Fix"
description: "Fix 'Undefined function or variable X' when MATLAB cannot find a function or variable by that name."
languages: ["matlab"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["undefined-function", "undefined-variable", "not-found"]
weight: 5
---

# MATLAB Undefined Function or Variable Error Fix

This error occurs when MATLAB encounters a name it doesn't recognize as a function, variable, or class. The message reads: `Undefined function or variable 'X'.`

## Description

MATLAB searches for names in the following order: current workspace variables, subfunctions in the current file, private functions, class constructors, overloaded methods, functions on the path, and built-in functions. If no match is found, this error fires.

## Common Causes

- **Typo in function or variable name** — `LENGHT` instead of `LENGTH`.
- **Missing function on path** — the `.m` file exists but isn't in MATLAB's search path.
- **Variable not yet assigned** — using a variable before any assignment.
- **Missing toolbox** — the function requires a toolbox that isn't installed or licensed.

## How to Fix

### Fix 1: Check for typos using tab completion

```matlab
% Wrong
result = LENGHT([1, 2, 3]);

% Correct — use tab completion or check docs
result = length([1, 2, 3]);
```

### Fix 2: Add the function's directory to the path

```matlab
% Check if the file exists
which myFunction

% Add its directory to the path
addpath('/path/to/function/directory')

% Save the path for future sessions
savepath
```

### Fix 3: Assign variables before use

```matlab
% Wrong — x used before assignment
y = x + 5;  % Undefined function or variable 'x'.

% Correct — assign first
x = 10;
y = x + 5;
```

### Fix 4: Check if the required toolbox is installed

```matlab
% List installed toolboxes
ver

% Check if a specific toolbox is available
if ~isempty(ver('signal'))
    % Signal Processing Toolbox is available
    result = fft(data);
else
    error('Signal Processing Toolbox is required');
end
```

## Examples

```matlab
>> result = myFunc(42)
Undefined function or variable 'myFunc'.

>> n = COUNT([1,2,3])
Undefined function or variable 'COUNT'.
% Did you mean: length?

>> x = undeclaredVar + 1
Undefined function or variable 'undeclaredVar'.
```

## Related Errors

- [Index Out of Bounds]({{< relref "/languages/matlab/index-out-of-bounds" >}}) — accessing an array beyond its bounds.
- [Invalid Identifier]({{< relref "/languages/matlab/invalid-identifier" >}}) — malformed expression or identifier.
