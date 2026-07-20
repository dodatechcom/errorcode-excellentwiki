---
title: "[Solution] MATLAB mldivide (\\) — Singular, Rank Deficient, Least Squares"
description: "Fix MATLAB backslash operator errors: singular matrices, rank deficiency, least squares solutions, and warnings."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 122
---

## Common Causes

- Using `\` on a singular matrix producing warnings or Inf/NaN
- Non-square matrix with `\` not intended for least squares
- Rank deficiency not detected before solving
- Overdetermined system without expecting least squares result
- Underdetermined system producing minimum norm vs arbitrary solution

## How to Fix

```matlab
% WRONG: Singular matrix with backslash
A = [1 2; 2 4];
b = [3; 6];
x = A \ b;  % Warning: matrix is singular, solutions may not exist

% CORRECT: Use pinv for singular/underdetermined systems
x = pinv(A) * b;  % Minimum norm solution
```

```matlab
% WRONG: Assuming unique solution for overdetermined system
A = rand(100, 5);
b = rand(100, 1);
x = A \ b;  % Returns least squares but no residual info

% CORRECT: Use backslash with explicit residual check
[x, rnorm] = linsolve(A, b);
residual = norm(A * x - b);
fprintf('Residual norm: %g\n', residual);

% Or use explicit least squares
[Q, R] = qr(A, 0);
x = R \ (Q' * b);
```

```matlab
% CORRECT: Detect rank deficiency
A = [1 2 3; 4 5 6; 7 8 9];  % Rank 2
r = rank(A);
fprintf('Rank: %d (matrix is %dx%d)\n', r, size(A));

if r < min(size(A))
    % Use thresholded pinv
    [U, S, V] = svd(A, 'econ');
    tol = max(size(A)) * eps(S(1));
    S_inv = diag(1 ./ diag(S));
    S_inv(diag(S) < tol) = 0;
    x = V * S_inv * U' * b;
end
```

```matlab
% CORRECT: Explicitly choose between least squares and minimum norm
function x = smartSolve(A, b)
    [m, n] = size(A);
    if m >= n
        % Overdetermined: least squares
        x = A \ b;  % Or lsqminnorm(A, b) for minimum norm among LS
    else
        % Underdetermined: minimum norm
        x = lsqminnorm(A, b);  % R2017b+
        % Or: x = pinv(A) * b;
    end
end
```

```matlab
% CORRECT: Iterative refinement for ill-conditioned systems
function x = refinedSolve(A, b, maxIter)
    if nargin < 3, maxIter = 3; end
    x = A \ b;
    for k = 1:maxIter
        r = b - A * x;
        dx = A \ r;
        x = x + dx;
        if norm(dx) < 1e-14 * norm(x)
            break;
        end
    end
end
```

## Examples

```matlab
% Example: Polynomial fitting via least squares
x = linspace(0, 1, 20)';
y = sin(2*pi*x) + 0.1*randn(20, 1);

% Degree 3 polynomial: Vandermonde matrix
A = [x.^3, x.^2, x, ones(size(x))];
coeffs = A \ y;  % Least squares solution
y_fit = A * coeffs;

fprintf('Fit RMSE: %.4f\n', sqrt(mean((y - y_fit).^2)));
```

## Related Errors

- [Matrix Inversion](matlab-matrix-inversion) — inv vs pinv
- [Eigenvalue](matlab-eigenvalue) — matrix decomposition
- [Linear Solve](matlab-linear-solve) — more solve patterns
