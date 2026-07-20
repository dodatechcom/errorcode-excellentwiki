---
title: "[Solution] MATLAB assert() Failure — Assertion Error with Custom Messages"
description: "Fix MATLAB assert() failures with proper condition checks, custom error messages, and debugging strategies."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 101
---

## Common Causes

- Assertion condition evaluates to `false` or empty
- Comparing floating-point numbers with exact equality in `assert`
- Missing error message providing context for failure
- Using `assert` on operations with side effects that change state
- Assertion conditions that don't account for `NaN` or empty arrays

## How to Fix

```matlab
% WRONG: Floating-point exact comparison
x = 0.1 + 0.2;
assert(x == 0.3);  % Fails due to floating-point rounding

% CORRECT: Use tolerance-based comparison
x = 0.1 + 0.2;
assert(abs(x - 0.3) < 1e-10, 'Expected 0.3 but got %.15f', x);
```

```matlab
% WRONG: No diagnostic message
assert(size(A, 1) == size(B, 1));

% CORRECT: Include descriptive error message
assert(size(A, 1) == size(B, 1), ...
    'Matrix row count mismatch: A has %d rows, B has %d rows', ...
    size(A, 1), size(B, 1));
```

```matlab
% WRONG: Assertion with side effects
assert(length(data) > 0, 'Data is empty');
result = data(1);  % Will error if data is empty and assertion is disabled

% CORRECT: Validate then act without side effects in condition
assert(~isempty(data) && length(data) > 0, 'Data must be non-empty');
result = data(1);
```

```matlab
% CORRECT: Assert with custom class for structured checks
function validateConfig(cfg)
    assert(isstruct(cfg), 'config must be a struct');
    assert(isfield(cfg, 'tolerance'), 'config.tolerance is required');
    assert(isfield(cfg, 'maxIter'), 'config.maxIter is required');
    assert(cfg.tolerance > 0 && cfg.tolerance < 1, ...
        'tolerance must be between 0 and 1, got %g', cfg.tolerance);
    assert(cfg.maxIter > 0 && mod(cfg.maxIter, 1) == 0, ...
        'maxIter must be a positive integer, got %g', cfg.maxIter);
end
```

```matlab
% CORRECT: Use verify (requires Testing Framework) or conditional assert
function testOutput()
    A = rand(3, 3);
    B = inv(A);
    product = A * B;
    I = eye(3);
    assert(max(abs(product(:) - I(:))) < 1e-10, ...
        'A * inv(A) should equal identity matrix');
end
```

## Examples

```matlab
% Example: Assertion in a unit test with detailed diagnostics
function testInterpolation()
    x = 0:0.1:pi;
    y = sin(x);
    xq = 0:0.01:pi;
    yq = interp1(x, y, xq, 'spline');

    err = max(abs(yq - sin(xq)));
    assert(err < 1e-2, ...
        'Spline interpolation error %.6f exceeds tolerance 0.01', err);
end
```

## Related Errors

- [Assertion Failed](matlab-assertion-failed) — classic assert issues
- [Error Function](matlab-error-function) — error reporting patterns
- [Dimension Mismatch](matlab-dimension-mismatch-v2) — size validation
