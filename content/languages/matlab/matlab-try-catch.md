---
title: "[Solution] MATLAB try/catch — Rethrow, catch ME, and Best Practices"
description: "Fix MATLAB try/catch usage: proper exception capture, rethrow patterns, catch ME.message access, and error recovery."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 103
---

## Common Causes

- `catch` without capturing `ME` making exception details inaccessible
- Using `error()` in catch block instead of `rethrow` (loses stack trace)
- Swallowing exceptions silently with empty catch blocks
- Catching too broadly (entire function) instead of specific operations
- Accessing `ME.stack` without checking it exists first

## How to Fix

```matlab
% WRONG: Empty catch block swallows errors silently
try
    result = compute(data);
catch
    result = [];  % Error is silently lost
end

% CORRECT: Capture ME and log or rethrow
try
    result = compute(data);
catch ME
    warning('Compute failed: %s', ME.message);
    result = [];
end
```

```matlab
% WRONG: Raising new error loses original context
try
    result = parseJSON(jsonStr);
catch ME
    error('Parse failed');  % Original ME is lost
end

% CORRECT: Rethrow or chain the exception
try
    result = parseJSON(jsonStr);
catch ME
    rethrow(ME);  % Preserves original stack trace
end
```

```matlab
% CORRECT: MException chaining for multi-level context
try
    raw = readFile(filename);
    data = parseData(raw);
    result = transform(data);
catch ME
    cause = MException('Pipeline:StageFailed', ...
        'Pipeline failed at stage processing %s', filename);
    cause = addCause(cause, ME);
    throw(cause);
end
```

```matlab
% CORRECT: Retry pattern with try/catch
function result = retryOperation(func, maxRetries, varargin)
    for attempt = 1:maxRetries
        try
            result = func(varargin{:});
            return;
        catch ME
            fprintf('Attempt %d/%d failed: %s\n', attempt, maxRetries, ME.message);
            if attempt == maxRetries
                rethrow(ME);
            end
            pause(2^attempt);  % Exponential backoff
        end
    end
end
```

```matlab
% CORRECT: Targeted try/catch around specific lines
function result = process(dataset)
    validated = validateInput(dataset);      % This can throw
    result = struct();

    try
        result.fit = fitModel(validated);
    catch ME
        warning('Model fitting failed: %s', ME.message);
        result.fit = [];
    end

    result.stats = computeStats(validated);  % This can throw independently
end
```

## Examples

```matlab
% Example: Safe file processing with detailed error info
function data = safeLoad(filename)
    try
        data = load(filename);
    catch ME
        if strcmp(ME.identifier, 'MATLAB:load:couldNotReadFile')
            error('FileNotFound', 'Cannot open %s: %s', filename, ME.message);
        else
            rethrow(ME);
        end
    end
end
```

## Related Errors

- [Error Function](matlab-error-function) — error vs warning
- [dbstop if error](matlab-dbstop-error) — interactive debugging
- [fopen Error](matlab-fopen) — file access errors
