---
title: "[Solution] MATLAB table Indexing — Row/Column Access and Variable Names"
description: "Fix MATLAB table indexing errors: row/column access, variable names, dot notation, and mixed indexing."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 111
---

## Common Causes

- Using numeric index for a variable name or vice versa
- Mixing row and column indexing syntax (parentheses vs curly braces)
- Accessing a variable that doesn't exist in the table
- Confusing `T.Var` (returns column) with `T{:, 'Var'}` (returns data)
- Indexing with logical vector of wrong length

## How to Fix

```matlab
% WRONG: Using wrong indexing for table rows
T = table([1;2;3], {'a';'b';'c'}, 'VariableNames', {'ID','Name'});
row = T(1, :);       % Returns a table (1 row), not the data

% CORRECT: Access row data directly
row = T(1, :);               % Table with 1 row
rowID = T.ID(1);              % Scalar value
rowData = T{1, :};            % Cell array of row values
```

```matlab
% WRONG: Column indexing with curly braces (for single column)
col = T{:,'ID'};  % Returns double, but risky if multiple columns

% CORRECT: Use parentheses for table column, curly for raw data
col = T(:, 'ID');            % Table with 1 column
colData = T{:, 'ID'};       % Raw double array
colData = T.ID;              % Dot notation (shortest syntax)
```

```matlab
% CORRECT: Dynamic variable name access
varName = 'ID';
if ismember(varName, T.Properties.VariableNames)
    data = T.(varName);
else
    error('Variable %s not found in table', varName);
end
```

```matlab
% CORRECT: Row filtering with logical indexing
T = table((1:5)', {'A';'B';'C';'D';'E'}, [10;20;30;40;50], ...
    'VariableNames', {'ID','Name','Score'});

% Filter rows where Score > 25
filtered = T(T.Score > 25, :);

% Multiple conditions
subset = T(T.Score > 20 & T.Score < 50, :);
```

```matlab
% CORRECT: Add/remove rows and columns safely
T = table();
T.Name = {'Alice'; 'Bob'};
T.Age = [30; 25];

% Add a new column
T.Score = [88; 92];

% Remove a column
T = removevars(T, 'Age');

% Add a row
T = [T; table({'Charlie'}, [35], [78], 'VariableNames', T.Properties.VariableNames)];
```

## Examples

```matlab
% Example: Safe table access with validation
function val = tableGet(T, row, varName)
    assert(istable(T), 'Input must be a table');
    assert(ismember(varName, T.Properties.VariableNames), ...
        'Variable %s not found', varName);
    assert(row >= 1 && row <= height(T), ...
        'Row %d out of range (table has %d rows)', row, height(T));
    val = T{row, varName};
end
```

## Related Errors

- [Table Join](matlab-table-join) — merging tables
- [Table Error](matlab-table-error) — variable name issues
- [Index Out of Range](matlab-index-out-of-range) — array bounds
