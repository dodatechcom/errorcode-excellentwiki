---
title: "[Solution] MATLAB eig/eigs — Eigenvalue Convergence, Complex Eigenvalues, Condition"
description: "Fix MATLAB eigenvalue errors: eig/eigs convergence failures, complex eigenvalue handling, and condition number issues."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 121
---

## Common Causes

- `eigs` not converging for ill-conditioned or non-normal matrices
- Requesting more eigenvalues than matrix dimension
- Using `eigs` for small matrices where `eig` is better
- Not handling complex eigenvalues from non-symmetric matrices
- `eigs` with sigma near eigenvalues causing near-singularity in shifted matrix

## How to Fix

```matlab
% WRONG: eigs on small matrix
A = rand(5);
[V, D] = eigs(A, 3);  % Works but unnecessary — use eig instead

% CORRECT: Use eig for small/medium matrices
A = rand(5);
[V, D] = eig(A);
```

```matlab
% WRONG: eigs not converging
A = gallery('poisson', 100);  % Singular matrix (all rows sum to 0)
[V, D] = eigs(A, 5);  % May not converge

% CORRECT: Shift matrix to avoid singularity
A_reg = A + 1e-6 * eye(size(A));
[V, D] = eigs(A_reg, 5);
```

```matlab
% CORRECT: Handle complex eigenvalues
A = [0 -1; 1 0];  % Pure rotation — eigenvalues are ±i
[V, D] = eig(A);

% Check if eigenvalues are complex
eigenvalues = diag(D);
if any(imag(eigenvalues) ~= 0)
    fprintf('Complex eigenvalues found: %s\n', ...
        mat2str(eigenvalues, 4));
end
```

```matlab
% CORRECT: eigs with targeted sigma for specific eigenvalues
A = rand(100);
[V, D] = eigs(A, 5, 'largestabs');       % 5 largest by magnitude
[V, D] = eigs(A, 5, 'smallestabs');      % 5 smallest by magnitude
[V, D] = eigs(A, 5, 'largestreal');      % 5 largest real part

% Near a specific value
[V, D] = eigs(A, 5, 1.0);  % 5 eigenvalues nearest to 1.0
```

```matlab
% CORRECT: Validate eigenvalue decomposition
function [V, D, residual] = verifiedEig(A)
    [V, D] = eig(A);
    residual = norm(A * V - V * D);
    if residual > 1e-10
        warning('Eigendecomposition residual: %g', residual);
    end
end
```

## Examples

```matlab
% Example: Compute matrix exponential via eigenvalues
A = [2 1; 1 3];
[V, D] = eig(A);
expA = V * diag(exp(diag(D))) / V;

% Verify: expm should match
expA_ref = expm(A);
fprintf('Approximation error: %g\n', norm(expA - expA_ref));
```

## Related Errors

- [Matrix Inversion](matlab-matrix-inversion) — singular matrices
- [Linear Solve](matlab-linear-solve) — Ax = b systems
- [FFT Error](matlab-fft-error) — eigenvalue-related signal processing
