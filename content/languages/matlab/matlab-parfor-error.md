---
title: "[Solution] MATLAB parfor — Transparency, Classification, and Sliced Variables"
description: "Fix MATLAB parfor errors: transparency rules, variable classification, sliced variables, and communication patterns."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 109
---

## Common Causes

- Variable doesn't meet `parfor` transparency requirements (sliced, broadcast, etc.)
- Using `break`, `continue`, or `return` inside `parfor`
- Dependent iteration where loop body depends on previous iteration results
- Writing to overlapping elements of the same output variable
- Mixing `spmd` and `parfor` in the same function

## How to Fix

```matlab
% WRONG: Dependent iteration — result of iteration k depends on k-1
for k = 2:length(data)
    data(k) = data(k) + data(k-1);  % Can't parallelize
end

% CORRECT: Separate into independent prefix sum or use parallel algorithm
function result = parallelPrefixSum(data)
    n = length(data);
    result = zeros(size(data));
    result(1) = data(1);
    parfor k = 2:n
        result(k) = data(k);  % Independent: just copy
    end
    result = cumsum(result);   % Serial prefix sum
end
```

```matlab
% WRONG: Writing to overlapping indices
parfor k = 1:10
    output(k) = compute(k);
    output(1) = 0;  % Conflict: multiple iterations write to index 1
end

% CORRECT: Each iteration writes to unique indices
parfor k = 1:10
    output(k) = compute(k);
end
```

```matlab
% WRONG: Non-sliced variable in parfor
parfor k = 1:100
    val = accumulator + k;  % 'accumulator' is not sliced
    accumulator = val;      % Dependency across iterations
end

% CORRECT: Use reduction variable pattern
total = 0;
parfor k = 1:100
    total = total + k;  % MATLAB classifies as reduction variable
end
```

```matlab
% CORRECT: Proper variable classification example
function [results, counts, total] = analyzeData(data)
    n = numel(data);
    results = zeros(n, 1);     % Sliced output
    counts = zeros(n, 1);      % Sliced output
    total = 0;                 % Reduction variable

    parfor k = 1:n
        [results(k), counts(k)] = processElement(data(k));
        total = total + results(k);  % Reduction
    end
end
```

```matlab
% CORRECT: Handle parfor with temporary variables
function output = parforWithTemp(data)
    n = numel(data);
    output = cell(1, n);

    parfor k = 1:n
        temp = transform(data{k});    % Temporary: local to each iteration
        output{k} = finalStep(temp);  % Sliced output
    end
end
```

## Examples

```matlab
% Example: Parfor with proper variable usage
function [means, stds] = parallelStats(data)
    n = size(data, 1);
    p = size(data, 2);
    means = zeros(n, 1);
    stds = zeros(n, 1);

    parfor k = 1:n
        row = data(k, :);            % Sliced input (row of data)
        means(k) = mean(row);        % Sliced output
        stds(k) = std(row);          % Sliced output
    end
end
```

## Related Errors

- [SPMD Error](matlab-spmd-error) — SPMD communication
- [Broadcast Error](matlab-broadcast-error) — variable size issues
- [Parallel Error](matlab-parallel-error) — general parallel toolbox
