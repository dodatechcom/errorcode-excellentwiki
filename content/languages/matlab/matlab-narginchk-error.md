---
title: "[Solution] MATLAB narginchk/nargoutchk — Too Few or Too Many Arguments"
description: "Fix MATLAB narginchk and nargoutchk errors when calling functions with incorrect argument count."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 100
---

## Common Causes

- Calling a function with fewer arguments than required by `narginchk`
- Passing more output arguments than declared in `nargoutchk`
- Missing default value handling in functions with optional arguments
- Confusing `nargin` checks with `narginchk` calls
- Using `narginchk` with incorrect min/max bounds

## How to Fix

```matlab
% WRONG: narginchk with reversed arguments
function result = myFunc(a, b)
    narginchk(3, 3);  % Error: requires 3 args but function only takes 2
    result = a + b;
end

% CORRECT: Match narginchk bounds to function signature
function result = myFunc(a, b, c)
    narginchk(2, 3);
    if nargin < 3
        c = 0;
    end
    result = a + b + c;
end
```

```matlab
% WRONG: Missing nargoutchk for fixed output
function [x, y] = divide(a, b)
    % No output validation
    x = a / b;
    y = a - b * floor(a/b);
end
[y] = divide(10, 3);  % Error: too many output args requested from caller perspective if misused

% CORRECT: Use nargoutchk to enforce output count
function [x, y] = divide(a, b)
    nargoutchk(1, 2);
    x = a / b;
    y = a - b * floor(a / b);
end
```

```matlab
% CORRECT: Validate both input and output counts
function varargout = processSignal(data, varargin)
    narginchk(1, 3);
    nargoutchk(0, nargin);

    dim = 1;
    winSize = 5;
    if nargin >= 2, dim = varargin{1}; end
    if nargin >= 3, winSize = varargin{2}; end

    result = movmean(data, winSize, dim);

    if nargout >= 1, varargout{1} = result; end
    if nargout >= 2, varargout{2} = mean(result, dim); end
end
```

```matlab
% CORRECT: Use arguments block (R2019b+) with automatic validation
function result = compute(a, b, opts)
    arguments
        a (1,:) double
        b (1,:) double
        opts.Scale (1,1) double = 1.0
        opts.Method string {mustBeMember(opts.Method, ["linear","pchip"])} = "linear"
    end
    result = opts.Scale * interp1(a, b, linspace(a(1), a(end), 100), opts.Method);
end
```

```matlab
% CORRECT: Variable argument handling with varargout
function varargout = multiReturn(data)
    narginchk(1, 1);
    nargoutchk(0, 3);

    outputs{1} = mean(data);
    outputs{2} = std(data);
    outputs{3} = median(data);

    for k = 1:min(nargout, numel(outputs))
        varargout{k} = outputs{k};
    end
end

[m, s] = multiReturn(randn(100,1));  % Returns mean and std only
```

## Examples

```matlab
% Example: Building a wrapper that safely forwards arguments
function varargout = safeWrapper(funcName, varargin)
    narginchk(1, Inf);
    func = str2func(funcName);
    try
        [varargout{1:nargout(funcName)}] = func(varargin{:});
    catch ME
        error('Wrapper failed for %s: %s', funcName, ME.message);
    end
end
```

## Related Errors

- [Too Many Arguments](matlab-too-many-args-v2) — argument count mismatch
- [Error Function](matlab-error-function) — error vs warning usage
- [Try/Catch](matlab-try-catch) — error handling best practices
