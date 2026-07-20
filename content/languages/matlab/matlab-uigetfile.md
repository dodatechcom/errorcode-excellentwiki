---
title: "[Solution] MATLAB uigetfile/uiputfile Dialog Error — Filter, Path & Cancel"
description: "Fix MATLAB uigetfile and uiputfile dialog errors for file filters, path handling, cancel detection, and platform issues."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 109
---

MATLAB's `uigetfile` and `uiputfile` open system file dialogs. Errors occur when the filter specification is invalid, the returned path is not checked for cancel, or the initial directory does not exist.

## Common Causes

- User clicks Cancel and the code does not check for `0` return value
- Filter string is malformed (must be `'*.ext;*.ext2', 'Description'` pairs)
- Initial directory path does not exist on the system
- Attempting to read the selected file before verifying it exists
- Mixing `uigetfile` with `uiputfile` filter syntax

## How to Fix

### Solution 1: Basic file selection with cancel check

```matlab
[filename, pathname] = uigetfile('*.mat', 'Select a MAT file');
if isequal(filename, 0)
    disp('User cancelled.');
else
    fullPath = fullfile(pathname, filename);
    disp(['Selected: ', fullPath]);
    load(fullPath);
end
```

### Solution 2: Multiple filter options

```matlab
[file, path] = uigetfile({ ...
    '*.m', 'MATLAB Files (*.m)'; ...
    '*.mat', 'MAT-Files (*.mat)'; ...
    '*.png;*.jpg', 'Images (*.png, *.jpg)'; ...
    '*.*', 'All Files (*.*)'}, ...
    'Select a file');
if ~isequal(file, 0)
    disp(fullfile(path, file));
end
```

### Solution 3: Save file with default name

```matlab
defaultName = 'output_data.mat';
[file, path] = uiputfile('*.mat', 'Save As', defaultName);
if ~isequal(file, 0)
    savePath = fullfile(path, file);
    data = rand(100, 3);
    save(savePath, 'data');
    disp(['Saved to: ', savePath]);
else
    disp('Save cancelled.');
end
```

### Solution 4: Validate initial directory exists

```matlab
initDir = '/path/to/data';
if ~isfolder(initDir)
    initDir = pwd;
    warning('Initial directory not found; using current directory.');
end
[file, path] = uigetfile('*.csv', 'Select CSV', initDir);
if ~isequal(file, 0)
    data = readtable(fullfile(path, file));
end
```

### Solution 5: Select multiple files

```matlab
[files, path] = uigetfile({'*.png;*.jpg;*.bmp', 'Image Files'}, ...
    'Select Images', 'MultiSelect', 'on');
if isequal(files, 0)
    disp('Cancelled.');
else
    if ischar(files)
        files = {files};
    end
    for i = 1:length(files)
        img = imread(fullfile(path, files{i}));
        fprintf('Loaded %s: %dx%d\n', files{i}, size(img,1), size(img,2));
    end
end
```

## Examples

Batch process all selected image files:

```matlab
[files, path] = uigetfile({'*.png;*.jpg', 'Images'}, ...
    'Select Images', 'MultiSelect', 'on');
if isequal(files, 0)
    return;
end
if ischar(files), files = {files}; end

for i = 1:length(files)
    img = imread(fullfile(path, files{i}));
    grayImg = rgb2gray(img);
    [~, name, ext] = fileparts(files{i});
    imwrite(grayImg, fullfile(path, [name '_gray' ext]));
end
disp('Done.');
```

## Related Errors

- [MATLAB msgbox Error](matlab-msgbox) — dialog and message boxes
- [MATLAB uicontrol Error](matlab-uicontrol) — GUI control creation
- [MATLAB File Transfer Error](matlab-file-transfer-error) — file I/O issues
