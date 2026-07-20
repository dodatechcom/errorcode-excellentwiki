---
title: "[Solution] MATLAB integral/quadgk — Singularities, Tolerance, and Convergence"
description: "Fix MATLAB integral errors: singularity handling, tolerance settings, convergence failures, and array-valued integrands."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 124
---

## Common Causes

- Integrating over a singularity without specifying `'Waypoints'`
- Tolerance too tight causing timeout or max interval warnings
- Integrand returning NaN or Inf at evaluation points
- Using `integral` for oscillatory functions without options
- Array-valued integrand not returning correct shape

## How to Fix

```matlab
% WRONG: Integrating over a singularity
f = @(x) 1 ./ sqrt(x);  % Singularity at x=0
q = integral(f, 0, 1);   % May fail or warn

% CORRECT: Use singular endpoint handling
f = @(x) 1 ./ sqrt(x);
q = integral(f, 0, 1, 'Waypoints', [0.001]);  % Avoid singularity
% Or use singularity declaration:
q = integral(f, 0, 1, 'AbsTol', 1e-10, 'RelTol', 1e-10);
```

```matlab
% WRONG: Relaxed tolerance gives inaccurate result
f = @(x) exp(-x.^2);
q = integral(f, -10, 10, 'RelTol', 1e-1);

% CORRECT: Set appropriate tolerance
q = integral(f, -10, 10, 'RelTol', 1e-12, 'AbsTol', 1e-12);
```

```matlab
% CORRECT: Handle array-valued integrands
f = @(x) [sin(x), cos(x), exp(-x)];
q = integral(f, 0, pi, 'ArrayValued', true);
% Returns 1x3 vector of integrals
```

```matlab
% CORRECT: Oscillatory integral with substitution
f = @(x) sin(100*x) ./ (1 + x.^2);
% Direct integration may be slow:
q = integral(f, 0, 10, 'Waypoints', [0 1 2 3 4 5 6 7 8 9 10]);
```

```matlab
% CORRECT: Check convergence warning
[q, err] = integral(f, a, b, 'RelTol', 1e-8);
if err > 1e-6
    warning('Integration error estimate: %g', err);
end
```

## Examples

```matlab
% Example: Improper integral with singularity
f = @(x) log(x) ./ (1 + x);
% Singularity at x=0 from log(x)

% Method 1: Avoid exact singularity
q1 = integral(f, 1e-15, 1);

% Method 2: Split at singularity
q2 = integral(f, 1e-15, 0.5) + integral(f, 0.5, 1);

fprintf('Result: %.10f\n', q2);
```

## Related Errors

- [ODE45](matlab-ode45) — ODE integration
- [ODE15s](matlab-ode15s) — stiff ODE solvers
- [Linear Solve](matlab-linear-solve) — numerical methods
