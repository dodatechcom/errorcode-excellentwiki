---
title: "[Solution] MATLAB Matrix Inversion — pinv vs inv, Singular/Ill-conditioned Matrix"
description: "Fix MATLAB matrix inversion errors: pinv vs inv, singular matrix, ill-conditioned systems, and condition number warnings."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 120
---

## Common Causes

- `inv()` on a singular or nearly singular matrix
- Matrix with determinant very close to zero
- Not using `pinv` for rank-deficient systems
- Confusing `inv(A)*b` with `A\b` (numerical stability)
- Condition number exceeding machine precision

## How to Fix

```matlab
% WRONG: Using inv() on singular matrix
A = [1 2; 2 4];
B = inv(A);  % Warning: matrix is singular

% CORRECT: Use pinv for pseudo-inverse
A = [1 2; 2 4];
B = pinv(A);  % Returns least-norm solution
```

```matlab
% WRONG: inv(A)*b for solving linear systems
x = inv(A) * b;  % Less accurate and slower

% CORRECT: Use backslash operator
x = A \ b;  % Uses LU/LDL factorization, more stable

% For least squares (rank deficient):
x = pinv(A) * b;  % Minimum norm solution
```

```matlab
% CORRECT: Check condition number before inversion
A = [1 2 3; 4 5 6; 7 8 10];
condNum = cond(A);
fprintf('Condition number: %g\n', condNum);

if condNum > 1/eps(class(A))
    warning('Matrix is nearly singular (cond = %g)', condNum);
end
```

```matlab
% CORRECT: Use decomposition for repeated solves
A = rand(100);
[L, U, P] = lu(A);

% Solve multiple systems efficiently
b1 = rand(100, 1);
b2 = rand(100, 1);
x1 = U \ (L \ (P * b1));
x2 = U \ (L \ (P * b2));
```

```matlab
% CORRECT: Diagnose and handle singular systems
function x = safeSolve(A, b)
    [m, n] = size(A);
    rankA = rank(A);

    if rankA < min(m, n)
        warning('Matrix rank deficient (rank = %d)', rankA);
        x = pinv(A) * b;  % Least squares solution
    else
        condNum = cond(A);
        if condNum > 1e12
            warning('Ill-conditioned matrix (cond = %g)', condNum);
        end
        x = A \ b;
    end
end
```

## Examples

```matlab
% Example: Compare inv vs pinv vs backslash
A = [1 2 3; 4 5 6; 7 8 9];  % Rank 2 matrix
b = [1; 2; 3];

x_inv = pinv(A) * b;        % Pseudo-inverse
x_slash = A \ b;            % Backslash (rank deficient warning)
x_lsq = lsqminnorm(A, b);   % Minimum norm (R2017b+)

fprintf('pinv norm: %.6f\n', norm(A*x_inv - b));
fprintf('lsqminnorm norm: %.6f\n', norm(A*x_lsq - b));
```

## Related Errors

- [Linear Solve](matlab-linear-solve) — mldivide issues
- [Eigenvalue](matlab-eigenvalue) — matrix decomposition
- [Dimension Mismatch](matlab-dimension-mismatch-v2) — size errors
