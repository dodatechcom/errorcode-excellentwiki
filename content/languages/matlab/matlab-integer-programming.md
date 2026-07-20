---
title: "[Solution] MATLAB Integer Programming (intlinprog) Error — Constraints & Bounds"
description: "Fix MATLAB intlinprog errors for integer constraints, bound violations, infeasibility, and solver convergence issues."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 116
---

MATLAB's `intlinprog` solves mixed-integer linear programming problems. Errors occur when integer variables are not properly declared, constraints are infeasible, or the problem formulation is numerically unstable.

## Common Causes

- `intcon` indices exceed the number of decision variables
- Linear constraints `A*x <= b` are contradictory (infeasible)
- Objective function coefficients are extremely large or small
- Bounds `lb` or `ub` are missing or incorrectly dimensioned
- Problem has no integer-feasible solution within tolerance

## How to Fix

### Solution 1: Basic integer programming

```matlab
f = [-2; -3; -1];
intcon = [1, 2, 3];
A = [1 1 1; 4 2 1; 2 5 3];
b = [6; 8; 10];
lb = [0; 0; 0];
ub = [Inf; Inf; Inf];
[x, fval, exitflag] = intlinprog(f, intcon, A, b, [], [], lb, ub);
fprintf('Solution: [%.0f, %.0f, %.0f], f = %.0f\n', x(1), x(2), x(3), fval);
```

### Solution 2: Equality constraints

```matlab
f = [3; 1; 3];
intcon = [1, 2, 3];
Aeq = [1 1 1];
beq = 4;
lb = [0; 0; 0];
[x, fval] = intlinprog(f, intcon, [], [], Aeq, beq, lb);
```

### Solution 3: Mixed-integer with binary variables

```matlab
f = [-1; -2; -3; 1];
intcon = [1, 2, 3, 4];
A = [2 1 -1 3; 1 3 2 -1];
b = [10; 12];
lb = [0; 0; 0; 0];
ub = [1; 1; 1; 1];  % Binary variables
[x, fval] = intlinprog(f, intcon, A, b, [], [], lb, ub);
```

### Solution 4: Display progress

```matlab
options = optimoptions('intlinprog', 'Display', 'off');
[x, fval, exitflag, output] = intlinprog(f, intcon, A, b, [], [], lb, ub, options);
disp(output);
```

### Solution 5: Infeasibility diagnosis

```matlab
try
    [x, fval, exitflag] = intlinprog(f, intcon, A, b, [], [], lb, ub);
    if exitflag == -2
        fprintf('Problem is infeasible.\n');
    elseif exitflag == -1
        fprintf('Solver stopped prematurely.\n');
    end
catch ME
    fprintf('Error: %s\n', ME.message);
end
```

## Examples

Knapsack problem:

```matlab
weights = [2; 3; 4; 5];
values = [3; 4; 5; 6];
maxWeight = 8;
n = length(values);
f = -values;  % Maximize profit = minimize negative profit
intcon = 1:n;
A = weights';
b = maxWeight;
lb = zeros(n, 1);
ub = ones(n, 1);
[x, fval] = intlinprog(f, intcon, A, b, [], [], lb, ub);
fprintf('Items selected: %s, Total value: %.0f\n', mat2str(x > 0.5), -fval);
```

## Related Errors

- [MATLAB Quadratic Programming Error](matlab-quadratic-programming) — QP problems
- [MATLAB Optimization fmincon/fminunc Error](matlab-optimization-v2) — continuous optimization
- [MATLAB Global Optimization Error](matlab-global-optimization) — global search methods
