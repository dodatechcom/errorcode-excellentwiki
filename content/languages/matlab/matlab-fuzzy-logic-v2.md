---
title: "[Solution] MATLAB Fuzzy Logic Error — Inference, Membership & Defuzzification"
description: "Fix MATLAB Fuzzy Logic Toolbox errors for fuzzy inference systems, membership function configuration, and defuzzification issues."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 145
---

MATLAB's Fuzzy Logic Toolbox (`fuzzy`, `mamfis`, `evalfis`, `trapmf`) can fail when membership function ranges overlap incorrectly, rule bases reference undefined variables, or defuzzification methods are incompatible with the output type.

## Common Causes

- Membership function range exceeds the variable's defined range
- Rule base references input/output variables not in the FIS
- `evalfis` receives input vectors with wrong number of columns
- Defuzzification method `'wtaver'` is used with non-singleton output
- Too many or too few rules for the number of input variables

## How to Fix

### Solution 1: Create a Mamdani FIS

```matlab
fis = mamfis('Name', 'tipper');
fis = addInput(fis, [0 10], 'Name', 'service');
fis = addInput(fis, [0 10], 'Name', 'food');
fis = addOutput(fis, [0 30], 'Name', 'tip');
fis = addMF(fis, 'service', 'trimf', [0 0 5], 'Name', 'bad');
fis = addMF(fis, 'service', 'trimf', [0 5 10], 'Name', 'good');
fis = addMF(fis, 'service', 'trimf', [5 10 10], 'Name', 'excellent');
fis = addMF(fis, 'food', 'trimf', [0 0 5], 'Name', 'rancid');
fis = addMF(fis, 'food', 'trimf', [5 10 10], 'Name', 'delicious');
fis = addMF(fis, 'tip', 'trimf', [0 5 10], 'Name', 'low');
fis = addMF(fis, 'tip', 'trimf', [5 15 25], 'Name', 'medium');
fis = addMF(fis, 'tip', 'trimf', [15 25 30], 'Name', 'high');
```

### Solution 2: Add rules

```matlab
ruleList = [
    1 1 1 1 1;  % IF service=bad AND food=rancid THEN tip=low
    2 2 2 1 1;  % IF service=good AND food=delicious THEN tip=medium
    3 2 3 1 1;  % IF service=excellent AND food=delicious THEN tip=high
];
fis = addRule(fis, ruleList);
```

### Solution 3: Evaluate the FIS

```matlab
result = evalfis(fis, [7 8]);
fprintf('Tip: $%.2f\n', result);
```

### Solution 4: Trapezoidal membership function

```matlab
x = 0:0.1:10;
y = trapmf(x, [2 3 5 7]);
plot(x, y);
xlabel('x'); ylabel('Membership');
title('Trapezoidal MF');
```

### Solution 5: Sugeno FIS

```matlab
fis = sugfis('Name', 'sugeno_demo');
fis = addInput(fis, [-10 10], 'Name', 'x');
fis = addOutput(fis, [-10 10], 'Name', 'y');
fis = addMF(fis, 'x', 'gaussmf', [2 -5], 'Name', 'neg');
fis = addMF(fis, 'x', 'gaussmf', [2 5], 'Name', 'pos');
fis = addMF(fis, 'y', 'constant', -5, 'Name', 'neg_out');
fis = addMF(fis, 'y', 'constant', 5, 'Name', 'pos_out');
fis = addRule(fis, [1 1 1 1; 2 2 1 1]);
result = evalfis(fis, 3);
```

## Examples

Fuzzy temperature controller:

```matlab
fis = mamfis('Name', 'temp_controller');
fis = addInput(fis, [15 35], 'Name', 'temperature');
fis = addInput(fis, [-5 5], 'Name', 'rate');
fis = addOutput(fis, [-10 10], 'Name', 'adjustment');
fis = addMF(fis, 'temperature', 'trimf', [15 15 25], 'Name', 'cold');
fis = addMF(fis, 'temperature', 'trimf', [20 25 30], 'Name', 'comfortable');
fis = addMF(fis, 'temperature', 'trimf', [25 35 35], 'Name', 'hot');
fis = addMF(fis, 'rate', 'trimf', [-5 -5 0], 'Name', 'decreasing');
fis = addMF(fis, 'rate', 'trimf', [0 0 5], 'Name', 'increasing');
fis = addMF(fis, 'adjustment', 'trimf', [-10 -10 0], 'Name', 'cool');
fis = addMF(fis, 'adjustment', 'trimf', [0 10 10], 'Name', 'heat');
fis = addRule(fis, [1 1 1 1 1; 1 2 1 1 1; 3 2 2 1 1; 3 1 2 1 1]);
out = evalfis(fis, [30 -1]);
fprintf('Adjustment: %.2f\n', out);
```

## Related Errors

- [MATLAB Control Design Error](matlab-control-design) — classical control
- [MATLAB Machine Learning Error](matlab-machine-learning) — data-driven modeling
- [MATLAB Model Predictive Control Error](matlab-model-predictive) — advanced control
