---
title: "[Solution] MATLAB struct — Field Access, Dynamic Names, rmfield/isfield"
description: "Fix MATLAB struct errors: field access failures, dynamic field names, rmfield/isfield usage, and struct array issues."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 110
---

## Common Causes

- Accessing a field that doesn't exist with dot notation
- Using `struct.field` instead of `struct.(dynamicName)` for runtime field names
- Confusing struct arrays with scalar structs
- `rmfield` on a struct array removing fields from all elements unexpectedly
- Forgetting to initialize struct fields before accessing them

## How to Fix

```matlab
% WRONG: Accessing nonexistent field
S = struct('name', 'Alice', 'age', 30);
department = S.department;  % Error: Reference to nonexistent field

% CORRECT: Check field exists before access
if isfield(S, 'department')
    department = S.department;
else
    department = 'Unknown';
end
```

```matlab
% WRONG: Dynamic field name with dot notation
fieldName = 'score';
value = S.fieldName;  % Error: no field named 'fieldName'

% CORRECT: Use dynamic field names with parentheses
fieldName = 'score';
value = S.(fieldName);
```

```matlab
% CORRECT: Safe dynamic field access with default
function val = safeGetField(S, fieldName, defaultVal)
    if isfield(S, fieldName)
        val = S.(fieldName);
    elseif nargin >= 3
        val = defaultVal;
    else
        error('Field "%s" not found in struct', fieldName);
    end
end
```

```matlab
% CORRECT: Struct array vs scalar struct
S(1) = struct('x', 1, 'y', 2);
S(2) = struct('x', 3, 'y', 4);

% S.x returns [1 3] — array of field values
% Use S(1).x to get scalar value

% Access all elements of a field
allX = [S.x];        % Concatenated: [1 3]
allX2 = {S.x};       % Cell array: {1, 3}
```

```matlab
% CORRECT: Use rmfield safely on struct arrays
S = struct('a', {1, 2, 3}, 'b', {4, 5, 6}, 'c', {7, 8, 9});
S_clean = rmfield(S, 'b');  % Removes 'b' from all elements

% Check fields
disp(fieldnames(S_clean));  % {'a'; 'c'}
```

```matlab
% CORRECT: Build struct incrementally
function S = buildConfig()
    S = struct();
    S.timeout = 30;
    S.retries = 3;
    if exist('customConfig', 'file')
        custom = load('customConfig.mat');
        S = mergeStructs(S, custom);
    end
end

function result = mergeStructs(base, overlay)
    result = base;
    fields = fieldnames(overlay);
    for k = 1:numel(fields)
        result.(fields{k}) = overlay.(fields{k});
    end
end
```

## Examples

```matlab
% Example: Iterating over struct fields dynamically
S = struct('temperature', 72, 'humidity', 45, 'pressure', 30.12);
fields = fieldnames(S);
for k = 1:numel(fields)
    fprintf('%s: %g\n', fields{k}, S.(fields{k}));
end
```

## Related Errors

- [Container Map](matlab-containers-map) — key-value alternative
- [Table Index](matlab-table-index) — tabular data access
- [Variable Not Found](matlab-variable-not-found) — undefined variables
