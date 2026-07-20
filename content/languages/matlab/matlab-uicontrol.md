---
title: "[Solution] MATLAB uicontrol Error — Style, Callback, Position & Units"
description: "Fix MATLAB uicontrol errors for invalid styles, missing callbacks, and Position/Units configuration with code examples."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 106
---

MATLAB's `uicontrol` creates GUI components in traditional figure windows, but errors occur when the style is invalid, the callback function is not properly defined, or Position and Units are misconfigured.

## Common Causes

- Specifying a `Style` value that does not exist (e.g., `'slider2'`)
- The `Callback` property references a function that is not on the path
- `Position` vector has incorrect number of elements (must be `[left bottom width height]`)
- Mixing `normalized` and `pixels` units without accounting for figure resizing
- Creating a uicontrol on a figure that has been deleted

## How to Fix

### Solution 1: Create a button with proper callback

```matlab
fig = figure('Name', 'Demo', 'Position', [100 100 400 300]);
btn = uicontrol('Style', 'pushbutton', 'String', 'Click Me', ...
    'Position', [150 200 100 40], ...
    'Callback', @(src, evt) disp('Button clicked!'));
```

### Solution 2: Use a function handle callback

```matlab
fig = figure('Name', 'Input Demo', 'Position', [100 100 400 200]);
editBox = uicontrol('Style', 'edit', 'String', 'Enter text', ...
    'Position', [50 120 200 30]);
uicontrol('Style', 'pushbutton', 'String', 'Submit', ...
    'Position', [270 120 80 30], ...
    'Callback', @(src, evt) submitCallback(editBox));

function submitCallback(editBox)
    val = get(editBox, 'String');
    disp(['You entered: ', val]);
end
```

### Solution 3: Arrange multiple controls with normalized units

```matlab
fig = figure('Name', 'Layout Demo', 'Position', [100 100 500 400]);
uicontrol('Style', 'text', 'String', 'Name:', ...
    'Units', 'normalized', 'Position', [0.05 0.85 0.2 0.1]);
uicontrol('Style', 'edit', 'String', '', ...
    'Units', 'normalized', 'Position', [0.25 0.85 0.5 0.1]);
uicontrol('Style', 'popupmenu', 'String', {'Red','Green','Blue'}, ...
    'Units', 'normalized', 'Position', [0.05 0.65 0.3 0.1]);
```

### Solution 4: Dynamic callback with persistent data

```matlab
fig = figure('Name', 'Counter', 'Position', [100 100 300 150]);
count = 0;
countText = uicontrol('Style', 'text', 'String', 'Count: 0', ...
    'Position', [50 90 200 40], 'FontSize', 14);
uicontrol('Style', 'pushbutton', 'String', 'Increment', ...
    'Position', [50 30 100 40], ...
    'Callback', @(src, evt) incrementCount());
uicontrol('Style', 'pushbutton', 'String', 'Reset', ...
    'Position', [160 30 100 40], ...
    'Callback', @(src, evt) resetCount());

    function incrementCount()
        count = count + 1;
        set(countText, 'String', sprintf('Count: %d', count));
    end

    function resetCount()
        count = 0;
        set(countText, 'String', 'Count: 0');
    end
end
```

### Solution 5: Validate figure handle before creating controls

```matlab
function createGUI()
    fig = figure('Name', 'Safe GUI', 'Position', [100 100 400 300]);
    if ~isvalid(fig)
        error('Failed to create figure.');
    end
    uicontrol('Style', 'pushbutton', 'String', 'OK', ...
        'Position', [150 50 100 40], ...
        'Callback', @(src, evt) close(fig));
end
```

## Examples

A complete slider-controlled plot:

```matlab
fig = figure('Name', 'Sine Wave', 'Position', [100 100 600 400]);
ax = axes('Parent', fig, 'Position', [0.1 0.3 0.8 0.6]);
x = linspace(0, 2*pi, 200);
h = plot(ax, x, sin(x));
xlabel(ax, 'x'); ylabel(ax, 'sin(x)');

slider = uicontrol('Style', 'slider', 'Min', 0.5, 'Max', 5, ...
    'Value', 1, 'Units', 'normalized', ...
    'Position', [0.1 0.05 0.8 0.1], ...
    'Callback', @(src, evt) updateFreq(src, h, x));

function updateFreq(src, h, x)
    freq = get(src, 'Value');
    set(h, 'YData', sin(freq * x));
end
```

## Related Errors

- [MATLAB uifigure Error](matlab-uifigure) — App Designer figure issues
- [MATLAB uitable Error](matlab-uitable) — table component errors
- [MATLAB msgbox Error](matlab-msgbox) — dialog box errors
