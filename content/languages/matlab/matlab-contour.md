---
title: "[Solution] MATLAB contour/contourf — Levels, Z Data, clabel, LabelSpacing"
description: "Fix MATLAB contour errors: contour level specification, Z data format, clabel placement, and LabelSpacing settings."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 135
---

## Common Causes

- Z data not a matrix for `contour`/`contourf`
- Incorrect contour level specification (scalar vs vector)
- `clabel` crashing on contours with zero-length paths
- `LabelSpacing` too small causing overlapping labels
- Using `contour` on scattered data without grid interpolation

## How to Fix

```matlab
% WRONG: Contour with vector Z data
x = 1:10;
y = 1:10;
z = rand(1, 100);  % Vector — error
contour(x, y, z);

% CORRECT: Z must be a 2D matrix
[X, Y] = meshgrid(1:10, 1:10);
Z = rand(10, 10);
contour(X, Y, Z);
```

```matlab
% WRONG: Scalar level gives single contour
contour(Z, 5);  % Request 5 levels, not 1 level at value 5

% CORRECT: Use vector for specific levels
contour(Z, [0.2 0.4 0.6 0.8]);  % Specific contour levels
% Or number of levels:
contour(Z, 10);  % 10 auto-selected levels
```

```matlab
% CORRECT: clabel with proper spacing
[C, h] = contour(Z, 10);
clabel(C, h, 'LabelSpacing', 500, 'FontSize', 10);
```

```matlab
% CORRECT: contourf with colorbar
figure;
contourf(X, Y, Z, 20);
colorbar;
xlabel('X'); ylabel('Y');
title('Filled Contour Plot');
```

```matlab
% CORRECT: Contour from scattered data
x = rand(1000, 1) * 10;
y = rand(1000, 1) * 10;
z = sin(x) + cos(y);

[Xgrid, Ygrid] = meshgrid(linspace(0, 10, 100));
Zgrid = griddata(x, y, z, Xgrid, Ygrid, 'cubic');
contour(Xgrid, Ygrid, Zgrid, 15);
```

## Examples

```matlab
% Example: Publication-quality contour
[X, Y, Z] = peaks(200);
figure('Color', 'w');
contourf(X, Y, Z, 20, 'LineColor', 'none');
colormap(parula);
colorbar('Label', 'Amplitude');
clim([-8 8]);
xlabel('X'); ylabel('Y');
title('Peaks Function Contour');
```

## Related Errors

- [3D Plot](matlab-3d-plot) — surface/mesh plots
- [Colormap](matlab-colormap) — color mapping
- [Image Display](matlab-image-display) — image visualization
