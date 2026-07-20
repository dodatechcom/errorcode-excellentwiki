---
title: "[Solution] MATLAB VideoReader/VideoWriter Error — Codec, Frame Rate & Resolution"
description: "Fix MATLAB VideoReader and VideoWriter errors for unsupported codecs, frame rate mismatches, and resolution issues with code examples."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 103
---

MATLAB's `VideoReader` and `VideoWriter` can fail when the video codec is not installed, the frame rate is inconsistent, or the output resolution does not match the input.

## Common Causes

- The video file uses a codec not available on the system (e.g., H.265/HEVC)
- Reading frames beyond the actual number of frames in the video
- `VideoWriter` profile does not match the desired output format
- Frame rate passed to `VideoWriter` does not match the source video
- Attempting to read a video file that is locked by another process

## How to Fix

### Solution 1: Check codec availability and video properties

```matlab
v = VideoReader('clip.mp4');
disp(['Format: ', v.VideoFormat]);
disp(['Resolution: ', num2str(v.Width), 'x', num2str(v.Height)]);
disp(['Frame rate: ', num2str(v.FrameRate), ' fps']);
disp(['NumFrames: ', num2str(v.NumFrames)]);
disp(['Duration: ', num2str(v.Duration), ' s']);
```

### Solution 2: Read and write video with matching parameters

```matlab
src = VideoReader('input.mp4');
dst = VideoWriter('output.avi', 'Motion JPEG AVI');
dst.FrameRate = src.FrameRate;
open(dst);

while hasFrame(src)
    frame = readFrame(src);
    writeVideo(dst, frame);
end
close(dst);
```

### Solution 3: Extract specific frames safely

```matlab
v = VideoReader('clip.mp4');
targetFrame = 30;
if targetFrame > v.NumFrames
    targetFrame = v.NumFrames;
    warning('Requested frame exceeds total; using last frame.');
end
v.CurrentTime = (targetFrame - 1) / v.FrameRate;
frame = readFrame(v);
imshow(frame);
title(sprintf('Frame %d', targetFrame));
```

### Solution 4: Resize frames during writing

```matlab
src = VideoReader('input.mp4');
dst = VideoWriter('resized_output.mp4', 'MPEG-4');
dst.FrameRate = src.FrameRate;
open(dst);

targetW = 640;
targetH = 480;

while hasFrame(src)
    frame = readFrame(src);
    resizedFrame = imresize(frame, [targetH, targetW]);
    writeVideo(dst, resizedFrame);
end
close(dst);
```

### Solution 5: Write a grayscale video

```matlab
src = VideoReader('color_input.mp4');
dst = VideoWriter('grayscale_output.avi', 'Grayscale AVI');
dst.FrameRate = src.FrameRate;
open(dst);

while hasFrame(src)
    frame = readFrame(src);
    grayFrame = rgb2gray(frame);
    writeVideo(dst, grayFrame);
end
close(dst);
```

## Examples

Create a video from a sequence of images:

```matlab
imageFiles = dir('frames/*.png');
dst = VideoWriter('reconstructed.mp4', 'MPEG-4');
dst.FrameRate = 30;
open(dst);

for i = 1:length(imageFiles)
    img = imread(fullfile(imageFiles(i).folder, imageFiles(i).name));
    writeVideo(dst, img);
end
close(dst);
disp('Video created successfully.');
```

## Related Errors

- [MATLAB audioread/audiowrite Error](matlab-audioread-error) — audio file I/O
- [MATLAB Video Processing Error](matlab-video-processing) — computer vision video analysis
- [MATLAB Image Transform Error](matlab-image-transform) — image resizing and rotation
