---
title: "[Solution] MATLAB load/readtable — Variable Names, File Format, Header"
description: "Fix MATLAB load/readtable errors: variable name extraction, file format detection, header rows, and encoding issues."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 137
---

## Common Causes

- `load` on non-MAT file without specifying format
- `readtable` failing on files with unexpected headers or delimiters
- Variable names from MAT file containing invalid characters
- Mixed numeric/text columns causing type inference issues
- File encoding mismatch (UTF-8 vs ASCII vs Windows-1252)

## How to Fix

```matlab
% WRONG: load on CSV file
data = load('data.csv');  % Error: not a MAT file

% CORRECT: Use readtable for CSV/text files
data = readtable('data.csv');
% Or readmatrix for numeric only:
data = readmatrix('data.csv');
```

```matlab
% WRONG: readtable guessing wrong header row
T = readtable('data.csv');  % First row used as variable names

% CORRECT: Specify header row
T = readtable('data.csv', 'NumHeaderLines', 1);  % Skip 1 header row
% Or set variable names explicitly:
T = readtable('data.csv', 'NumHeaderLines', 2, ...
    'VariableNames', {'ID','Name','Value'});
```

```matlab
% CORRECT: Handle different delimiters
T = readtable('data.csv', 'Delimiter', ',');      % CSV
T = readtable('data.tsv', 'Delimiter', '\t');      % Tab-separated
T = readtable('data.psv', 'Delimiter', '|');       % Pipe-separated
T = readtable('data.txt', 'Delimiter', 'auto');    % Auto-detect
```

```matlab
% CORRECT: Load MAT file with variable preservation
S = load('data.mat');  % Returns struct with all variables
fieldnames(S);

% Or load specific variables
S = load('data.mat', 'x', 'y');

% Or load directly into workspace
load('data.mat', 'x');
```

```matlab
% CORRECT: Handle mixed-type columns
T = readtable('data.csv', ...
    'VariableTypes', {'double','string','double','datetime'}, ...
    'TextType', 'string');
```

## Examples

```matlab
% Example: Robust file loading pipeline
function T = safeReadTable(filename)
    if ~isfile(filename)
        error('File not found: %s', filename);
    end
    [~, ~, ext] = fileparts(filename);
    switch lower(ext)
        case '.csv'
            T = readtable(filename, 'Delimiter', ',');
        case '.tsv'
            T = readtable(filename, 'Delimiter', '\t');
        case '.mat'
            S = load(filename);
            T = struct2table(S);
        otherwise
            error('Unsupported format: %s', ext);
    end
end
```

## Related Errors

- [Save Error](matlab-save-error) — file writing
- [fopen Error](matlab-fopen) — file access
- [textscan](matlab-textscan) — custom parsing
