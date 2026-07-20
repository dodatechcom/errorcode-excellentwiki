---
title: "[Solution] MATLAB BVP Error (bvp4c/bvp5c) — Boundary Conditions & Singular Jacobian"
description: "Fix MATLAB bvp4c and bvp5c errors for boundary condition specification, singular Jacobian, and mesh refinement failures."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 120
---

MATLAB's `bvp4c` and `bvp5c` solve two-point boundary value problems. Errors occur when boundary conditions are inconsistent, the initial mesh is too coarse, or the Jacobian becomes singular during the solver iterations.

## Common Causes

- Boundary condition function returns wrong number of conditions
- Initial guess `solinit` is too far from the true solution
- The BVP has a singular solution or is not well-posed
- `bvp4c` fails to converge and `bvp5c` should be used instead
- Mesh points are too closely spaced, causing numerical instability

## How to Fix

### Solution 1: Basic bvp4c usage

```matlab
solinit = bvpinit(linspace(0, 1, 20), [1 0]);
sol = bvp4c(@ode, @bc, solinit);

x = linspace(0, 1, 100);
y = deval(sol, x);
plot(x, y(1, :), 'b-', x, y(2, :), 'r--');
legend('y', 'dy/dx');

function dydx = ode(x, y)
    dydx = [y(2); -y(1)];
end

function res = bc(ya, yb)
    res = [ya(1); yb(1) - 1];
end
```

### Solution 2: Better initial guess with bvpinit

```matlab
solinit = bvpinit(linspace(0, pi, 30), [0 1]);
sol = bvp4c(@odefun, @bcfun, solinit);

function dydx = odefun(x, y)
    dydx = [y(2); -y(1)];
end

function res = bcfun(ya, yb)
    res = [ya(1); yb(1)];
end
```

### Solution 3: Switch to bvp5c for difficult problems

```matlab
solinit = bvpinit(linspace(0, 1, 10), [0 0]);
try
    sol = bvp4c(@ode, @bc, solinit);
catch
    sol = bvp5c(@ode, @bc, solinit);
    disp('Used bvp5c as fallback.');
end
```

### Solution 4: Use parameters in BVP

```matlab
solinit = bvpinit(linspace(0, 1, 20), [0 0], 1);
sol = bvp4c(@ode, @bc, solinit);
fprintf('Estimated parameter: %.4f\n', sol.parameters);

function dydx = ode(x, y, p)
    dydx = [y(2); -p^2 * y(1)];
end

function res = bc(ya, yb, p)
    res = [ya(1); yb(1) - 1];
end
```

### Solution 5: Verify mesh quality

```matlab
solinit = bvpinit(linspace(0, 1, 50), [1 0]);
sol = bvp4c(@ode, @bc, solinit, bvpset('RelTol', 1e-6));
meshInfo = sol.x;
fprintf('Mesh points: %d\n', length(meshInfo));
if length(meshInfo) < 20
    warning('Mesh may be too coarse. Consider more initial points.');
end
```

## Examples

Solve the Bratu equation:

```matlab
lambda = 1;
solinit = bvpinit(linspace(0, 1, 40), [0 0]);
sol = bvp4c(@(x,y) bratuODE(x, y, lambda), @bratuBC, solinit);
x = linspace(0, 1, 100);
y = deval(sol, x);
plot(x, y(1, :));
title(sprintf('Bratu Equation (lambda = %.1f)', lambda));

function dydx = bratuODE(x, y, lambda)
    dydx = [y(2); -lambda * exp(y(1))];
end

function res = bratuBC(ya, yb)
    res = [ya(1); yb(1)];
end
```

## Related Errors

- [MATLAB PDE Solver Error](matlab-pde-error) — PDE systems (pdepe)
- [MATLAB ODE Solver Error](matlab-ode-solver-error) — initial value ODEs
- [MATLAB fsolve Error](matlab-fsolve) — nonlinear equation solving
