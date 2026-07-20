---
title: "[Solution] MATLAB fsolve Error — Algorithm, Jacobian & Initial Guess"
description: "Fix MATLAB fsolve errors for algorithm selection, Jacobian specification, and poor initial guess convergence with code examples."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 115
---

MATLAB's `fsolve` finds roots of nonlinear systems of equations. Errors occur when the initial guess is far from any solution, the Jacobian is singular at the solution, or the algorithm fails to converge within the iteration limit.

## Common Causes

- Initial guess is far from any root, causing divergence
- Jacobian becomes singular or ill-conditioned during iteration
- Equation system is underdetermined or overdetermined
- Function evaluation returns `NaN` or `Inf`
- Maximum function evaluations or iterations exceeded

## How to Fix

### Solution 1: Solve a simple system

```matlab
fun = @(x) [x(1)^2 + x(2)^2 - 4; x(1) - x(2) - 1];
x0 = [1; 0];
[x, fval, exitflag] = fsolve(fun, x0);
fprintf('Solution: [%.4f, %.4f]\n', x(1), x(2));
```

### Solution 2: Supply Jacobian for accuracy

```matlab
fun = @(x) [x(1)^2 + x(2)^2 - 4; x(1) - x(2) - 1];
jac = @(x) [2*x(1), 2*x(2); 1, -1];
options = optimoptions('fsolve', 'SpecifyObjectiveGradient', true, 'Display', 'iter');
[x, fval] = fsolve(fun, [1; 0], options);
```

### Solution 3: Try multiple initial guesses

```matlab
fun = @(x) [x(1)^2 - 2; x(2)^2 - 3];
bestX = []; bestRes = Inf;
for i = 1:10
    x0 = randn(2, 1);
    [x, fval] = fsolve(fun, x0);
    res = norm(fval);
    if res < bestRes
        bestRes = res;
        bestX = x;
    end
end
fprintf('Best solution: [%.4f, %.4f], residual: %.2e\n', bestX(1), bestX(2), bestRes);
```

### Solution 4: Handle singular Jacobian

```matlab
fun = @(x) [x(1)^2 - 1; x(2)^2 - 1];
x0 = [0.1; 0.1];
options = optimoptions('fsolve', 'Algorithm', 'levenberg-marquardt');
[x, fval, exitflag] = fsolve(fun, x0, options);
if exitflag <= 0
    warning('fsolve did not converge. Try a different initial guess.');
end
```

### Solution 5: Set tolerances for precision

```matlab
options = optimoptions('fsolve', ...
    'FunctionTolerance', 1e-12, ...
    'StepTolerance', 1e-12, ...
    'MaxFunctionEvaluations', 5000);
[x, fval] = fsolve(fun, x0, options);
```

## Examples

Solve a 3-variable system:

```matlab
fun = @(x) [x(1) + x(2) + x(3) - 6; ...
            x(1)*x(2) + x(2)*x(3) + x(1)*x(3) - 11; ...
            x(1)*x(2)*x(3) - 6];
x0 = [1; 2; 3];
[x, fval, exitflag] = fsolve(fun, x0);
disp(x);
```

## Related Errors

- [MATLAB lsqcurvefit Error](matlab-lsqcurvefit) — nonlinear least-squares
- [MATLAB Optimization fmincon/fminunc Error](matlab-optimization-v2) — general optimization
- [MATLAB BVP Error](matlab-bvp-error) — boundary value problems
