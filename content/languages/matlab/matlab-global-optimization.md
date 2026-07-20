---
title: "[Solution] MATLAB Global Optimization — GlobalSearch/MultiStart Local Minima"
description: "Fix MATLAB GlobalSearch and MultiStart errors for local minima convergence, objective function issues, and solver configuration."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 112
---

MATLAB's `GlobalSearch` and `MultiStart` run global optimization algorithms to avoid local minima. Errors occur when the objective function is not properly wrapped, the solver fails to converge on any run, or the search space is too constrained.

## Common Causes

- Objective function is not a function handle or returns non-numeric values
- Number of starting points is too low for the problem dimensionality
- Bounds are too tight, making the problem infeasible
- `GlobalSearch` runs exceed time limit before finding a solution
- Problem has no feasible region given the constraints

## How to Fix

### Solution 1: Basic MultiStart usage

```matlab
problem = createOptimProblem('fmincon', ...
    'objective', @(x) (x(1)-1)^2 + (x(2)-3)^2, ...
    'x0', [0, 0], ...
    'lb', [-5, -5], 'ub', [5, 5]);
ms = MultiStart('Display', 'iter');
[x, fval, exitflag, output] = run(ms, problem, 20);
```

### Solution 2: GlobalSearch with bounds

```matlab
problem = createOptimProblem('fmincon', ...
    'objective', @(x) rosenbrock(x), ...
    'x0', [0, 0], ...
    'lb', [-2, -2], 'ub', [2, 2]);
gs = GlobalSearch('Display', 'iter', 'NumTrialPoints', 200);
[x, fval, exitflag, output] = run(gs, problem);
```

### Solution 3: Use parallel computing

```matlab
parpool(4);
problem = createOptimProblem('fmincon', ...
    'objective', @(x) sum(x.^2), ...
    'x0', randn(1, 3), ...
    'lb', -5*ones(1,3), 'ub', 5*ones(1,3));
ms = MultiStart('UseParallel', true);
[x, fval] = run(ms, problem, 50);
```

### Solution 4: Custom start points

```matlab
xstarts = -2 + 4*rand(100, 2);  % 100 random points in [-2, 2]
problem = createOptimProblem('fmincon', ...
    'objective', @(x) (x(1)^2+x(2)^2-1)^2, ...
    'x0', [0, 0], ...
    'lb', [-3, -3], 'ub', [3, 3]);
ms = MultiStart;
[x, fval] = run(ms, problem, xstarts);
```

### Solution 5: Validate objective before running

```matlab
fun = @(x) (x(1)-2)^2 + (x(2)+1)^2;
x0_test = [0, 0];
try
    val = fun(x0_test);
    assert(isfinite(val), 'Objective returns non-finite value.');
catch ME
    error('Objective function error: %s', ME.message);
end
```

## Examples

Find global minimum of the Rastrigin function:

```matlab
rastrigin = @(x) 20 + x(1)^2 + x(2)^2 - 10*(cos(2*pi*x(1)) + cos(2*pi*x(2)));
problem = createOptimProblem('fmincon', ...
    'objective', rastrigin, ...
    'x0', [2, 2], ...
    'lb', [-5, -5], 'ub', [5, 5]);
gs = GlobalSearch('NumTrialPoints', 500);
[x, fval] = run(gs, problem);
fprintf('Global minimum at [%.4f, %.4f], f = %.4f\n', x(1), x(2), fval);
```

## Related Errors

- [MATLAB Optimization fmincon/fminunc Error](matlab-optimization-v2) — local optimization
- [MATLAB Integer Programming Error](matlab-integer-programming) — mixed-integer problems
- [MATLAB Bayesian Optimization Error](matlab-bayesian-optimization) — surrogate-based optimization
