---
title: "[Solution] MATLAB axes — Handle, gca/cla, yyaxis right, Multiple Axes"
description: "Fix MATLAB axes errors: axes handle management, gca/cla commands, yyaxis dual axes, and overlaying plots."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 131
---

## Common Causes

- Using `gca` creating unwanted axes in a figure with no axes
- `cla` clearing axes that should be preserved
- yyaxis left/right not properly synchronized
- Plotting on wrong axes after creating a second axes object
- Overlaying plots with incompatible axis scales

## How to Fix

```matlab
% WRONG: gca creates axes when none exist
ax = gca;  % Creates axes in current figure

% CORRECT: Create axes explicitly
h = figure;
ax = axes(h);
plot(ax, 1:10, rand(10,1));
```

```matlab
% WRONG: cla clearing everything
figure;
plot(1:10, rand(10,1));
cla;  % Deletes the plot

% CORRECT: Use cla on specific axes handle
h = figure;
ax1 = axes(h);
plot(ax1, 1:10, rand(10,1));
cla(ax1);  % Only clears ax1
```

```matlab
% CORRECT: yyaxis for dual y-axis plots
figure;
yyaxis left;
plot(1:10, rand(10,1) * 100);
ylabel('Temperature (°F)');

yyaxis right;
plot(1:10, rand(10,1) * 30);
ylabel('Pressure (psi)');

xlabel('Time');
legend('Temperature', 'Pressure');
```

```matlab
% CORRECT: Multiple independent axes
figure;
ax1 = axes('Position', [0.1 0.5 0.8 0.4]);
plot(ax1, 1:10, rand(10,1));
title(ax1, 'Top Plot');

ax2 = axes('Position', [0.1 0.05 0.8 0.4]);
plot(ax2, 1:10, rand(10,1));
title(ax2, 'Bottom Plot');
```

```matlab
% CORRECT: axes with specific properties
ax = axes('XLim', [0 10], 'YLim', [0 1], ...
          'FontSize', 12, 'FontName', 'Arial');
line('XData', 1:10, 'YData', rand(10,1), 'Parent', ax);
```

## Examples

```matlab
% Example: Overlay histogram and density on same axes
data = randn(1000, 1);
figure;
ax1 = axes;
histogram(ax1, data, 'Normalization', 'pdf', 'FaceAlpha', 0.5);
hold(ax1, 'on');
x = linspace(-4, 4, 200);
plot(ax1, x, normpdf(x), 'r-', 'LineWidth', 2);
hold(ax1, 'off');
legend(ax1, 'Histogram', 'PDF');
```

## Related Errors

- [Figure Error](matlab-figure-error) — figure handle management
- [Plot Error](matlab-plot-error) — line plotting
- [Colormap](matlab-colormap) — color mapping
