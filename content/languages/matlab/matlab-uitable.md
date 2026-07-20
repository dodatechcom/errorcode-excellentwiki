---
title: "[Solution] MATLAB uitable Error — ColumnName, Data & CellEditCallback"
description: "Fix MATLAB uitable errors for ColumnName configuration, Data type mismatches, and CellEditCallback handling with code examples."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 108
---

MATLAB's `uitable` displays tabular data in GUI figures. Errors occur when `ColumnName` length does not match the data columns, `Data` types are inconsistent, or `CellEditCallback` is not properly configured.

## Common Causes

- `ColumnName` cell array length does not match the number of data columns
- `Data` contains mixed types in a column (e.g., numeric and string)
- `CellEditCallback` does not accept the correct number of input arguments
- Setting `Data` to a struct without converting it to a cell array
- Attempting to edit a read-only column when `ColumnEditable` is not set

## How to Fix

### Solution 1: Create a basic editable table

```matlab
fig = figure('Name', 'Table Demo', 'Position', [100 100 500 300]);
data = {'Alice', 90; 'Bob', 85; 'Charlie', 92};
colNames = {'Name', 'Score'};
t = uitable(fig, 'Data', data, 'ColumnName', colNames, ...
    'Position', [20 20 460 260], 'ColumnEditable', [false true]);
```

### Solution 2: Use CellEditCallback for validation

```matlab
fig = figure('Name', 'Validated Table', 'Position', [100 100 500 300]);
data = {10, 20, 30; 40, 50, 60};
colNames = {'A', 'B', 'C'};
t = uitable(fig, 'Data', data, 'ColumnName', colNames, ...
    'Position', [20 20 460 260], 'ColumnEditable', true, ...
    'CellEditCallback', @(src, evt) validateEdit(src, evt));

function validateEdit(src, evt)
    newVal = evt.NewData;
    if ~isnumeric(newVal) || newVal < 0
        src.Data{evt.Indices(1), evt.Indices(2)} = evt.PreviousData;
        warning('Value must be a non-negative number.');
    end
end
```

### Solution 3: Convert struct data to cell array

```matlab
patients = struct('Name', {'John','Jane','Jim'}, ...
                  'Age', {28, 34, 45}, ...
                  'BP', {120, 135, 110});

fnames = fieldnames(patients);
colNames = fnames';
dataCell = cell(length(patients), length(fnames));
for i = 1:length(fnames)
    col = {patients.(fnames{i})};
    dataCell(:, i) = col(:);
end

fig = figure('Name', 'Struct Table', 'Position', [100 100 400 200]);
uitable(fig, 'Data', dataCell, 'ColumnName', colNames, ...
    'Position', [20 20 360 160]);
```

### Solution 4: Add rows dynamically

```matlab
fig = figure('Name', 'Dynamic Table', 'Position', [100 100 500 400]);
data = {};
colNames = {'Item', 'Quantity', 'Price'};
t = uitable(fig, 'Data', data, 'ColumnName', colNames, ...
    'Position', [20 60 460 320], 'ColumnEditable', true);
uicontrol('Style', 'pushbutton', 'String', 'Add Row', ...
    'Position', [20 10 100 30], ...
    'Callback', @(src, evt) addRow(t));

function addRow(t)
    currentData = t.Data;
    newRow = {'New Item', 1, 0.00};
    t.Data = [currentData; newRow];
end
```

### Solution 5: Color rows conditionally

```matlab
fig = figure('Name', 'Colored Table', 'Position', [100 100 500 300]);
data = {'Pass', 85; 'Fail', 42; 'Pass', 91; 'Fail', 38};
colNames = {'Result', 'Score'};
t = uitable(fig, 'Data', data, 'ColumnName', colNames, ...
    'Position', [20 20 460 260]);

for i = 1:size(data, 1)
    if strcmp(data{i, 1}, 'Fail')
        t.BackgroundColor(i, :) = [1.0 0.8 0.8];
    else
        t.BackgroundColor(i, :) = [0.8 1.0 0.8];
    end
end
```

## Examples

Spreadsheet-like table with sorting awareness:

```matlab
fig = figure('Name', 'Scoreboard', 'Position', [100 100 500 350]);
data = {'Alice', 95; 'Bob', 82; 'Charlie', 91; 'Diana', 88};
colNames = {'Name', 'Score'};
t = uitable(fig, 'Data', data, 'ColumnName', colNames, ...
    'Position', [20 50 460 280], 'ColumnEditable', [false true], ...
    'CellEditCallback', @(src, evt) disp(sprintf('Row %d Score: %d', evt.Indices(1), evt.NewData)));
```

## Related Errors

- [MATLAB uifigure Error](matlab-uifigure) — App Designer figure issues
- [MATLAB uicontrol Error](matlab-uicontrol) — traditional GUI controls
- [MATLAB Table Error](matlab-table-error) — table data type issues
