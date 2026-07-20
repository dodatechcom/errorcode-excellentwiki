---
title: "[Solution] MATLAB uifigure App Designer Error — Create, Close & Components"
description: "Fix MATLAB uifigure errors in App Designer for figure creation, component layout, close callbacks, and property access."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 107
---

MATLAB's `uifigure` is the foundation of App Designer applications. Errors occur when components are added to a deleted figure, properties are accessed incorrectly, or close callbacks are not properly configured.

## Common Causes

- Adding components to a `uifigure` that has been deleted or closed
- Accessing component properties that do not exist for that component type
- Using traditional `uicontrol` functions inside a `uifigure` (incompatible)
- Calling `delete(fig)` inside a `CloseRequestFcn` without proper cleanup
- Mixing `figure` and `uifigure` in the same application

## How to Fix

### Solution 1: Create a uifigure with components programmatically

```matlab
fig = uifigure('Name', 'My App', 'Position', [100 100 500 400]);
btn = uibutton(fig, 'push', 'Text', 'Click Me', ...
    'Position', [150 300 120 40], ...
    'ButtonPushedFcn', @(src, evt) disp('Clicked!'));
```

### Solution 2: Close figure safely with CloseRequestFcn

```matlab
fig = uifigure('Name', 'Close Demo', 'Position', [100 100 400 300]);
fig.CloseRequestFcn = @(src, evt) safeClose(src);

function safeClose(fig)
    selection = uiconfirm(fig, 'Are you sure?', 'Confirm Close');
    if strcmp(selection, 'OK')
        delete(fig);
    end
end
```

### Solution 3: Add and manage multiple components

```matlab
fig = uifigure('Name', 'Form', 'Position', [100 100 400 350]);
uilabel(fig, 'Text', 'Username:', 'Position', [30 280 80 22]);
uitextfield(fig, 'Position', [120 280 200 22]);
uilabel(fig, 'Text', 'Password:', 'Position', [30 240 80 22]);
uieditfield(fig, 'text', 'Position', [120 240 200 22]);
uibutton(fig, 'push', 'Text', 'Login', ...
    'Position', [120 180 100 30], ...
    'ButtonPushedFcn', @(src, evt) disp('Login pressed'));
```

### Solution 4: Update component properties dynamically

```matlab
fig = uifigure('Name', 'Dynamic', 'Position', [100 100 400 300]);
lbl = uilabel(fig, 'Text', 'Value: 0', 'Position', [50 250 200 22]);
slider = uislider(fig, 'Limits', [0 100], 'Value', 0, ...
    'Position', [50 200 250 3], ...
    'ValueChangedFcn', @(src, evt) updateLabel(lbl, src));

function updateLabel(lbl, src)
    lbl.Text = sprintf('Value: %.1f', src.Value);
end
```

### Solution 5: Check figure validity before operations

```matlab
fig = uifigure('Name', 'Valid Check', 'Position', [100 100 400 300]);
btn = uibutton(fig, 'push', 'Text', 'Close', ...
    'Position', [150 200 100 40], ...
    'ButtonPushedFcn', @(src, evt) closeFigure(fig));

function closeFigure(fig)
    if isvalid(fig)
        delete(fig);
    else
        warning('Figure already deleted.');
    end
end
```

## Examples

Build a simple calculator app:

```matlab
fig = uifigure('Name', 'Calculator', 'Position', [100 100 300 400]);
display = uitextfield(fig, 'Value', '0', ...
    'Position', [20 330 260 40], 'FontSize', 20);

btnLabels = {'7','8','9','/'; '4','5','6','*'; '1','2','3','-'; '0','.','=','+'};
for row = 1:4
    for col = 1:4
        x = 20 + (col-1)*65;
        y = 330 - row*65;
        uibutton(fig, 'push', 'Text', btnLabels{row, col}, ...
            'Position', [x y 60 55], ...
            'ButtonPushedFcn', @(src, evt) buttonPress(display, src.Text));
    end
end
```

## Related Errors

- [MATLAB uicontrol Error](matlab-uicontrol) — traditional GUI controls
- [MATLAB uitable Error](matlab-uitable) — table component issues
- [MATLAB msgbox Error](matlab-msgbox) — dialog box errors
