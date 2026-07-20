---
title: "[Solution] MATLAB HDF5 — h5read/h5write Dataset, Attribute, File Create"
description: "Fix MATLAB HDF5 errors: h5read/h5write operations, dataset creation, attribute access, and file structure."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 144
---

## Common Causes

- Dataset name or path not found in HDF5 file
- Writing to read-only HDF5 file
- Attribute doesn't exist at specified location
- File created by h5create not closed before read
- Datatype mismatch between MATLAB and HDF5 dataset

## How to Fix

```matlab
% WRONG: Reading nonexistent dataset
data = h5read('file.h5', '/nonexistent/path');  % Error

% CORRECT: List contents first
info = h5info('file.h5');
disp({info.Datasets.Name});  % List datasets

% Read with correct path
data = h5read('file.h5', '/dataset_name');
```

```matlab
% WRONG: Writing to file without creating it
h5write('new.h5', '/data', rand(10));  % Error: file doesn't exist

% CORRECT: Create file and dataset first
h5create('new.h5', '/data', [10 10]);
h5write('new.h5', '/data', rand(10));
```

```matlab
% CORRECT: Write to existing file with append
if ~isfile('data.h5')
    h5create('data.h5', '/measurements', [Inf 5], 'ChunkSize', [100 5]);
end

newData = rand(50, 5);
% Use h5write for fixed-size, or low-level API for appending
info = h5info('data.h5', '/measurements');
currentSize = info.Dataspace.Size;
h5write('data.h5', '/measurements', newData, ...
    [currentSize(1)+1 1], size(newData));
```

```matlab
% CORRECT: Read/write attributes
h5writeatt('file.h5', '/dataset_name', 'units', 'meters');
h5writeatt('file.h5', '/dataset_name', 'scale', 3.14);

units = h5readatt('file.h5', '/dataset_name', 'units');
scale = h5readatt('file.h5', '/dataset_name', 'scale');
```

```matlab
% CORRECT: Inspect HDF5 file structure
function printH5Info(filename)
    info = h5info(filename);
    fprintf('File: %s\n', filename);
    fprintf('Groups:\n');
    for k = 1:numel(info.Groups)
        fprintf('  /%s\n', info.Groups(k).Name);
    end
    fprintf('Datasets:\n');
    for k = 1:numel(info.Datasets)
        d = info.Datasets(k);
        fprintf('  %s: %s [%s]\n', d.Name, ...
            mat2str(d.Dataspace.Size), mat2str(d.Datatype.Class));
    end
end
```

## Examples

```matlab
% Example: Full HDF5 workflow
filename = 'experiment.h5';

% Create structure
h5create(filename, '/temperature', [Inf 3], 'ChunkSize', [100 3]);
h5create(filename, '/pressure', [Inf 1], 'ChunkSize', [100 1]);

% Write data
tempData = 20 + 10*rand(200, 3);
presData = 1013 + 5*rand(200, 1);
h5write(filename, '/temperature', tempData);
h5write(filename, '/pressure', presData);

% Add metadata
h5writeatt(filename, '/', 'experiment', 'Lab Test A');
h5writeatt(filename, '/temperature', 'units', 'Celsius');

% Read back
T = h5read(filename, '/temperature');
P = h5read(filename, '/pressure');
units = h5readatt(filename, '/temperature', 'units');
```

## Related Errors

- [Load Error](matlab-load-error) — MAT file operations
- [Save Error](matlab-save-error) — file saving
- [fopen Error](matlab-fopen) — file access
