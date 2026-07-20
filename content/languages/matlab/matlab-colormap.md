---
title: "[Solution] MATLAB colormap — Length, RGB Triple, caxis/clim, Colorbar"
description: "Fix MATLAB colormap errors: colormap length, RGB triple format, caxis/clim limits, and colorbar display."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 132
---

## Common Causes

- Colormap length not matching data range (256 vs 64 entries)
- Passing non-RGB data to colormap function
- caxis/clim limits hiding data outside range
- Colorbar not updating after colormap change
- Using old `caxis` instead of `clim` (R2022a+)

## How to Fix

```matlab
% WRONG: Colormap with wrong number of colors
colormap(lines(5));  % Only 5 colors for imagesc with 256 values

% CORRECT: Match colormap length to data resolution
colormap(lines(256));  % Full resolution colormap
% Or use built-in:
colormap(jet(256));
```

```matlab
% WRONG: caxis hiding data
imagesc(rand(100));
caxis([0.3 0.7]);  % Values outside [0.3, 0.7] are clipped

% CORRECT: Use clim to set proper limits (R2022a+)
imagesc(rand(100));
clim([0 1]);  % Full range
% Or auto:
clim('auto');
```

```matlab
% CORRECT: Custom colormap from RGB triplets
cmap = [
    0 0 1;    % Blue
    0 1 0;    % Green
    1 1 0;    % Yellow
    1 0 0     % Red
];
colormap(interp1(linspace(0,1,size(cmap,1)), cmap, linspace(0,1,256)));
```

```matlab
% CORRECT: Colorbar with proper labeling
figure;
h = imagesc(peaks(100));
colormap(parula);
cb = colorbar;
cb.Label.String = 'Amplitude';
cb.Label.FontSize = 12;
clim([-8 8]);
```

```matlab
% CORRECT: Create and apply custom colormap
function applyCustomCmap(hAxes, lowColor, highColor, n)
    if nargin < 4, n = 256; end
    cmap = [linspace(lowColor(1), highColor(1), n)', ...
            linspace(lowColor(2), highColor(2), n)', ...
            linspace(lowColor(3), highColor(3), n)'];
    colormap(hAxes, cmap);
end

% Usage:
ax = axes;
imagesc(ax, peaks);
applyCustomCmap(ax, [0 0 0.5], [1 1 0]);
```

## Examples

```matlab
% Example: Diverging colormap centered at zero
data = peaks(200);
figure;
imagesc(data);
colormap(redblue(256));  % Assuming redblue is available
clim([-8 8]);
colorbar;
title('Diverging Colormap');
```

## Related Errors

- [Image Display](matlab-image-display) — imagesc/imshow
- [3D Plot](matlab-3d-plot) — surface coloring
- [Contour](matlab-contour) — contour coloring
