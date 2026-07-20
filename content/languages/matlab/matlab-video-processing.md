---
title: "[Solution] MATLAB Video Processing Error — VideoFileReader & Optical Flow"
description: "Fix MATLAB vision.VideoFileReader and opticalFlow errors for video reading, optical flow computation, and frame processing with code examples."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 133
---

MATLAB's Computer Vision Toolbox video processing functions (`vision.VideoFileReader`, `opticalFlowLK`, `opticalFlowHS`) can fail when the video format is unsupported, the flow parameters are inappropriate, or frame dimensions change mid-stream.

## Common Causes

- Video codec is not installed on the system
- Optical flow `MemoryBlockSize` is too large for available RAM
- Video frame rate is inconsistent, causing sync issues
- `vision.VideoFileReader` output is not properly released
- Flow estimation fails on frames with very low contrast

## How to Fix

### Solution 1: Read video with VideoFileReader

```matlab
videoReader = vision.VideoFileReader('clip.mp4');
while ~isDone(videoReader)
    frame = videoReader();
    imshow(frame);
    drawnow;
end
release(videoReader);
```

### Solution 2: Lucas-Kanade optical flow

```matlab
videoReader = vision.VideoFileReader('traffic.mp4');
flow = opticalFlowLK('NumPyramidLevels', 4);
while ~isDone(videoReader)
    frame = videoReader();
    grayFrame = rgb2gray(frame);
    flowEstimate = estimateFlow(flow, grayFrame);
    figure(1); imshow(frame); hold on;
    plot(flowEstimate, 'DecimationFactor', [5 5], 'ScaleFactor', 20);
    hold off; drawnow;
end
release(videoReader);
```

### Solution 3: Horn-Schunck optical flow

```matlab
flow = opticalFlowHS('MaxIteration', 100, 'Smoothness', 1);
flowEstimate = estimateFlow(flow, rgb2gray(frame));
speed = sqrt(flowEstimate.Vx.^2 + flowEstimate.Vy.^2);
imshow(speed, []);
title('Optical Flow Speed');
```

### Solution 4: Save processed video

```matlab
videoReader = vision.VideoFileReader('input.mp4');
videoWriter = vision.VideoFileWriter('output.avi', 'FrameRate', 30);
while ~isDone(videoReader)
    frame = videoReader();
    gray = rgb2gray(frame);
    edges = edge(gray, 'Canny');
    outputFrame = repmat(uint8(edges)*255, [1 1 3]);
    videoWriter(outputFrame);
end
release(videoReader);
release(videoWriter);
```

### Solution 5: Background subtraction

```matlab
videoReader = vision.VideoFileReader('surveillance.mp4');
blobDetector = vision.BlobAnalysis('MinimumBlobArea', 500);
backgroundSubtractor = vision.ForegroundDetector('NumTrainingFrames', 20);
while ~isDone(videoReader)
    frame = videoReader();
    fgMask = backgroundSubtractor(frame);
    [area, centroid, bbox] = blobDetector(fgMask);
    annotatedFrame = insertShape(frame, 'Rectangle', bbox);
    imshow(annotatedFrame);
    drawnow;
end
release(videoReader);
```

## Examples

Detect motion direction from optical flow:

```matlab
videoReader = vision.VideoFileReader('walking.mp4');
flow = opticalFlowLK;
prevVx = 0;
while ~isDone(videoReader)
    frame = videoReader();
    grayFrame = rgb2gray(frame);
    flowEst = estimateFlow(flow, grayFrame);
    meanVx = mean(flowEst.Vx(:));
    if meanVx > 0.5
        disp('Moving right');
    elseif meanVx < -0.5
        disp('Moving left');
    end
end
release(videoReader);
```

## Related Errors

- [MATLAB VideoReader Error](matlab-videoreader) — VideoReader/VideoWriter codec
- [MATLAB Computer Vision Error](matlab-computer-vision) — feature detection
- [MATLAB Image Filter Error](matlab-image-filter) — spatial filtering
