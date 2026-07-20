---
title: "[Solution] MATLAB subplot — Index, tiledlayout, nexttile, Grid Layout"
description: "Fix MATLAB subplot errors: subplot indexing, tiledlayout positioning, nexttile usage, and grid layout management."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 128
---

## Common Causes

- Subplot index exceeding grid dimensions
- Confusing subplot(m,n,p) with linear index p (1-based)
- Using subplot inside a loop without proper index management
- Mixing subplot and tiledlayout causing layout conflicts
- Axes created by subplot being overwritten

## How to Fix

```matlab
% WRONG: Subplot index out of range
figure;
subplot(2, 3, 7);  % Error: max index is 6 for 2x3 grid

% CORRECT: Ensure index within grid
figure;
subplot(2, 3, 6);  % Valid: 2 rows, 3 cols, index 6
```

```matlab
% WRONG: Loop with subplot but wrong indexing
figure;
for k = 1:10
    subplot(3, 3, k);  % k=10 exceeds 3x3=9
    plot(rand(10,1));
end

% CORRECT: Use tiledlayout for automatic layout
figure;
t = tiledlayout(3, 4);  % 3x4 grid, can hold 12 plots
for k = 1:10
    nexttile(t);
    plot(rand(10,1));
    title(sprintf('Plot %d', k));
end
```

```matlab
% CORRECT: Subplot with proper row/column calculation
rows = 2; cols = 3;
figure;
for k = 1:6
    subplot(rows, cols, k);
    plot(rand(10, 1));
    title(sprintf('Subplot %d', k));
end
```

```matlab
% CORRECT: tiledlayout with variable-size plots
figure;
t = tiledlayout('flow');  % Auto-sized tiles
for k = 1:7
    nexttile(t);
    bar(rand(5, 1));
end
```

```matlab
% CORRECT: Get axes handle from subplot for later modification
figure;
ax1 = subplot(2,1,1);
plot(ax1, 1:10, rand(10,1));
title(ax1, 'Plot 1');

ax2 = subplot(2,1,2);
plot(ax2, 1:10, rand(10,1));
title(ax2, 'Plot 2');
```

## Examples

```matlab
% Example: Dashboard layout with tiledlayout
figure;
t = tiledlayout(2, 3, 'TileSpacing', 'compact', 'Padding', 'compact');

nexttile(t); plot(rand(10,1)); title('Line');
nexttile(t); bar(rand(5,1)); title('Bar');
nexttile(t); scatter(rand(100,1), rand(100,1)); title('Scatter');
nexttile(t); pie([30 20 50]); title('Pie');
nexttile(t); histogram(randn(1000,1)); title('Histogram');
nexttile(t); imagesc(rand(10)); title('Image');
```

## Related Errors

- [Plot Error](matlab-plot-error) — line plot issues
- [Axis Error](matlab-axis-error) — axis limits
- [Figure Error](matlab-figure-error) — figure handles
