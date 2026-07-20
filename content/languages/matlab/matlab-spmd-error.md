---
title: "[Solution] MATLAB SPMD — labSend/labReceive/labBarrier Communication Errors"
description: "Fix MATLAB SPMD communication errors: labSend, labReceive, labBarrier, and distributed variable issues."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 107
---

## Common Causes

- `labSend`/`labReceive` called with mismatched lab indices
- Missing `labBarrier` causing race conditions between labs
- Using SPMD with more labs than available parallel workers
- Sending data before receiver calls `labReceive`
- Accessing distributed variables outside `spmd` block

## How to Fix

```matlab
% WRONG: Mismatched send/receive lab indices
spmd
    if labindex == 1
        labSend(data, 2);       % Send to lab 2
    end
    if labindex == 3            % Bug: expecting from lab 1 on lab 3
        received = labReceive(1);
    end
end

% CORRECT: Match send/receive pairs
spmd
    if labindex == 1
        labSend(data, 2);
    end
    if labindex == 2
        received = labReceive(1);
    end
end
```

```matlab
% WRONG: Missing barrier causes race condition
spmd
    if labindex == 1
        result = compute(localData);
        labSend(result, 2);     % Might send before lab 2 is ready
    end
    if labindex == 2
        partial = compute(localData);
        incoming = labReceive(1);  % May arrive before send
        finalResult = partial + incoming;
    end
end

% CORRECT: Use labBarrier to synchronize
spmd
    if labindex == 1
        result = compute(localData);
        labSend(result, 2);
    end
    if labindex == 2
        partial = compute(localData);
        labBarrier;             % Wait for all labs to reach this point
        incoming = labReceive(1);
        finalResult = partial + incoming;
    end
end
```

```matlab
% CORRECT: Broadcast pattern using labSend/labReceive
spmd
    localResult = compute(localPart);
end

% Gather results using spmd collect
results = spmd;
    labSend(localResult, 1);    % All labs send to lab 1
end

% Lab 1 collects
spmd
    if labindex == 1
        gathered = zeros(nlabs, 1);
        for k = 2:nlabs
            gathered(k) = labReceive(k);
        end
    end
end
```

```matlab
% CORRECT: Use spmdIdx for dynamic lab identification
spmd
    idx = spmdIndex;            % Current lab index (1-based)
    n = spmdNumLabs;            % Total number of labs
    fprintf('Lab %d of %d\n', idx, n);

    % Ring communication: send to next lab, receive from previous
    nextLab = mod(idx, n) + 1;
    prevLab = mod(idx - 2, n) + 1;
    labSend(idx, nextLab);
    receivedFrom = labReceive(prevLab);
end
```

## Examples

```matlab
% Example: Parallel matrix multiplication with SPMD
function C = parallelMatMul(A, B)
    [m, k1] = size(A);
    [k2, n] = size(B);
    assert(k1 == k2, 'Inner dimensions must agree');

    C = zeros(m, n);
    spmd
        localA = A(:, spmdIndex:spmdNumLabs:k1);
        localC = localA * B(spmdIndex:spmdNumLabs:k2, :);
    end
    % Collect results
    for k = 1:numel(localC)
        cols = k:nlabs:n;
        C(:, cols) = localC{k};
    end
end
```

## Related Errors

- [Parallel Error](matlab-parallel-error) — general parallel issues
- [parfor Error](matlab-parfor-error) — parfor transparency rules
- [Broadcast Error](matlab-broadcast-error) — variable size issues
