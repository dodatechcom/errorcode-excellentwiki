---
title: "[Solution] MATLAB table join/merge — innerjoin/outerjoin Key Match Errors"
description: "Fix MATLAB table join errors: innerjoin, outerjoin, key matching, and duplicate key handling."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 112
---

## Common Causes

- Join key variable names don't match between tables
- Data type mismatch in join keys (string vs char, double vs uint)
- Duplicate keys producing unexpected row explosion
- Using `innerjoin` when rows with no match should be preserved
- Joining tables with duplicate column names (not in key)

## How to Fix

```matlab
% WRONG: Key variable name mismatch
T1 = table([1;2;3], {'A';'B';'C'}, 'VariableNames', {'ID','Val1'});
T2 = table([2;3;4], {'X';'Y';'Z'}, 'VariableNames', {'Identifier','Val2'});
result = innerjoin(T1, T2, 'Keys', 'ID');  % Error: 'ID' not in T2

% CORRECT: Use matching key names or specify 'LeftKeys'/'RightKeys'
result = innerjoin(T1, T2, 'LeftKeys', 'ID', 'RightKeys', 'Identifier');
```

```matlab
% WRONG: Data type mismatch in keys
T1 = table([1;2;3]', 'VariableNames', {'ID'});    % double
T2 = table({'1';'2';'3'}, 'VariableNames', {'ID'}); % char
result = innerjoin(T1, T2, 'Keys', 'ID');  % Type mismatch, no matches

% CORRECT: Ensure key types match
T2.ID = str2double(T2.ID);  % Convert to double
result = innerjoin(T1, T2, 'Keys', 'ID');
```

```matlab
% CORRECT: Duplicate keys cause row explosion
T1 = table([1;1;2], {'A';'B';'C'}, 'VariableNames', {'ID','Name'});
T2 = table([1;1;3], [10;20;30], 'VariableNames', {'ID','Score'});
result = innerjoin(T1, T2, 'Keys', 'ID');
% ID=1 produces 4 rows (2x2 cross product)

% CORRECT: Deduplicate before joining
T2_dedup = T2(1, :);  % Keep first occurrence
result = innerjoin(T1, T2_dedup, 'Keys', 'ID');
```

```matlab
% CORRECT: outerjoin preserves unmatched rows
T1 = table([1;2;3], {'A';'B';'C'}, 'VariableNames', {'ID','Name'});
T2 = table([2;3;4], [20;30;40], 'VariableNames', {'ID','Score'});

% innerjoin: only IDs 2,3
inner = innerjoin(T1, T2, 'Keys', 'ID');

% outerjoin: IDs 1,2,3,4 with NaN for missing
outer = outerjoin(T1, T2, 'Keys', 'ID', 'MergeKeys', true);
```

```matlab
% CORRECT: Join multiple keys
T1 = table([1;1;2;2], [2023;2024;2023;2024], rand(4,1), ...
    'VariableNames', {'ID','Year','Value'});
T2 = table([1;1;2;2], [2023;2024;2023;2024], rand(4,1), ...
    'VariableNames', {'ID','Year','Other'});

result = innerjoin(T1, T2, 'Keys', {'ID','Year'});
```

## Examples

```matlab
% Example: Full join pipeline with validation
function result = safeJoin(T1, T2, keyVars)
    for k = 1:numel(keyVars)
        assert(ismember(keyVars{k}, T1.Properties.VariableNames), ...
            'Key %s not in left table', keyVars{k});
        assert(ismember(keyVars{k}, T2.Properties.VariableNames), ...
            'Key %s not in right table', keyVars{k});
        assert(isequal(class(T1.(keyVars{k})), class(T2.(keyVars{k}))), ...
            'Key %s type mismatch: %s vs %s', ...
            keyVars{k}, class(T1.(keyVars{k})), class(T2.(keyVars{k})));
    end
    result = innerjoin(T1, T2, 'Keys', keyVars);
end
```

## Related Errors

- [Table Index](matlab-table-index) — table access patterns
- [Table Error](matlab-table-error) — variable name issues
- [Categorical](matlab-categorical) — categorical key values
