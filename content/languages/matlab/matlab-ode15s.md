---
title: "[Solution] MATLAB ode15s/ode23s — Stiffness, Mass Matrix, Sparse Jacobian"
description: "Fix MATLAB stiff ODE solver errors: ode15s/ode23s configuration, mass matrices, Jacobian specification, and convergence."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 126
---

## Common Causes

- Not specifying Jacobian for large systems (auto-detection is slow)
- Mass matrix is not constant when declared as such
- Stiff system with discontinuities at wrong time points
- Using ode23s when ode15s would be more efficient
- Missing `Jacobian` option causing repeated numerical differentiation

## How to Fix

```matlab
% WRONG: Using ode45 on stiff system (missing Jacobian)
[t, y] = ode45(@stiffRHS, tspan, y0);  % Thousands of failed steps

% CORRECT: Use ode15s with analytical Jacobian
opts = odeset('Jacobian', @stiffJacobian);
[t, y] = ode15s(@stiffRHS, tspan, y0, opts);
```

```matlab
% CORRECT: Provide sparse Jacobian for large systems
function J = stiffJacobian(t, y)
    n = numel(y);
    J = spalloc(n, n, 5*n);
    % Build sparse Jacobian efficiently
    for k = 1:n
        J(k, k) = -2;
        if k > 1, J(k, k-1) = 1; end
        if k < n, J(k, k+1) = 1; end
    end
end

opts = odeset('Jacobian', @stiffJacobian, 'Vectorized', 'on');
[t, y] = ode15s(@stiffRHS, tspan, y0, opts);
```

```matlab
% CORRECT: Time-varying mass matrix
M = @(t, y) [1 0; 0 sin(t)+1];  % Time-varying
opts = odeset('Mass', M, 'MStateDependence', 'weak');
[t, y] = ode15s(@rhs, tspan, y0, opts);
```

```matlab
% CORRECT: Event detection in stiff systems
function [value, isterminal, direction] = stiffEvents(t, y)
    value = y(1) - threshold;
    isterminal = 1;
    direction = -1;
end

opts = odeset('Events', @stiffEvents, ...
              'Jacobian', @stiffJacobian, ...
              'RelTol', 1e-8, 'AbsTol', 1e-10);
[t, y, te, ye] = ode15s(@stiffRHS, tspan, y0, opts);
```

```matlab
% CORRECT: Choose between ode15s and ode23s
% ode15s: multi-step, variable order (1-5), good for general stiff
% ode23s: Rosenbrock, fixed order (2-3), good for discontinuous problems

% Discontinuous RHS → ode23s
opts = odeset('Jacobian', @sparseJac);
[t, y] = ode23s(@discontinuousRHS, tspan, y0, opts);

% Smooth RHS → ode15s
[t, y] = ode15s(@smoothRHS, tspan, y0, opts);
```

## Examples

```matlab
% Example: Robertson chemical kinetics (classic stiff test)
function dydt = robertson(t, y)
    dydt = [-0.04*y(1) + 1e4*y(2)*y(3);
             0.04*y(1) - 1e4*y(2)*y(3) - 3e7*y(2)^2;
             3e7*y(2)^2];
end

function J = robertsonJac(t, y)
    J = [-0.04,           1e4*y(3),        1e4*y(2);
          0.04, -1e4*y(3)-6e7*y(2),       -1e4*y(2);
          0,     6e7*y(2),                 0];
end

opts = odeset('Jacobian', @robertsonJac, 'RelTol', 1e-8);
[t, y] = ode15s(@robertson, [0 1e6], [1; 0; 0], opts);
```

## Related Errors

- [ODE45](matlab-ode45) — non-stiff solver
- [ODE Solver Error](matlab-ode-solver-error) — general ODE issues
- [Integral](matlab-integral) — numerical integration
