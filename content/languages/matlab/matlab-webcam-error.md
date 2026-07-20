---
title: "[Solution] MATLAB webcam Error — Preview, Snapshot, Resolution & Device"
description: "Fix MATLAB webcam errors for device not found, preview failures, resolution mismatch, and snapshot issues with code examples."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 104
---

The MATLAB `webcam` function from the Image Acquisition Toolbox connects to USB cameras, but errors occur when no device is detected, the resolution is unsupported, or the preview fails to start.

## Common Causes

- No webcam is connected or the driver is not installed
- Multiple applications are using the webcam simultaneously
- Requested resolution is not supported by the device
- The webcam object was cleared but code still references it
- Permission denied on Linux when accessing `/dev/video*`

## How to Fix

### Solution 1: List and select a webcam

```matlab
camList = webcamlist;
if isempty(camList)
    error('No webcams detected.');
end
disp('Available webcams:');
for i = 1:length(camList)
    fprintf('  %d: %s\n', i, camList{i});
end
cam = webcam(1);
```

### Solution 2: Configure resolution before preview

```matlab
cam = webcam();
disp(cam.AvailableResolutions);
cam.Resolution = '640x480';
preview(cam);
pause(5);
closePreview(cam);
```

### Solution 3: Take a snapshot safely

```matlab
cam = webcam();
cam.Resolution = '1280x720';
img = snapshot(cam);
imshow(img);
title('Webcam Snapshot');
clear cam;
```

### Solution 4: Record a short video from webcam

```matlab
cam = webcam();
cam.Resolution = '640x480';
outputVideo = VideoWriter('webcam_recording.mp4', 'MPEG-4');
outputVideo.FrameRate = 30;
open(outputVideo);

preview(cam);
pause(2);  % Let camera warm up

durationSec = 5;
framesToCapture = durationSec * outputVideo.FrameRate;

for i = 1:framesToCapture
    frame = snapshot(cam);
    writeVideo(outputVideo, frame);
end

close(outputVideo);
closePreview(cam);
clear cam;
disp('Recording saved.');
```

### Solution 5: Handle device busy errors

```matlab
try
    cam = webcam();
catch ME
    if contains(ME.message, 'busy') || contains(ME.message, 'in use')
        warning('Webcam is in use by another application. Closing other apps...');
        clear all;
        cam = webcam();
    else
        rethrow(ME);
    end
end
preview(cam);
```

## Examples

Continuous snapshot capture with timestamp:

```matlab
cam = webcam();
cam.Resolution = '640x480';

for i = 1:10
    img = snapshot(cam);
    filename = sprintf('snap_%s_%02d.jpg', datestr(now, 'HHMMSS'), i);
    imwrite(img, filename);
    pause(1);
end
clear cam;
disp('Snapshots captured.');
```

## Related Errors

- [MATLAB Arduino Error](matlab-arduino-error) — hardware device connection
- [MATLAB Serial Port Error](matlab-serial-port) — device communication
- [MATLAB Image Processing Error](matlab-image-processing-error) — image operations
