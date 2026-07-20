---
title: "[Solution] MATLAB figure — Handle, gcf/clf/close, Invisible, Resize"
description: "Fix MATLAB figure errors: figure handle management, gcf/clf/close commands, invisible figures, and resize behavior."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 130
---

## Common Causes

- Using `gcf` when no figure exists creating an unwanted figure
- `close all` closing figures needed by other scripts
- Figure handle variable being overwritten or garbage-collected
- Invisible figure (`Visible`, 'off') not becoming visible later
- Resize causing figure to change size unexpectedly

## How to Fix

```matlab
% WRONG: gcf creates figure when none exists
h = gcf;  % Creates new figure even if you didn't want one

% CORRECT: Get or create explicitly
if isempty(findobj('Type', 'figure'))
    h = figure('Name', 'My Plot');
else
    h = gcf;
end
```

```matlab
% WRONG: close all closing figures you need
close all;  % Closes everything

% CORRECT: Close specific figures by handle or tag
figs = findobj('Type', 'figure', 'Tag', 'temporary');
close(figs);

% Or close by number
close(figure(3));
```

```matlab
% CORRECT: Store figure handle in base workspace
h = figure('Name', 'Analysis', 'NumberTitle', 'off');
% Save handle for later use
assignin('base', 'myFigHandle', h);

% Later, modify the figure
h = evalin('base', 'myFigHandle');
if ishandle(h)
    figure(h);  % Bring to front
end
```

```matlab
% CORRECT: Create invisible figure, render, then show
h = figure('Visible', 'off');
plot(1:10, rand(10,1));
title('Rendered Offscreen');
drawnow;
h.Visible = 'on';  % Show when ready
```

```matlab
% CORRECT: Control figure size
h = figure('Position', [100 100 800 600], ...  % [left bottom width height]
           'Units', 'pixels', ...
           'Resize', 'on');

% Or fixed size
h = figure('Position', [100 100 800 600], ...
           'Resize', 'off');
```

## Examples

```matlab
% Example: Batch figure generation with proper handle management
for k = 1:5
    h = figure('Visible', 'off', 'Position', [100 100 600 400]);
    plot(rand(100,1));
    title(sprintf('Batch Plot %d', k));
    saveas(h, sprintf('plot_%d.png', k));
    close(h);  % Close immediately to free memory
end
```

## Related Errors

- [Axes Error](matlab-axes-error) — axes handle management
- [Plot Error](matlab-plot-error) — line plotting
- [Subplot](matlab-subplot) — layout management
