---
title: "[Solution] MATLAB cellfun/arrayfun/structfun — UniformOutput and ErrorHandler"
description: "Fix MATLAB cellfun, arrayfun, and structfun errors with UniformOutput, ErrorHandler, and size matching."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 106
---

## Common Causes

- Function returns variable-size outputs without `UniformOutput`, false
- `cellfun` called with non-cell input or mismatched cell sizes
- Function handle throws error inside `cellfun` with no `ErrorHandler`
- `structfun` applied to non-struct or scalar-struct mismatch
- `arrayfun` with function that returns different-size arrays per element

## How to Fix

```matlab
% WRONG: UniformOutput default causes error for non-scalar results
C = {'hello', 'world', 'foo'};
lengths = cellfun(@length, C);  % Works — scalar outputs

names = cellfun(@(x) x(1:2), C);  % Fails — variable-length output

% CORRECT: Disable UniformOutput for variable-size results
names = cellfun(@(x) x(1:2), C, 'UniformOutput', false);
```

```matlab
% WRONG: No ErrorHandler — first failure stops everything
C = {1, 'not_a_number', 3};
results = cellfun(@double, C);  % Error on second element

% CORRECT: Use ErrorHandler to gracefully handle failures
results = cellfun(@double, C, ...
    'UniformOutput', false, ...
    'ErrorHandler', @(x, varargin) NaN);
```

```matlab
% CORRECT: arrayfun with size matching
A = [1 2 3; 4 5 6];
% WRONG: Function returns scalar for each element but UniformOutput matters
squares = arrayfun(@(x) x^2, A);  % Returns 2x3 array (works)

% For cell output:
results = arrayfun(@(x) {x^2, x^3}, A, 'UniformOutput', false);
```

```matlab
% CORRECT: structfun with validation
S = struct('a', 1, 'b', 'hello', 'c', [1 2 3]);
isNumericField = structfun(@isnumeric, S);  % Returns [true; false; true]

% Filter to only numeric fields
numFields = fieldnames(S);
for k = 1:numel(numFields)
    if isnumeric(S.(numFields{k}))
        disp([numFields{k} ': ' mat2str(S.(numFields{k}))]);
    end
end
```

```matlab
% CORRECT: Parallel cellfun with parfor (avoid nested parallelism)
% WRONG:
result = cellfun(@slowFunc, C, 'UniformOutput', false);
% CORRECT: Use parfor if slowFunc is expensive
parfor k = 1:numel(C)
    result{k} = slowFunc(C{k});
end
```

## Examples

```matlab
% Example: cellfun with error logging
function results = safeCellfun(func, C)
    n = numel(C);
    results = cell(size(C));
    errors = false(size(C));

    for k = 1:n
        try
            results{k} = func(C{k});
        catch ME
            errors(k) = true;
            results{k} = [];
            fprintf('cellfun failed at index %d: %s\n', k, ME.message);
        end
    end

    fprintf('%d/%d calls succeeded\n', sum(~errors), n);
end
```

## Related Errors

- [parfor Error](matlab-parfor-error) — parallel cell operations
- [Try/Catch](matlab-try-catch) — error handling in callbacks
- [Container Map](matlab-containers-map) — struct alternatives
