---
title: "[Solution] MATLAB Optimization fmincon/fminunc Error — Constraint, Gradient & Hessian"
description: "Fix MATLAB fmincon and fminunc errors for constraint violations, gradient specification, Hessian issues, and convergence failures."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 111
---

MATLAB's `fmincon` and `fminunc` solve constrained and unconstrained nonlinear optimization problems. Errors arise when constraints are infeasible, gradients are incorrectly specified, or the Hessian is not positive definite.

## Common Causes

- Initial point violates nonlinear inequality or equality constraints
- Gradient function returns wrong dimensions or incorrect values
- Hessian is not positive semidefinite for `fmincon` with `'interior-point'` algorithm
- `lb` and `ub` bounds are inconsistent (lower > upper)
- Objective function returns `NaN` or `Inf` at the starting point

## How to Fix

### Solution 1: Basic unconstrained optimization with fminunc

```matlab
fun = @(x) (x(1)-1)^2 + (x(2)-2)^2;
x0 = [0, 0];
options = optimoptions('fminunc', 'Display', 'iter', 'Algorithm', 'quasi-newtown');
[x, fval, exitflag] = fminunc(fun, x0, options);
fprintf('Solution: [%.4f, %.4f], f = %.6f\n', x(1), x(2), fval);
```

### Solution 2: Constrained optimization with bounds

```matlab
fun = @(x) x(1)^2 + x(2)^2;
x0 = [3, 3];
lb = [0, 0];
ub = [5, 5];
A = [1 1]; b = 6;
options = optimoptions('fmincon', 'Display', 'final');
[x, fval] = fmincon(fun, x0, A, b, [], [], lb, ub, [], options);
```

### Solution 3: Supply analytical gradient

```matlab
fun = @(x) 100*(x(2)-x(1)^2)^2 + (1-x(1))^2;
grad = @(x) [-400*x(1)*(x(2)-x(1)^2)-2*(1-x(1)); 200*(x(2)-x(1)^2)];
x0 = [-1, 1];
options = optimoptions('fmincon', 'SpecifyObjectiveGradient', true);
[x, fval] = fmincon(fun, x0, [], [], [], [], [], [], [], options);
```

### Solution 4: Nonlinear constraint functions

```matlab
fun = @(x) x(1)^2 + x(2)^2;
nonlcon = @(x) deal(x(1)^2 + x(2)^2 - 1, []);  % x^2+y^2 <= 1
x0 = [0.5, 0.5];
options = optimoptions('fmincon', 'Algorithm', 'sqp');
[x, fval] = fmincon(fun, x0, [], [], [], [], [], [], nonlcon, options);
```

### Solution 5: Verify gradient with check gradients

```matlab
fun = @(x) x(1)^2 + 2*x(2)^2;
grad = @(x) [2*x(1); 4*x(2)];
x0 = [1, 1];
checkGradients(fun, x0, grad);
```

## Examples

Minimize a function with integer constraints:

```matlab
fun = @(x) (x(1)-3.7)^2 + (x(2)-5.2)^2;
x0 = [0, 0];
lb = [0, 0]; ub = [10, 10];
intcon = [1, 2];
[x, fval] = ga(fun, 2, [], [], [], [], lb, ub, [], intcon);
fprintf('Best integer point: [%.0f, %.0f], f = %.4f\n', x(1), x(2), fval);
```

## Related Errors

- [MATLAB Global Optimization Error](matlab-global-optimization) — local minima issues
- [MATLAB Quadratic Programming Error](matlab-quadratic-programming) — QP solver errors
- [MATLAB Nonlinear Least Squares Error](matlab-nonlinear-least-squares) — residual-based fitting
