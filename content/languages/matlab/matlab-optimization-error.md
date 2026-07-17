---
title: "[Solution] Optimization: convergence failure in MATLAB"
description: "Fix MATLAB optimization errors when solvers fail to converge, reach iteration limits, or produce invalid solutions."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Optimization errors occur when MATLAB's optimization solvers cannot find a solution that satisfies convergence criteria within the allowed iterations or function evaluations.

## Common Causes

- Initial guess too far from solution
- Objective function not smooth
- Constraints infeasible
- Iteration limit reached
- Step size too small
- Numerical gradient issues

## How to Fix

```matlab
% WRONG: Bad initial guess
x0 = 1000;  % Far from solution
[x, fval] = fminsearch(@(x) (x-1)^2, x0);  % May not converge

% CORRECT: Better initial guess
x0 = 0.5;  % Close to expected solution
[x, fval] = fminsearch(@(x) (x-1)^2, x0);
```

```matlab
% WRONG: Default options
[x, fval] = fmincon(@(x) x^2, 1, [], [], [], [], 0, 10);

% CORRECT: Set options for better convergence
options = optimoptions('fmincon', ...
    'Display', 'iter', ...
    'MaxIterations', 1000, ...
    'MaxFunctionEvaluations', 5000, ...
    'OptimalityTolerance', 1e-8);
[x, fval] = fmincon(@(x) x^2, 1, [], [], [], [], 0, 10, [], options);
```

```matlab
% CORRECT: Check convergence
[x, fval, exitflag, output] = fminsearch(@(x) (x-1)^2, 0);
if exitflag <= 0
    warning('Optimization did not converge');
    disp(output.message);
end
```

```matlab
% CORRECT: Use multiple starting points
bestX = [];
bestFval = Inf;
for x0 = -10:2:10
    [x, fval] = fminsearch(@(x) (x-1)^2, x0);
    if fval < bestFval
        bestFval = fval;
        bestX = x;
    end
end
```

## Related Errors

- [ODE Solver Error](matlab-ode-solver-error) - ODE issues
- [Assertion Failed](matlab-assertion-failed-v2) - validation
- [Invalid Function Handle](matlab-invalid-function-handle-v2) - function issues
