---
title: "[Solution] MATLAB imshow — Data Type, uint8/double Scaling, truesize"
description: "Fix MATLAB imshow errors: data type handling, uint8 vs double scaling, truesize display, and image format issues."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 136
---

## Common Causes

- `imshow` on double data outside [0, 1] range showing all white/black
- uint8 data not displaying correctly after conversion
- `truesize` not working on axes with multiple image objects
- Displaying grayscale image that's actually 3D (RGB)
- Using `imagesc` instead of `imshow` expecting auto-scaling

## How to Fix

```matlab
% WRONG: imshow on double data > 1 shows all white
data = rand(100) * 255;
imshow(data);  % All white — values outside [0,1] clipped

% CORRECT: Normalize data or specify range
data = rand(100) * 255;
imshow(data, []);             % Auto-scale to [min, max]
% Or normalize manually:
imshow(data / 255);           % Scale to [0, 1]
```

```matlab
% WRONG: Wrong data type for imshow
data = uint8(rand(100) * 255);
imshow(double(data) / 255);  % Works but unnecessary conversion

% CORRECT: Use native uint8 type
data = uint8(rand(100) * 255);
imshow(data);  % Correct: displays as expected
```

```matlab
% CORRECT: Display with specific display range
data = randn(100) * 10 + 128;
imshow(uint8(data));           % Clips to [0, 255]
imshow(data, [100 200]);       % Maps [100,200] to [0,1] for display
imshow(data, []);              % Maps [min,max] to [0,1]
```

```matlab
% CORRECT: Control image display size
figure;
h = imshow(data);
truesize(h, [200 200]);  % Display at 200x200 pixels
% Or proportional:
truesize(h, [size(data,1)/2, size(data,2)/2]);
```

```matlab
% CORRECT: imagesc vs imshow
figure;
subplot(1,2,1);
imagesc(rand(100));  % Auto-scales to data range, shows colorbar
title('imagesc');

subplot(1,2,2);
imshow(rand(100), []);  % No colorbar by default
title('imshow');
```

## Examples

```matlab
% Example: Display RGB image from matrix
img = zeros(100, 100, 3, 'uint8');
img(:,:,1) = uint8(linspace(0, 255, 100)');  % Red gradient
img(:,:,2) = uint8(linspace(255, 0, 100));   % Green gradient
img(:,:,3) = 128;

figure;
imshow(img);
title('RGB from matrix');
```

## Related Errors

- [Image Display](matlab-image-display) — display techniques
- [Plot Error](matlab-plot-error) — 2D visualization
- [Colormap](matlab-colormap) — color mapping for imagesc
