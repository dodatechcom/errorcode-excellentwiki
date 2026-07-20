---
title: "[Solution] MATLAB animation — animatedline/addpoints, drawnow, VideoWriter"
description: "Fix MATLAB animation errors: animatedline usage, drawnow rate limiting, VideoWriter frame timing, and performance."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 133
---

## Common Causes

- `drawnow` called too frequently causing sluggish animation
- VideoWriter frame rate mismatch with drawnow timing
- Not using `animatedline` for efficient line animations
- Forgetting to `open` VideoWriter before writing frames
- Memory exhaustion from accumulating too many points in animatedline

## How to Fix

```matlab
% WRONG: Plot in loop (slow, creates new graphics objects)
figure;
for k = 1:1000
    plot(rand, rand, 'o');  % Creates 1000 figure objects
    drawnow;
end

% CORRECT: Use animatedline for efficient line animation
h = animatedline('MaximumNumPoints', 100);
for k = 1:1000
    addpoints(h, k, sin(k*0.01));
    drawnow limitrate;  % Limit updates to ~20 fps
end
```

```matlab
% WRONG: VideoWriter without opening
vw = VideoWriter('output.avi');
writeVideo(vw, getframe(gcf));  % Error: file not open

% CORRECT: Open, write, close
vw = VideoWriter('output.avi');
vw.FrameRate = 30;
open(vw);
for k = 1:100
    drawnow;
    writeVideo(vw, getframe(gcf));
end
close(vw);
```

```matlab
% CORRECT: Controlled animation frame rate
figure;
h = animatedline;
axis([0 10 -1 1]);
startTime = tic;

for k = 1:500
    t = toc(startTime);
    addpoints(h, t, sin(2*pi*t));
    xlim([max(0, t-2), t]);  % Rolling window

    % Maintain target frame rate
    elapsed = toc(startTime);
    targetTime = k / 30;  % 30 fps
    if targetTime > elapsed
        pause(targetTime - elapsed);
    end
    drawnow;
end
```

```matlab
% CORRECT: Animated scatter plot
figure;
h = scatter([], [], 50, 'filled');
axis([0 1 0 1]);
for k = 1:200
    x = rand(1, 10);
    y = rand(1, 10);
    set(h, 'XData', x, 'YData', y, 'CData', rand(10, 3));
    drawnow limitrate;
end
```

```matlab
% CORRECT: Record animation to MP4
vw = VideoWriter('animation.mp4', 'MPEG-4');
vw.FrameRate = 60;
open(vw);

figure('Color', 'w');
h = animatedline('Color', 'b', 'LineWidth', 2);
axis([0 2*pi -1.5 1.5]);
grid on;

for k = 1:600
    t = k * 0.01;
    addpoints(h, t, sin(t));
    drawnow;
    writeVideo(vw, getframe(gcf));
end

close(vw);
```

## Examples

```matlab
% Example: Real-time data acquisition simulation
figure;
h = animatedline('MaximumNumPoints', 500, 'Color', 'r');
ax = gca;
ax.YLim = [-2 2];
xlabel('Time'); ylabel('Value');

for k = 1:1000
    val = sin(k*0.05) + 0.1*randn;
    addpoints(h, k*0.01, val);
    drawnow limitrate;
end
```

## Related Errors

- [Plot Error](matlab-plot-error) — line plotting basics
- [Figure Error](matlab-figure-error) — figure management
- [3D Plot](matlab-3d-plot) — 3D animation
