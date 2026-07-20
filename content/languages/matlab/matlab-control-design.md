---
title: "[Solution] MATLAB Control Design Error — tf, ss, zpk, bode, nyquist & margin"
description: "Fix MATLAB Control System Toolbox errors for transfer functions, state-space, Bode plots, Nyquist, and stability margins."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 141
---

MATLAB's Control System Toolbox functions (`tf`, `ss`, `zpk`, `bode`, `nyquist`, `margin`) can fail when system matrices are singular, transfer function orders are inconsistent, or stability margin computation encounters a marginally stable system.

## Common Causes

- Transfer function numerator and denominator have inconsistent orders
- State-space matrices `A` is singular and `ss` conversion fails
- `bode` or `nyquist` frequency range includes a resonance peak that is infinite
- `margin` returns `Inf` gain or phase margin for unstable systems
- `zpk` encounters poles or zeros at infinity

## How to Fix

### Solution 1: Create and analyze transfer functions

```matlab
G = tf([1 2], [1 3 2]);
disp(G);
pzmap(G);
grid on;
```

### Solution 2: State-space representation

```matlab
A = [0 1; -2 -3];
B = [0; 1];
C = [1 0];
D = 0;
sys = ss(A, B, C, D);
step(sys);
title('Step Response');
```

### Solution 3: Bode plot with stability margins

```matlab
G = tf([1], [1 1 1]);
margin(G);
[Gm, Pm, Wcg, Wcp] = margin(G);
fprintf('Gain Margin: %.2f dB at %.2f rad/s\n', 20*log10(Gm), Wcg);
fprintf('Phase Margin: %.2f deg at %.2f rad/s\n', Pm, Wcp);
```

### Solution 4: Nyquist plot

```matlab
G = tf([1], [1 2 3 1]);
figure;
nyquist(G);
title('Nyquist Plot');
```

### Solution 5: ZPK format

```matlab
G = zpk([-1 -2], [-3 -4 -5], 1);
disp(G);
bode(G);
```

## Examples

Design and verify a PID controller:

```matlab
G = tf([1], [1 2 1]);
C = pidtune(G, 'PID');
T = feedback(C*G, 1);
stepinfo(T)
margin(C*G);
```

## Related Errors

- [MATLAB Robust Control Error](matlab-robust-control) — uncertainty modeling
- [MATLAB System Identification Error](matlab-system-identification) — model estimation
- [MATLAB Model Predictive Control Error](matlab-model-predictive) — MPC controller
