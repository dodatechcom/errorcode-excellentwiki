---
title: "[Solution] MATLAB Quadratic Programming (quadprog) Error — Hessian & Equality Constraints"
description: "Fix MATLAB quadprog errors for Hessian matrix issues, equality constraint infeasibility, and solver convergence problems."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 117
---

MATLAB's `quadprog` solves quadratic programming problems of the form min 0.5*x'*H*x + f'*x. Errors occur when the Hessian is not positive definite, constraints are contradictory, or the problem is poorly scaled.

## Common Causes

- Hessian `H` is not positive semidefinite (solver requires it for convex QP)
- Equality constraints `Aeq*x = beq` are inconsistent
- Problem is poorly scaled (coefficients differ by many orders of magnitude)
- Number of constraints exceeds the number of variables
- `H` dimensions do not match `f` length

## How to Fix

### Solution 1: Basic quadratic programming

```matlab
H = [2 1; 1 3];
f = [-4; -6];
A = [1 1; 1 -1];
b = [5; 3];
lb = [0; 0];
[x, fval] = quadprog(H, f, A, b, [], [], lb);
fprintf('Solution: [%.4f, %.4f]\n', x(1), x(2));
```

### Solution 2: With equality constraints

```matlab
H = [2 0; 0 4];
f = [-6; -8];
Aeq = [1 1];
beq = 5;
lb = [0; 0];
[x, fval] = quadprog(H, f, [], [], Aeq, beq, lb);
```

### Solution 3: Verify Hessian is positive definite

```matlab
H = [2 1; 1 1];
eigenvalues = eig(H);
if any(eigenvalues < -1e-10)
    warning('Hessian is not positive definite.');
    H = H + abs(min(eigenvalues)) * eye(size(H));
    disp('Hessian shifted to be positive definite.');
end
[x, fval] = quadprog(H, f, A, b);
```

### Solution 4: Scale the problem

```matlab
H = [1e6 0; 0 1e-6];
f = [1e3; 1e-3];
% Scale
scale = sqrt(diag(H));
Hs = H ./ (scale * scale');
fs = f ./ scale;
[xs, ~] = quadprog(Hs, fs, A, b, [], [], lb./scale, ub./scale);
x = xs .* scale;
```

### Solution 5: Display solver output

```matlab
options = optimoptions('quadprog', 'Display', 'iter', 'Algorithm', 'interior-point-convex');
[x, fval, exitflag, output] = quadprog(H, f, A, b, [], [], lb, ub, [], options);
disp(output);
```

## Examples

Markowitz portfolio optimization:

```matlab
Sigma = [0.04 0.006; 0.006 0.09];  % Covariance matrix
mu = [0.12; 0.08];                  % Expected returns
targetReturn = 0.10;

H = Sigma;
f = zeros(2, 1);
Aeq = mu';
beq = targetReturn;
lb = [0; 0];
ub = [1; 1];

[x, fval] = quadprog(H, f, [], [], Aeq, beq, lb, ub);
fprintf('Portfolio weights: [%.2f, %.2f]\n', x(1), x(2));
fprintf('Portfolio risk (variance): %.6f\n', fval);
```

## Related Errors

- [MATLAB Optimization fmincon/fminunc Error](matlab-optimization-v2) — nonlinear optimization
- [MATLAB Integer Programming Error](matlab-integer-programming) — mixed-integer problems
- [MATLAB Nonlinear Least Squares Error](matlab-nonlinear-least-squares) — residual-based fitting
