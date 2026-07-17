---
title: "[Solution] Statistics: insufficient data points error in MATLAB"
description: "Fix MATLAB Statistics Toolbox errors when statistical functions receive too few data points or invalid inputs."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Statistics Toolbox errors occur when statistical functions receive insufficient data, invalid parameters, or data that doesn't meet distribution assumptions.

## Common Causes

- Sample size too small for analysis
- Data contains NaN or Inf values
- Parameters outside valid range
- Distribution assumptions violated
- Missing required arguments

## How to Fix

```matlab
% WRONG: Too few data points
data = [1, 2];
[m, s] = normfit(data);  % May warn about small sample

% CORRECT: Check sample size
data = randn(100, 1);
if length(data) < 30
    warning('Small sample size may affect results');
end
[m, s] = normfit(data);
```

```matlab
% WRONG: NaN in data
data = [1, 2, NaN, 4, 5];
m = mean(data);  % Returns NaN

% CORRECT: Remove NaN values
data = [1, 2, NaN, 4, 5];
m = mean(data, 'omitnan');  % Ignores NaN
```

```matlab
% CORRECT: Validate data before analysis
function [m, s] = safeStats(data)
    % Remove NaN and Inf
    data = data(isfinite(data));
    
    if length(data) < 2
        error('Need at least 2 data points');
    end
    
    m = mean(data);
    s = std(data);
end
```

```matlab
% CORRECT: Check distribution assumptions
data = randn(100, 1);
[h, p] = kstest((data - mean(data))/std(data));
if h == 0
    disp('Data appears normally distributed');
else
    disp('Data may not be normally distributed');
end
```

```matlab
% CORRECT: Robust statistics
data = [1, 2, 3, 4, 1000];  % Outlier
m_robust = median(data);  % Robust to outliers
```

## Related Errors

- [Financial Error](matlab-financial-error) - date issues
- [Table Error](matlab-table-error) - data format
- [Assertion Failed](matlab-assertion-failed-v2) - validation
