---
title: "[Solution] MATLAB Robust Control Error — muAnalysis, robstab & robgain"
description: "Fix MATLAB Robust Control Toolbox errors for mu analysis, robust stability, robust gain, and uncertainty modeling with code examples."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 142
---

MATLAB's Robust Control Toolbox functions (`muAnalysis`, `robstab`, `robgain`) can fail when uncertainty objects are not properly connected, the system is ill-conditioned, or the structured singular value computation does not converge.

## Common Causes

- Uncertainty blocks have overlapping or conflicting ranges
- The system plant has more uncertainty than the analysis can handle
- `robstab` is called on a system without proper `uss` or `ufrd` model
- Frequency grid is too coarse for the analysis
- `robgain` target gain is physically unrealistic

## How to Fix

### Solution 1: Create uncertain system

```matlab
K = tf([2], [1 1]);
Gnom = tf([1], [1 2 1]);
dG = ureal('dG', 0, 'Percentage', 20);
G = Gnom * (1 + dG);
T = feedback(K*G, 1);
```

### Solution 2: Robust stability analysis

```matlab
[Gm, info] = robstab(T);
fprintf('Robust stability margin: %.4f\n', Gm);
if Gm < 1
    warning('System is NOT robustly stable.');
end
```

### Solution 3: Robust gain analysis

```matlab
[maxGain, info] = robgain(T, 1);
fprintf('Max gain: %.4f\n', maxGain);
```

### Solution 4: Structured singular value (mu)

```matlab
sigma = muAnalysis(T);
disp(sigma);
plot(sigma);
title('Structured Singular Value');
```

### Solution 5: Connect uncertain blocks properly

```matlab
p = ureal('p', 1, 'Percentage', 10);
q = ureal('q', 0, 'Percentage', 15);
G = tf([p], [1 q 1]);
```

## Examples

Worst-case analysis of a feedback system:

```matlab
G = tf([1], [1 2 1]);
K = 5;
Gunc = G * (1 + ureal('dG', 0, 'Percentage', 30));
T = feedback(K*Gunc, 1);
[margin, info] = robstab(T);
fprintf('Worst-case destabilizing perturbation:\n');
disp(info);
```

## Related Errors

- [MATLAB Control Design Error](matlab-control-design) — nominal control design
- [MATLAB Model Predictive Control Error](matlab-model-predictive) — MPC design
- [MATLAB System Identification Error](matlab-system-identification) — system modeling
