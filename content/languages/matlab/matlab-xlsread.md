---
title: "[Solution] MATLAB xlsread/xlswrite — Sheet, Range, COM Server, Excel Format"
description: "Fix MATLAB xlsread/xlswrite errors: sheet selection, range specification, COM server issues, and modern alternatives."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 142
---

## Common Causes

- Excel not installed (COM server unavailable on Linux/Mac)
- Sheet name not found in workbook
- Range specification format incorrect
- File open in Excel preventing write
- Using deprecated xlsread instead of readtable/readcell

## How to Fix

```matlab
% WRONG: xlsread on Linux (no COM server)
[num, txt, raw] = xlsread('data.xlsx');  % Error on Linux

% CORRECT: Use readcell or readtable (cross-platform)
data = readcell('data.xlsx');          % All data as cell array
T = readtable('data.xlsx');            % As table
[num, txt, raw] = readcell('data.xlsx');  % Similar to xlsread output
```

```matlab
% WRONG: Wrong range format
data = xlsread('data.xlsx', 'Sheet1', 'A1:C10');  % May fail

% CORRECT: Specify sheet and range properly
data = readmatrix('data.xlsx', 'Sheet', 'Sheet1', 'Range', 'A1:C10');
% Or for cell data:
data = readcell('data.xlsx', 'Sheet', 'Sheet1', 'Range', 'A1:C10');
```

```matlab
% CORRECT: List available sheets
info = sheetnames('data.xlsx');
disp(info);

% Read specific sheet
T = readtable('data.xlsx', 'Sheet', info{1});
```

```matlab
% CORRECT: Write to Excel cross-platform
T = table([1;2;3], {'A';'B';'C'}, 'VariableNames', {'ID','Name'});
writetable(T, 'output.xlsx', 'Sheet', 'Results');

% Write cell array
data = {'Header1','Header2'; 1, 2; 3, 4};
writecell(data, 'output.xlsx', 'Sheet', 'Data');
```

```matlab
% CORRECT: append rows to existing Excel file
if isfile('output.xlsx')
    existing = readtable('output.xlsx');
    T = [existing; table([4;5], {'D';'E'}, 'VariableNames', {'ID','Name'})];
else
    T = table([4;5], {'D';'E'}, 'VariableNames', {'ID','Name'});
end
writetable(T, 'output.xlsx');
```

## Examples

```matlab
% Example: Full Excel read/write workflow
function processExcel(inputFile, outputFile)
    % Read
    T = readtable(inputFile, 'Sheet', 'Raw');

    % Process
    T.Calculated = T.Value * 1.1;

    % Write results
    writetable(T, outputFile, 'Sheet', 'Processed');

    % Write summary to separate sheet
    summary = table({'Mean';'Std';'Max'}, [mean(T.Value); std(T.Value); max(T.Value)], ...
        'VariableNames', {'Statistic','Value'});
    writetable(summary, outputFile, 'Sheet', 'Summary');
end
```

## Related Errors

- [Load Error](matlab-load-error) — MAT file loading
- [textscan](matlab-textscan) — text file parsing
- [fopen Error](matlab-fopen) — file access
