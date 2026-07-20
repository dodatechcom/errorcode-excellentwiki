---
title: "[Solution] MATLAB textscan — Format, Delimiter, emptyValue, CollectOutput"
description: "Fix MATLAB textscan errors: format string specification, delimiter settings, emptyValue handling, and CollectOutput."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 141
---

## Common Causes

- Format string not matching number of columns in file
- Delimiter not specified causing fields to run together
- Missing values crashing without `emptyValue` set
- `CollectOutput` true but format has mixed types
- Not calling `fclose` after `textscan`

## How to Fix

```matlab
% WRONG: Format string with wrong number of fields
fid = fopen('data.csv', 'r');
% File has 4 columns but format only has 3
C = textscan(fid, '%f %s %f');  % Reads 3 fields, last column lost
fclose(fid);

% CORRECT: Match format to all columns
fid = fopen('data.csv', 'r');
C = textscan(fid, '%f %s %f %f', 'Delimiter', ',');
fclose(fid);
```

```matlab
% WRONG: No delimiter specified for CSV
fid = fopen('data.csv', 'r');
C = textscan(fid, '%f%s%f');  % Fields merged together

% CORRECT: Specify delimiter
fid = fopen('data.csv', 'r');
C = textscan(fid, '%f %s %f', 'Delimiter', ',', 'EmptyValue', NaN);
fclose(fid);
```

```matlab
% CORRECT: Handle missing/empty values
fid = fopen('data.csv', 'r');
C = textscan(fid, '%f %s %f', ...
    'Delimiter', ',', ...
    'EmptyValue', NaN, ...          % Replace empty with NaN
    'TreatAsEmpty', {'NA', 'NULL', ''}, ...  % These strings become NaN
    'ReturnOnError', true);          % Don't crash on parse errors
fclose(fid);
```

```matlab
% CORRECT: CollectOutput for numeric arrays
fid = fopen('data.txt', 'r');
% Multiple numeric columns → one array
C = textscan(fid, '%f %f %f', 'CollectOutput', true);
fclose(fid);
matrix = C{1};  % Single Nx3 array instead of 3 separate cells
```

```matlab
% CORRECT: Read entire file at once
fid = fopen('large.txt', 'r');
C = textscan(fid, '%f %f', 'Delimiter', ',', 'HeaderLines', 1);
fclose(fid);

x = C{1};
y = C{2};
fprintf('Read %d data points\n', numel(x));
```

## Examples

```matlab
% Example: Parse complex CSV with mixed types
function T = parseCSV(filename)
    fid = fopen(filename, 'r', 'n', 'UTF-8');
    if fid == -1
        error('File not found: %s', filename);
    end

    % Read header
    header = strsplit(fgetl(fid), ',');

    % Read data
    nCols = numel(header);
    fmt = strjoin([repmat({'%f'}, 1, nCols-1), {'%s'}], ' ');
    C = textscan(fid, fmt, 'Delimiter', ',', 'EmptyValue', NaN);
    fclose(fid);

    T = table(C{:}, 'VariableNames', matlab.lang.makeValidName(header));
end
```

## Related Errors

- [fscanf Error](matlab-fscanf) — formatted reading
- [fopen Error](matlab-fopen) — file access
- [Load Error](matlab-load-error) — file loading
