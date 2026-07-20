---
title: "[Solution] MATLAB fopen/fclose — File ID, Permission, Encoding, Not Found"
description: "Fix MATLAB fopen/fclose errors: file permission modes, encoding specification, file-not-found, and resource cleanup."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 139
---

## Common Causes

- File not found (path error or missing file)
- Wrong permission mode (reading with 'w' or writing with 'r')
- Not closing file handles causing resource leaks
- Encoding mismatch when reading non-ASCII files
- File path with special characters not escaped

## How to Fix

```matlab
% WRONG: Opening file without checking if it exists
fid = fopen('data.txt', 'r');  % Returns -1 if not found
data = fread(fid, '*char');

% CORRECT: Check fopen return value
fid = fopen('data.txt', 'r');
if fid == -1
    error('Cannot open data.txt: %s', ferror(fid));
end
data = fread(fid, '*char');
fclose(fid);
```

```matlab
% WRONG: Not closing file (resource leak)
fid = fopen('log.txt', 'a');
for k = 1:1000
    fprintf(fid, 'Line %d\n', k);
end
% File handle leaked

% CORRECT: Always close with try/catch or onCleanup
fid = fopen('log.txt', 'a');
cleanup = onCleanup(@() fclose(fid));
for k = 1:1000
    fprintf(fid, 'Line %d\n', k);
end
% cleanup object calls fclose when function exits
```

```matlab
% CORRECT: Proper permission modes
fid = fopen('file.txt', 'r');    % Read only
fid = fopen('file.txt', 'w');    % Write (create/truncate)
fid = fopen('file.txt', 'a');    % Append
fid = fopen('file.txt', 'r+');   % Read and write
fid = fopen('file.txt', 'wt');   % Write text (Windows line endings)
```

```matlab
% CORRECT: Handle encoding for non-ASCII files
fid = fopen('data.txt', 'r', 'n', 'UTF-8');
if fid == -1
    error('File not found');
end
line = fgetl(fid);
fclose(fid);
```

```matlab
% CORRECT: Temporary file with cleanup
function processTempFile()
    tmpFile = [tempname, '.tmp'];
    fid = fopen(tmpFile, 'w');
    cleanup = onCleanup(@() deleteIfExists(tmpFile));

    fprintf(fid, 'temporary data\n');
    fclose(fid);

    % Process...
end

function deleteIfExists(f)
    if isfile(f), delete(f); end
end
```

## Examples

```matlab
% Example: Robust file read pipeline
function lines = readLines(filename)
    fid = fopen(filename, 'r', 'n', 'UTF-8');
    if fid == -1
        error('Cannot open %s', filename);
    end
    cleanup = onCleanup(@() fclose(fid));

    lines = {};
    while ~feof(fid)
        line = fgetl(fid);
        if ischar(line)
            lines{end+1} = line;
        end
    end
end
```

## Related Errors

- [fscanf Error](matlab-fscanf) — format spec reading
- [textscan](matlab-textscan) — formatted text parsing
- [Load Error](matlab-load-error) — file loading
