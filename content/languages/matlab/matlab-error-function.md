---
title: "[Solution] MATLAB error() vs warning() vs MException — Error Reporting Done Right"
description: "Fix MATLAB error function usage: when to use error(), warning(), MException, and rethrow for proper error handling."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 102
---

## Common Causes

- Using `error()` where `warning()` is more appropriate (non-fatal issues)
- Calling `error()` inside a `try` block without preserving the original `MException`
- Forgetting `rethrow` when re-raising caught exceptions
- Using `error()` with unformatted strings causing injection-style issues
- Mixing `error('msg')` with `error(id, 'msg')` inconsistently

## How to Fix

```matlab
% WRONG: Using error() for non-fatal conditions
if ~isfile(filename)
    error('File not found');  % Kills the entire script
end

% CORRECT: Use warning() for non-fatal, continue with fallback
if ~isfile(filename)
    warning('File %s not found, using default', filename);
    filename = 'default.dat';
end
```

```matlab
% WRONG: Losing the exception context
try
    result = riskyOperation();
catch ME
    fprintf('Error: %s\n', ME.message);
    % Original stack trace is lost
end

% CORRECT: Use MException and rethrow or add context
try
    result = riskyOperation();
catch ME
    newME = MException('MyTool:OpFailed', ...
        'riskyOperation failed: %s', ME.message);
    newME = addCause(newME, ME);
    throw(newME);
end
```

```matlab
% CORRECT: Error with identifier and formatted message
function validateMatrix(A, name)
    if ~isnumeric(A)
        error('MyTool:InvalidInput', ...
            '%s must be numeric, got %s', name, class(A));
    end
    if ~ismatrix(A)
        error('MyTool:InvalidDims', ...
            '%s must be a 2D matrix, got %dD array', name, ndims(A));
    end
    if any(isnan(A(:)))
        warning('MyTool:NaNValues', '%s contains NaN values', name);
    end
end
```

```matlab
% CORRECT: Catch, log, and rethrow with additional context
function result = processWithLogging(data)
    try
        result = transform(data);
    catch ME
        logError(ME, 'processWithLogging');
        rethrow(ME);  % Preserve original exception
    end
end
```

```matlab
% CORRECT: Nested error handling with MException chain
function outer()
    try
        inner();
    catch ME
        wrapped = MException('Outer:Failed', 'Outer processing failed');
        wrapped = addCause(wrapped, ME);
        throw(wrapped);
    end
end

function inner()
    error('Inner:BadData', 'Data integrity check failed');
end
```

## Examples

```matlab
% Example: Choosing between error/warning based on severity
function result = processConfig(cfg)
    if ~isfield(cfg, 'timeout')
        warning('Config:MissingField', 'timeout not set, using 30s');
        cfg.timeout = 30;
    end
    if ~isfield(cfg, 'endpoint')
        error('Config:RequiredMissing', 'endpoint is mandatory');
    end
    result = webread(cfg.endpoint, 'Timeout', cfg.timeout);
end
```

## Related Errors

- [Try/Catch](matlab-try-catch) — catch block patterns
- [Assertion Failed](matlab-assertion-failed) — assert vs error
- [Stack Trace / dbstop](matlab-dbstop-error) — debugging errors
