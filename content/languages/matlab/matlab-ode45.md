---
title: "[Solution] MATLAB ode45 — Singular Jacobian, Stiff Solver, Events Function"
description: "Fix MATLAB ode45 errors: singular Jacobian, stiff system detection, Events function, and solver selection."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 125
---

## Common Causes

- Using ode45 on a stiff system (should use ode15s)
- Jacobian is singular or ill-conditioned at some time points
- Events function not returning proper [value, isterminal, direction]
- Step size becoming too small, causing integration to stall
- ODE function returning wrong-size output vector

## How to Fix

```matlab
% WRONG: Using ode45 for stiff system
function dydt = stiffODE(t, y)
    dydt = zeros(2,1);
    dydt(1) = -1000 * y(1) + y(2);
    dydt(2) = y(1) - y(2);
end
[t, y] = ode45(@stiffODE, [0 10], [1; 1]);  % Extremely slow

% CORRECT: Use stiff solver
opts = odeset('RelTol', 1e-6, 'AbsTol', 1e-9);
[t, y] = ode15s(@stiffODE, [0 10], [1; 1], opts);
```

```matlab
% WRONG: Events function with wrong output size
function [value, isterminal, direction] = eventsFcn(t, y)
    value = y(1);        % Must be scalar
    isterminal = 1;      % Must be scalar
    direction = 0;       % Must be scalar
end

% CORRECT: Ensure scalar outputs
function [value, isterminal, direction] = eventsFcn(t, y)
    value = y(1);        % When y(1) crosses zero
    isterminal = 1;      % Stop integration
    direction = -1;      % Only downward crossing
end

opts = odeset('Events', @eventsFcn);
[t, y, te, ye] = ode45(@odeFcn, [0 10], y0, opts);
```

```matlab
% CORRECT: Detect stiffness and switch solver
function [t, y] = adaptiveSolve(odeFcn, tspan, y0)
    % Try ode45 first
    opts = odeset('RelTol', 1e-6, 'Stats', 'on');
    [t45, y45] = ode45(odeFcn, tspan, y0, opts);

    % Check step sizes — small steps indicate stiffness
    if length(t45) > 10000
        fprintf('Many steps (%d), trying stiff solver...\n', length(t45));
        [t, y] = ode15s(odeFcn, tspan, y0, opts);
    else
        t = t45;
        y = y45;
    end
end
```

```matlab
% CORRECT: Mass matrix for DAE systems
function dydt = daeSystem(t, y)
    M = [1 0; 0 0];  % Singular mass matrix
    dydt = [y(2); y(1) - 1];  % Algebraic constraint: y(1) = 1
end

opts = odeset('Mass', @massFcn);
[t, y] = ode15s(@daeSystem, [0 10], [0.5; 1], opts);
```

```matlab
% CORRECT: Validate ODE function output
function dydt = safeODE(t, y)
    dydt = odeFunc(t, y);
    if ~isvector(dydt) || numel(dydt) ~= numel(y)
        error('ODE function must return vector of size %d, got %d', ...
            numel(y), numel(dydt));
    end
end
```

## Examples

```matlab
% Example: Van der Pol oscillator (mildly stiff for mu > 1)
mu = 100;
f = @(t, y) [y(2); mu*(1 - y(1)^2)*y(2) - y(1)];
opts = odeset('RelTol', 1e-6, 'AbsTol', 1e-9, 'MaxStep', 0.01);
[t, y] = ode15s(f, [0 300], [2; 0], opts);
plot(y(:,1), y(:,2)); xlabel('x'); ylabel('dx/dt');
```

## Related Errors

- [ODE15s](matlab-ode15s) — stiff solver details
- [ODE Solver Error](matlab-ode-solver-error) — general ODE issues
- [Integral](matlab-integral) — quadrature integration
