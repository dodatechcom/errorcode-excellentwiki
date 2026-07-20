---
title: "[Solution] MATLAB Bayesian Optimization Error — Acquisition Function & Constraints"
description: "Fix MATLAB bayesopt errors for acquisition functions, objective evaluation, constraint handling, and surrogate model issues."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 127
---

MATLAB's `bayesopt` performs surrogate-based optimization using Gaussian processes. Errors occur when the objective function returns `NaN`, acquisition function settings are inappropriate, or variable ranges are invalid.

## Common Causes

- Objective function returns `NaN` or `Inf` for some parameter combinations
- Variable bounds are inverted (min > max)
- `IsObjectiveDeterministic` is set incorrectly for noisy functions
- `AcquisitionFunctionName` is incompatible with constraint settings
- Number of initial evaluations exceeds the total budget

## How to Fix

### Solution 1: Basic bayesopt

```matlab
fun = @(x) (x(1)-3)^2 + (x(2)+1)^2 + 0.1*randn;
vars = [
    optimizableVariable('x1', [-5, 5])
    optimizableVariable('x2', [-5, 5])];
results = bayesopt(fun, vars, 'MaxObjectiveEvaluations', 30);
disp(results);
```

### Solution 2: With constraints

```matlab
fun = @(x) x(1)^2 + x(2)^2;
constraint = @(x) deal(x(1) + x(2) - 3, []);  % x1+x2 <= 3
vars = [
    optimizableVariable('x1', [0, 5])
    optimizableVariable('x2', [0, 5])];
results = bayesopt(fun, vars, ...
    'Constraints', constraint, ...
    'MaxObjectiveEvaluations', 50);
```

### Solution 3: Specify acquisition function

```matlab
results = bayesopt(fun, vars, ...
    'AcquisitionFunctionName', 'expected-improvement-plus', ...
    'MaxObjectiveEvaluations', 40, ...
    'Verbose', 0);
```

### Solution 4: Parallel evaluation

```matlab
results = bayesopt(fun, vars, ...
    'MaxObjectiveEvaluations', 60, ...
    'IsObjectiveDeterministic', false, ...
    'NumWorkers', 4);
```

### Solution 5: Extract best parameters

```matlab
results = bayesopt(fun, vars, 'MaxObjectiveEvaluations', 30);
bestPoint = bestPoint(results);
fprintf('Best x1: %.4f, Best x2: %.4f\n', bestPoint.x1, bestPoint.x2);
```

## Examples

Optimize a hyperparameter with bayesopt:

```matlab
fun = @(x) crossValLoss(x.NumNeighbors, x.Kernel);
vars = [
    optimizableVariable('NumNeighbors', [1, 50], 'Type', 'integer')
    optimizableVariable('Kernel', {'euclidean', 'cityblock', 'cosine'})];
results = bayesopt(fun, vars, 'MaxObjectiveEvaluations', 20);
```

## Related Errors

- [MATLAB Gaussian Process Error](matlab-gaussian-process) — GP regression kernel issues
- [MATLAB Global Optimization Error](matlab-global-optimization) — global search methods
- [MATLAB Optimization fmincon/fminunc Error](matlab-optimization-v2) — continuous optimization
