---
title: "[Solution] Control System Toolbox: unstable system error in MATLAB"
description: "Fix MATLAB Control System Toolbox errors when systems are unstable, poles are in right half-plane, or design fails."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Control System Toolbox errors occur when designing or analyzing systems that are unstable, have poles in the right half-plane, or when controller design specifications are incompatible.

## Common Causes

- System has unstable poles (positive real part)
- Controller design specs too aggressive
- Gain margin or phase margin issues
- Feedback loop sign incorrect
- Model order too high

## How to Fix

```matlab
% WRONG: Unstable system
sys = tf(1, [1 -2]);  % Pole at +2 (unstable)

% CORRECT: Check stability first
sys = tf(1, [1 -2]);
poles = pole(sys);
if any(real(poles) > 0)
    warning('System has unstable poles');
end
```

```matlab
% WRONG: Aggressive design specs
% Controller trying to make unstable system stable
G = tf(1, [1 1 1]);
C = pid(1000, 1000, 1000);  % Very high gains
T = feedback(C*G, 1);  % May be unstable

% CORRECT: Design stabilizing controller
G = tf(1, [1 1 1]);
C = pidtune(G, 'PID');
T = feedback(C*G, 1);

% Verify stability
if all(real(pole(T)) < 0)
    disp('Closed-loop is stable');
end
```

```matlab
% CORRECT: Analyze system
G = tf([1 2], [1 3 2]);
margin(G);  % Check gain and phase margins
pzmap(G);  % Plot poles and zeros
step(T);   % Check step response
```

```matlab
% CORRECT: Design robust controller
G = tf(1, [1 2 1]);
[C, info] = pidtune(G, 'PID');
disp(info);
T = feedback(C*G, 1);
step(T);
```

## Related Errors

- [ODE Solver Error](matlab-ode-solver-error) - dynamic systems
- [Optimization Error](matlab-optimization-error) - design optimization
- [Dimension Mismatch](matlab-dimension-mismatch-v2) - dimension errors
