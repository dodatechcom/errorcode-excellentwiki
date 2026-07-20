---
title: "[Solution] MATLAB 3D Plot — plot3/surf/mesh/meshgrid, Z Matrix, NaN"
description: "Fix MATLAB 3D plot errors: meshgrid sizing, surf Z matrix requirements, plot3 vector dimensions, and NaN handling."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 134
---

## Common Causes

- `Z` not a matrix for `surf`/`mesh` (must be 2D)
- `meshgrid` output dimensions not matching Z
- `plot3` vectors not same length
- Using `surf` without `shading interp` on non-gridded data
- NaN in surface data causing rendering gaps

## How to Fix

```matlab
% WRONG: surf expects Z as matrix, not vector
x = 1:10;
y = 1:10;
z = rand(10, 1);  % Vector — error
surf(x, y, z);

% CORRECT: Use meshgrid for proper 2D grid
[X, Y] = meshgrid(1:10, 1:10);
Z = rand(10, 10);
surf(X, Y, Z);
```

```matlab
% WRONG: meshgrid dimensions don't match Z
[X, Y] = meshgrid(1:5, 1:10);  % 10x5
Z = rand(3, 3);                 % 3x3 — error
surf(X, Y, Z);

% CORRECT: Match all dimensions
[X, Y] = meshgrid(1:5, 1:5);
Z = rand(5, 5);
surf(X, Y, Z);
```

```matlab
% CORRECT: plot3 with same-length vectors
x = 1:100;
y = sin(x);
z = cos(x);
plot3(x, y, z, 'b-', 'LineWidth', 2);
xlabel('X'); ylabel('Y'); zlabel('Z');
grid on;
```

```matlab
% CORRECT: Handle NaN in surface data
Z = peaks(20);
Z(Z < -4) = NaN;  % Creates holes in surface
figure;
surf(X, Y, Z);
shading interp;  % Smooths NaN boundaries
```

```matlab
% CORRECT: meshgrid vs ndgrid
[X, Y] = meshgrid(1:5, 1:3);  % X is 3x5, Y is 3x5
% X varies along columns (dim 2)
% Y varies along rows (dim 1)

[X2, Y2] = ndgrid(1:5, 1:3);  % X2 is 5x3, Y2 is 5x3
% X2 varies along rows (dim 1)
% Y2 varies along columns (dim 2)
```

## Examples

```matlab
% Example: 3D parametric surface
t = linspace(0, 2*pi, 100);
[u, v] = meshgrid(t);
x = (1 + 0.5*cos(v)) .* cos(u);
y = (1 + 0.5*cos(v)) .* sin(u);
z = 0.5 * sin(v);

figure;
surf(x, y, z);
axis equal; shading interp;
colormap(hsv);
```

## Related Errors

- [Plot Error](matlab-plot-error) — 2D plotting
- [Contour](matlab-contour) — contour plots
- [Colormap](matlab-colormap) — color mapping
