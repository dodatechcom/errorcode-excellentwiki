---
title: "[Solution] MATLAB feval() — Function Handle, str2func, and eval Alternatives"
description: "Fix MATLAB feval() errors with function handles, str2func validation, and safe alternatives to eval."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 105
---

## Common Causes

- Passing a string instead of a function handle to `feval`
- Using `eval` where `feval` or direct function calls are safer
- `str2func` returning invalid function handle for undefined functions
- Argument count mismatch between `feval` call and target function
- `feval` with built-in functions that expect different argument patterns

## How to Fix

```matlab
% WRONG: Passing string where function handle is expected
funcName = 'sin';
result = feval(funcName, x);  % Works but fragile

% CORRECT: Convert to validated function handle
funcName = 'sin';
func = str2func(funcName);
assert(isa(func, 'function_handle'), 'Invalid function: %s', funcName);
result = func(x);
```

```matlab
% WRONG: Using eval instead of feval
eval('result = myFunc(x, y)');  % Slow, hard to debug, security risk

% CORRECT: Use feval with function handle
func = @myFunc;
result = feval(func, x, y);
% Or even simpler:
result = func(x, y);
```

```matlab
% CORRECT: Safe feval wrapper with input validation
function varargout = safeFeval(funcName, varargin)
    if ischar(funcName) || isstring(funcName)
        func = str2func(funcName);
    elseif isa(funcName, 'function_handle')
        func = funcName;
    else
        error('Invalid function reference: expected string or function_handle');
    end
    [varargout{1:nargout}] = func(varargin{:});
end
```

```matlab
% CORRECT: Validate function existence before feval
function result = applyFunction(funcName, data)
    if exist(funcName, 'file') ~= 2 && exist(funcName, 'builtin') ~= 5
        error('Function "%s" not found on path', funcName);
    end
    func = str2func(funcName);
    result = func(data);
end
```

```matlab
% CORRECT: Use feval with cell array of function handles
functions = {@sin, @cos, @tan};
values = {linspace(0, pi, 100), linspace(0, 2*pi, 100), linspace(0, pi/2, 100)};

for k = 1:numel(functions)
    results{k} = feval(functions{k}, values{k});
end
```

## Examples

```matlab
% Example: Dynamic function dispatch without eval
function result = dispatch(operation, a, b)
    ops = struct('add', @plus, 'sub', @minus, ...
                 'mul', @times, 'div', @rdivide);
    if ~isfield(ops, operation)
        error('Unknown operation: %s', operation);
    end
    result = feval(ops.(operation), a, b);
end
```

## Related Errors

- [Invalid Function Handle](matlab-invalid-function-handle) — handle issues
- [Variable Not Found](matlab-variable-not-found) — undefined names
- [Error Function](matlab-error-function) — proper error messages
