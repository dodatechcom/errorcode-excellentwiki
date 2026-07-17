---
title: "[Solution] ODE solver: step size too small in MATLAB"
description: "Fix MATLAB ODE solver errors when step size becomes too small, solver stalls, or integration fails."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

ODE solver errors occur when MATLAB's ordinary differential equation solvers (ode45, ode23, etc.) encounter singularities, stiff equations, or step sizes that become impractically small.

## Common Causes

- Stiff differential equations
- Singularity in solution
- Discontinuities in equations
- Step size too small for convergence
- Incorrect time span
- Event functions causing issues

## How to Fix

```matlab
% WRONG: Stiff equation with non-stiff solver
[t, y] = ode45(@(t,y) -1000*y, [0, 1], 1);  % May be slow

% CORRECT: Use stiff solver for stiff problems
[t, y] = ode15s(@(t,y) -1000*y, [0, 1], 1);
```

```matlab
% WRONG: Step size too small
[t, y] = ode45(@(t,y) y, [0, 1e-10], 1);  % May fail

% CORRECT: Adjust tolerances
options = odeset('RelTol', 1e-6, 'AbsTol', 1e-9);
[t, y] = ode45(@(t,y) y, [0, 1], 1, options);
```

```matlab
% CORRECT: Handle discontinuities
function dydt = myODE(t, y)
    if t < 0.5
        dydt = -y;
    else
        dydt = y;
    end
end

% Use events to detect discontinuity
function [value, isterminal, direction] = events(t, y)
    value = t - 0.5;
    isterminal = 1;
    direction = 0;
end

options = odeset('Events', @events);
[t, y, te, ye] = ode45(@myODE, [0, 2], 1, options);
```

```matlab
% CORRECT: Check solver output
[t, y] = ode45(@myODE, tspan, y0);
if length(t) < 10
    warning('Solver may have failed - few time points');
end

% Plot to verify solution
plot(t, y);
xlabel('Time');
ylabel('Solution');
```

## Related Errors

- [Optimization Error](matlab-optimization-error) - optimization issues
- [Assertion Failed](matlab-assertion-failed-v2) - validation errors
- [Dimension Mismatch](matlab-dimension-mismatch-v2) - dimension errors
