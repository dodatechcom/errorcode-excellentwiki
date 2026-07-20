---
title: "[Solution] MATLAB save — MAT Version, -v7.3, -append, Compression"
description: "Fix MATLAB save errors: MAT file version compatibility, -v7.3 format, -append mode, and file size optimization."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 138
---

## Common Causes

- Saving large variables in older MAT format losing compression
- `-v7.3` needed for variables > 2GB but incompatible with older MATLAB
- `-append` creating duplicate variables instead of overwriting
- Saving variables with names conflicting with MATLAB keywords
- File permissions preventing write access

## How to Fix

```matlab
% WRONG: Old format without compression (large file)
save('data.mat', 'largeMatrix');  % Default version, no compression

% CORRECT: Use -v7.3 for large files with HDF5 compression
save('data.mat', 'largeMatrix', '-v7.3', '-nocompression');
% Or with compression:
save('data.mat', 'largeMatrix', '-v7.3');
```

```matlab
% WRONG: -append creating duplicates
save('data.mat', 'x');  % Creates with x
save('data.mat', 'x', '-append');  % Overwrites x (expected)

% CORRECT: Clear variable before appending
if isfile('data.mat')
    oldData = load('data.mat');
end
save('data.mat', 'x', '-append');
```

```matlab
% CORRECT: Save specific variables with version control
save('results.mat', 'A', 'B', 'C', '-v7.3');

% Save with version for compatibility
save('legacy.mat', 'data', '-v6');    % Oldest, most compatible
save('modern.mat', 'data', '-v7.3');  % Supports large files, HDF5
```

```matlab
% CORRECT: Save to specific path
savePath = fullfile(outputDir, 'results.mat');
save(savePath, 'results', '-v7.3');
```

```matlab
% CORRECT: Check save succeeded
function safeSave(filename, varargin)
    try
        save(filename, varargin{:}, '-v7.3');
        info = dir(filename);
        fprintf('Saved %s (%.1f MB)\n', filename, info.bytes/1e6);
    catch ME
        error('Save failed: %s', ME.message);
    end
end
```

## Examples

```matlab
% Example: Save multiple variables to different files
data = rand(1000);
labels = string(randi(10, 1000, 1));
config = struct('version', 2, 'author', 'test');

save('data.mat', 'data', '-v7.3');
save('metadata.mat', 'labels', 'config', '-v7.3');
```

## Related Errors

- [Load Error](matlab-load-error) — file reading
- [fopen Error](matlab-fopen) — file access
- [HDF5 Error](matlab-hdf5-error) — HDF5 operations
