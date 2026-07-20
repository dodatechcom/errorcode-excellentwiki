---
title: "[Solution] MATLAB Model Predictive Control (mpc) Error — Weights, Constraints & Tuning"
description: "Fix MATLAB Model Predictive Control (mpc) errors for weight configuration, constraint violations, and controller tuning issues."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 144
---

MATLAB's Model Predictive Control Toolbox (`mpc`, `mpcmove`, `mpcobject`) can fail when the prediction horizon is too short, constraints are contradictory, or the plant model is not proper (feedthrough).

## Common Causes

- Plant model has direct feedthrough (`D` matrix is nonzero)
- Prediction horizon is shorter than the control horizon
- Constraints are set tighter than the plant's physical limits
- Weight matrices are not positive semi-definite
- Sampling time of MPC does not match the plant model

## How to Fix

### Solution 1: Basic MPC setup

```matlab
plant = tf([1], [1 2 1]);
Ts = 0.1;
mpcObj = mpc(plant, Ts);
mpcObj.PredictionHorizon = 20;
mpcObj.ControlHorizon = 5;
mpcObj.Weights.OutputVariables = 1;
mpcObj.Weights.ManipulatedVariablesRate = 0.1;
```

### Solution 2: Set constraints

```matlab
mpcObj.MV.Min = 0;
mpcObj.MV.Max = 10;
mpcObj.MV.RateMin = -2;
mpcObj.MV.RateMax = 2;
mpcObj.OV(1).Min = -5;
mpcObj.OV(1).Max = 5;
```

### Solution 3: Simulate the closed loop

```matlab
plant = ss(tf(1, [1 2 1]));
Ts = 0.1;
mpcObj = mpc(plant, Ts);
mpcObj.PredictionHorizon = 20;
mpcObj.ControlHorizon = 5;
Tstop = 10;
r = ones(Tstop/Ts, 1);
[y, t, u] = sim(mpcObj, Tstop/Ts, r);
plot(t, y, t, u);
legend('Output', 'Control');
```

### Solution 4: Weight tuning

```matlab
mpcObj.Weights.OutputVariables = [1 0];  % First output only
mpcObj.Weights.ManipulatedVariables = [0.1];
mpcObj.Weights.ManipulatedVariablesRate = [0.01];
```

### Solution 5: Use `mpcmove` for real-time control

```matlab
mpcobj = mpc(plant, 0.1);
x = mpcstate(mpcobj);
mv = mpcmove(mpcobj, x, y, ref, mv_prev);
```

## Examples

MPC for a two-input two-output system:

```matlab
plant = ss([0 1; -2 -3], [0; 1], [1 0], 0);
Ts = 0.1;
mpcObj = mpc(plant, Ts);
mpcObj.PredictionHorizon = 30;
mpcObj.ControlHorizon = 5;
mpcObj.Weights.OutputVariables = [1 0.5];
mpcObj.MV(1).Min = -10; mpcObj.MV(1).Max = 10;
mpcObj.MV(2).Min = -5; mpcObj.MV(2).Max = 5;
```

## Related Errors

- [MATLAB Control Design Error](matlab-control-design) — classical control
- [MATLAB Robust Control Error](matlab-robust-control) — uncertainty handling
- [MATLAB Optimization fmincon/fminunc Error](matlab-optimization-v2) — optimization internals
