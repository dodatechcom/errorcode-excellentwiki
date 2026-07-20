---
title: "[Solution] MATLAB plot() — Vector Length, hold on/off, Figure Management"
description: "Fix MATLAB plot errors: vector length mismatch, hold on/off state, figure management, and line specifications."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 127
---

## Common Causes

- X and Y vectors have different lengths
- `hold off` clearing previous plots unexpectedly
- Plotting with NaN causing gaps or warnings
- Mixing 2D and 3D plot commands on same axes
- Using `plot` on complex data without specifying real/imag parts

## How to Fix

```matlab
% WRONG: Mismatched vector lengths
x = 1:10;
y = 1:5;
plot(x, y);  % Error: Vectors must be the same length

% CORRECT: Match dimensions
x = 1:5;
y = 1:5;
plot(x, y);
% Or use linspace
x = linspace(0, 1, 5);
y = sin(2*pi*x);
plot(x, y);
```

```matlab
% WRONG: hold off clearing previous plots
figure;
plot(1:10, rand(10,1));
plot(1:10, rand(10,1));  % First plot is gone

% CORRECT: Use hold on to preserve plots
figure;
plot(1:10, rand(10,1), 'b-');
hold on;
plot(1:10, rand(10,1), 'r--');
hold off;
```

```matlab
% CORRECT: Handle NaN in data
x = [1 2 NaN 4 5];
y = [1 2 3 4 5];
plot(x, y, '-o');  % NaN creates a gap — usually desired behavior
```

```matlab
% CORRECT: Plot complex data properly
z = 1 + 1i*linspace(0, 2*pi, 100);
plot(real(z), imag(z));  % Plot in complex plane

% Or use plot with complex input (plots real vs imag automatically)
plot(z);
```

```matlab
% CORRECT: Multiple data series with legend
figure;
t = linspace(0, 2*pi, 100);
plot(t, sin(t), 'b-', 'LineWidth', 1.5);
hold on;
plot(t, cos(t), 'r--', 'LineWidth', 1.5);
plot(t, sin(2*t), 'g:', 'LineWidth', 2);
legend('sin', 'cos', 'sin(2x)');
xlabel('x'); ylabel('y');
title('Trigonometric Functions');
grid on;
hold off;
```

## Examples

```matlab
% Example: Animated plot with hold
figure;
x = linspace(0, 2*pi, 100);
y = sin(x);
h = plot(x, y, 'b-', 'LineWidth', 2);
hold on;
for k = 1:50
    y_shifted = sin(x - k*0.05);
    set(h, 'YData', y_shifted);
    drawnow limitrate;
end
hold off;
```

## Related Errors

- [Subplot](matlab-subplot) — layout management
- [Figure Error](matlab-figure-error) — figure handle issues
- [Axis Error](matlab-axis-error) — axis limits
