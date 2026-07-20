---
title: "[Solution] MATLAB axis limits — xlim/ylim/zlim, equal/auto/square"
description: "Fix MATLAB axis limit errors: xlim/ylim/zlim setting, axis equal/auto/square, and log scale issues."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 129
---

## Common Causes

- Setting axis limits that exclude all data points
- Using `axis equal` with log scale causing display issues
- Forgetting to update axis limits after adding new plot data
- Zlim not visible in 2D view — need `view(3)`
- Confusing `axis tight` with `axis auto`

## How to Fix

```matlab
% WRONG: Axis limits hiding data
figure;
plot([1 2 3], [4 5 6]);
xlim([0 1]);  % All data is outside visible range

% CORRECT: Set limits to encompass data or use auto
figure;
plot([1 2 3], [4 5 6]);
xlim([0.5 3.5]);  % Includes data with padding
% Or:
axis tight;  % Fits exactly to data
```

```matlab
% WRONG: axis equal with different scales makes plot hard to read
figure;
semilogy(1:10, exp(1:10));
axis equal;  % Distorts log-scale display

% CORRECT: Use axis normal for log scale
figure;
semilogy(1:10, exp(1:10));
axis normal;  % Or omit axis equal for log plots
```

```matlab
% CORRECT: axis square vs axis equal
% axis equal: equal data units on both axes
% axis square: square-shaped axes regardless of data range

figure;
plot([0 1 0], [0 1 0]);
axis equal;   % Isosceles right triangle looks correct
axis square;  % Axes are square but data may be distorted
```

```matlab
% CORRECT: Control z-axis in 3D plots
figure;
surf(peaks);
zlim([-8 8]);  % Only visible after view(3) or 3D command
view(3);
```

```matlab
% CORRECT: Freeze axis limits for animation
figure;
h = plot(NaN, NaN, 'o');
xlim([0 10]); ylim([0 10]);
for k = 1:100
    set(h, 'XData', rand, 'YData', rand);
    drawnow limitrate;
end
```

## Examples

```matlab
% Example: Combined axis control
figure;
tiledlayout(1, 2);

nexttile;
x = 0:0.01:4*pi;
plot(x, sin(x));
xlim([0 4*pi]);
ylim([-1.5 1.5]);
title('Linear scale');

nexttile;
plot(x, exp(sin(x)));
set(gca, 'YScale', 'log');
title('Log scale');
```

## Related Errors

- [Plot Error](matlab-plot-error) — plot display
- [Figure Error](matlab-figure-error) — figure management
- [3D Plot](matlab-3d-plot) — 3D visualization
