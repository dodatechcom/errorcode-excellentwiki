---
title: "[Solution] MATLAB fscanf/fprintf — Format Spec, Size, Count Return"
description: "Fix MATLAB fscanf/fprintf errors: format specifiers, size output arguments, count return values, and format mismatch."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 140
---

## Common Causes

- Format spec not matching actual data (e.g., `%d` for text)
- `fscanf` returning fewer values than expected (size mismatch)
- Forgetting to check `count` return value for partial reads
- Using `%s` vs `%c` incorrectly in format strings
- `fprintf` writing to wrong file ID (0 = console vs file)

## How to Fix

```matlab
% WRONG: Format mismatch
fid = fopen('data.txt', 'r');
values = fscanf(fid, '%f');  % File contains text, not numbers
fclose(fid);

% CORRECT: Match format to data
fid = fopen('data.txt', 'r');
text = fscanf(fid, '%c');    % Read all as characters
fclose(fid);
```

```matlab
% WRONG: Not checking count return
fid = fopen('data.bin', 'rb');
data = fread(fid, [100, 100], 'double');  % May return fewer values
fclose(fid);

% CORRECT: Check count and reshape carefully
fid = fopen('data.bin', 'rb');
[data, count] = fread(fid, [100, 100], 'double');
fclose(fid);
if count < 10000
    warning('Partial read: %d of 10000 values', count);
    data(count+1:end) = 0;  % Pad with zeros
end
```

```matlab
% CORRECT: fscanf with size specification
fid = fopen('data.txt', 'r');

% Read up to 100 doubles
values = fscanf(fid, '%f', 100);

% Read specific matrix dimensions
matrix = fscanf(fid, '%f', [3, 4]);  % 3x4 matrix

fclose(fid);
```

```matlab
% CORRECT: fprintf format for different types
fid = fopen('output.txt', 'w');
fprintf(fid, 'Integer: %d\n', 42);
fprintf(fid, 'Float: %.6f\n', 3.14159);
fprintf(fid, 'String: %s\n', 'hello');
fprintf(fid, 'Hex: %08X\n', 255);
fprintf(fid, 'Scientific: %.4e\n', 0.001234);
fclose(fid);
```

```matlab
% CORRECT: Write to console (fid = 0) vs file
fprintf(0, 'This goes to console\n');  % fid=0 is stdout

fid = fopen('log.txt', 'a');
fprintf(fid, 'This goes to file\n');
fclose(fid);
```

## Examples

```matlab
% Example: Read and parse structured text file
function data = readStructuredFile(filename)
    fid = fopen(filename, 'r', 'n', 'UTF-8');
    cleanup = onCleanup(@() fclose(fid));

    header = fgetl(fid);  % Skip header
    nRows = str2double(fgetl(fid));

    data = zeros(nRows, 3);
    for k = 1:nRows
        line = fgetl(fid);
        values = sscanf(line, '%f,%f,%f');
        data(k, :) = values';
    end
end
```

## Related Errors

- [textscan](matlab-textscan) — advanced text parsing
- [fopen Error](matlab-fopen) — file access
- [fscanf Error](matlab-fscanf) — format spec details
