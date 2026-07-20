---
title: "[Solution] MATLAB msgbox/errordlg/warndlg/questdlg Error — Button, Timeout & Dialog"
description: "Fix MATLAB msgbox, errordlg, warndlg, and questdlg errors for button handling, timeout behavior, and dialog creation issues."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 110
---

MATLAB's `msgbox`, `errordlg`, `warndlg`, and `questdlg` create modal and non-modal dialog boxes. Errors occur when button outputs are not handled correctly, modal dialogs block execution unexpectedly, or the figure handle is invalid.

## Common Causes

- `questdlg` return value is not compared with `strcmp` (returns a string, not a number)
- Calling `errordlg` with more than 3 input arguments incorrectly
- Using `msgbox` in a loop without waiting for the user to close it
- The dialog's figure handle becomes invalid before the callback runs
- Passing empty strings to dialog title or message

## How to Fix

### Solution 1: Simple message box

```matlab
msgbox('Operation completed successfully.', 'Success');
```

### Solution 2: Error dialog with custom icon

```matlab
errordlg('File not found. Please check the path.', 'File Error', 'modal');
```

### Solution 3: Warning dialog with non-modal behavior

```matlab
h = warndlg('Disk space is low.', 'Warning');
% Continue execution without waiting
disp('Continuing with operation...');
```

### Solution 4: Question dialog with button handling

```matlab
choice = questdlg('Save changes before closing?', ...
    'Unsaved Changes', 'Yes', 'No', 'Cancel', 'Yes');

switch choice
    case 'Yes'
        save('workspace.mat');
        disp('Saved.');
    case 'No'
        disp('Discarded.');
    case 'Cancel'
        disp('Cancelled.');
    otherwise
        disp('Dialog closed without selection.');
end
```

### Solution 5: Input dialog for user data

```matlab
answer = inputdlg({'Enter name:', 'Enter age:'}, 'User Info', [1 40; 1 40], {'John', '25'});
if ~isempty(answer)
    name = answer{1};
    age = str2double(answer{2});
    fprintf('Name: %s, Age: %d\n', name, age);
end
```

## Examples

Confirmation dialog before destructive action:

```matlab
function deleteWithConfirm(filename)
    choice = questdlg( ...
        sprintf('Delete "%s"?', filename), ...
        'Confirm Delete', 'Delete', 'Cancel', 'Cancel');

    if strcmp(choice, 'Delete')
        if delete(filename)
            msgbox('File deleted.', 'Done');
        else
            errordlg('Failed to delete file.', 'Error');
        end
    end
end
```

## Related Errors

- [MATLAB uicontrol Error](matlab-uicontrol) — GUI control creation
- [MATLAB uifigure Error](matlab-uifigure) — App Designer figure issues
- [MATLAB uigetfile Error](matlab-uigetfile) — file dialog issues
