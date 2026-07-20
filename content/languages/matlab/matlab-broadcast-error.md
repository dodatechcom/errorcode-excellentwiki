---
title: "[Solution] MATLAB Broadcast Variable — Size Mismatch and Worker Memory"
description: "Fix MATLAB broadcast variable errors: size mismatch, worker memory issues, and automatic broadcasting rules."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 108
---

## Common Causes

- Automatic broadcasting fails when trailing dimensions don't match
- Large broadcast variables exhaust worker memory in `parfor`
- Implicit expansion introduced in R2016b breaking legacy element-wise code
- Confusing scalar expansion with true broadcasting
- Broadcasting across incompatible singleton dimensions

## How to Fix

```matlab
% WRONG: Dimension mismatch not compatible with broadcasting
A = rand(3, 4);
B = rand(3, 1);
C = A + B;  % Works via broadcasting: B expands along dim 2

D = rand(4, 3);
E = A + D;  % Error: dimensions 4 vs 3 don't match

% CORRECT: Reshape or transpose to match broadcasting rules
D = rand(3, 1);
E = A + D;  % Works: D broadcasts along dim 2
```

```matlab
% WRONG: Implicit expansion breaks old code that assumed error on size mismatch
a = [1 2 3];      % 1x3
b = [1; 2; 3];    % 3x1
c = a + b;         % Now returns 3x3 instead of error (R2016b+)

% CORRECT: Explicitly control with bsxfun or verify dimensions
a = [1 2 3];
b = [1; 2; 3];
c = bsxfun(@plus, a, b);   % Explicit broadcast (same as a + b)
% If you want element-wise: ensure same size
b2 = [1 2 3];
c2 = a + b2;               % 1x3 + 1x3 = 1x3
```

```matlab
% CORRECT: Use pagefun for high-dimensional broadcasting (GPU)
% For CPU, verify dimensions manually for clarity
function C = safeBroadcastAdd(A, B)
    szA = size(A);
    szB = size(B);

    % Pad shorter size with 1s for comparison
    maxDims = max(numel(szA), numel(szB));
    szA(end+1:maxDims) = 1;
    szB(end+1:maxDims) = 1;

    compatible = all(szA == szB | szA == 1 | szB == 1);
    if ~compatible
        error('Dimensions %s and %s are not compatible for broadcasting', ...
            mat2str(size(A)), mat2str(size(B)));
    end

    C = A + B;
end
```

```matlab
% CORRECT: Avoid large broadcast variables in parfor
% WRONG: broadcasting large matrix to every worker
parfor k = 1:1000
    results(k) = sum(largeMatrix(k, :) .* broadcastVector);  % broadcastVector copied to each worker
end

% CORRECT: Partition the data explicitly
nWorkers = 4;
chunkSize = ceil(1000 / nWorkers);
parfor k = 1:1000
    rowIdx = k;
    results(k) = sum(largeMatrix(rowIdx, :) .* broadcastVector);
end
```

```matlab
% CORRECT: Explicitly avoid implicit expansion when not desired
% Use .^ instead of .^ for scalar, or control with bsxfun
A = rand(3, 1);
B = rand(1, 3);
C = A + B;           % 3x3 via broadcasting

% If you want error on mismatch, pre-check:
if ~isequal(size(A), size(B)) && ~(isscalar(A) || isscalar(B))
    error('Sizes must match for element-wise operation without broadcasting');
end
```

## Examples

```matlab
% Example: Broadcasting with proper dimension management
x = 1:5;              % 1x5
y = (1:5)';           % 5x1
z = x + y;            % 5x5 matrix via broadcasting

% Verify expected behavior
assert(isequal(size(z), [5 5]), 'Expected 5x5 output from broadcasting');
assert(z(1,1) == x(1) + y(1), 'First element should be sum of first elements');
```

## Related Errors

- [Dimension Mismatch](matlab-dimension-mismatch-v2) — array sizing
- [SPMD Error](matlab-spmd-error) — parallel variable distribution
- [parfor Error](matlab-parfor-error) — parfor variable classification
