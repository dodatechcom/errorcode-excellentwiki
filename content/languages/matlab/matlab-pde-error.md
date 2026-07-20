---
title: "[Solution] MATLAB PDE Solver Error — pdepe Boundary, Mesh & Singular Solutions"
description: "Fix MATLAB PDE solver errors (pdepe, pdepe, solvepde) for boundary conditions, mesh resolution, and singular solution issues."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 119
---

MATLAB's PDE solvers (`pdepe` for 1D systems, `solvepde` for general FEM) can fail when boundary conditions are inconsistent, the mesh is too coarse or too fine, or the solution becomes singular.

## Common Causes

- Boundary conditions are inconsistent with initial conditions at the interface
- Mesh is too coarse, causing the solver to miss steep gradients
- Coefficient functions return `NaN` or `Inf` at certain spatial points
- The PDE has a singularity (e.g., division by zero at a boundary)
- `pdepe` receives an `m` value outside the valid range (0, 1, or 2)

## How to Fix

### Solution 1: Basic pdepe usage for heat equation

```matlab
m = 0;
x = linspace(0, 1, 50);
t = linspace(0, 0.5, 20);

sol = pdepe(m, @heatpde, @heatic, @heatbc, x, t);

function c = heatpde(x, t, u, Dudx)
    c = 1;
    f = Dudx;
    s = 0;
end

function u0 = heatic(x)
    u0 = sin(pi*x);
end

function [pl, ql, pr, qr] = heatbc(xl, ul, xr, ur, t)
    pl = ul;
    ql = 0;
    pr = ur - 1;
    qr = 0;
end
```

### Solution 2: Increase mesh resolution

```matlab
x = linspace(0, 1, 200);  % Finer mesh
t = linspace(0, 1, 100);
sol = pdepe(m, @pdefun, @icfun, @bcfun, x, t);
```

### Solution 3: Handle singularities in coefficient functions

```matlab
function c = pdefun(x, t, u, Dudx)
    if x == 0
        c = eps;  % Avoid division by zero
    else
        c = x;
    end
    f = x * Dudx;
    s = 0;
end
```

### Solution 4: Validate boundary condition consistency

```matlab
function [pl, ql, pr, qr] = bcfun(xl, ul, xr, ur, t)
    % Left BC: u = 0 (Dirichlet)
    pl = ul;
    ql = 0;
    % Right BC: du/dx = 0 (Neumann)
    pr = 0;
    qr = 1;
end
```

### Solution 5: Check solution for NaN or Inf

```matlab
sol = pdepe(m, @pdefun, @icfun, @bcfun, x, t);
if any(isnan(sol(:))) || any(isinf(sol(:)))
    warning('Solution contains NaN or Inf. Try refining the mesh.');
    x = linspace(0, 1, 200);
    sol = pdepe(m, @pdefun, @icfun, @bcfun, x, t);
end
surf(x, t, sol);
xlabel('x'); ylabel('t'); zlabel('u');
```

## Examples

Solve the wave equation with pdepe:

```matlab
m = 0;
x = linspace(0, 1, 100);
t = linspace(0, 0.5, 50);
sol = pdepe(m, @wavePDE, @waveIC, @waveBC, x, t);
figure;
surf(x, t, sol);
title('Wave Equation Solution');
xlabel('x'); ylabel('t'); zlabel('u');

function c = wavePDE(x, t, u, Dudx)
    c = 1;
    f = Dudx;
    s = 0;
end
function u0 = waveIC(x)
    u0 = sin(pi*x);
end
function [pl, ql, pr, qr] = waveBC(xl, ul, xr, ur, t)
    pl = 0; ql = 1; pr = 0; qr = 1;
end
```

## Related Errors

- [MATLAB BVP Error](matlab-bvp-error) — boundary value problems (bvp4c/bvp5c)
- [MATLAB ODE Solver Error](matlab-ode-solver-error) — ordinary differential equations
- [MATLAB Optimization fmincon/fminunc Error](matlab-optimization-v2) — numerical optimization
