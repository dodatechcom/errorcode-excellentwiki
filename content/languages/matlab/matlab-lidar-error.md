---
title: "[Solution] MATLAB Lidar Point Cloud Error — pcshow, pcread & pcdenoise"
description: "Fix MATLAB lidar point cloud errors for pcshow visualization, pcread file issues, and pcdenoise filtering with code examples."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 131
---

MATLAB's lidar and point cloud functions (`pcshow`, `pcread`, `pcdenoise`) can fail when the point cloud file is malformed, the data contains too few points, or the noise removal parameters are too aggressive.

## Common Causes

- Point cloud file (`.pcd`, `.ply`) is corrupted or has unsupported format
- `pcdenoise` threshold removes nearly all points
- `pcshow` receives a point cloud with no valid coordinates (all NaN)
- Point cloud has more than 3 columns but only 3 are expected
- Memory issues with very large point clouds (millions of points)

## How to Fix

### Solution 1: Read and inspect a point cloud

```matlab
ptCloud = pcread('scan.pcd');
disp(['Number of points: ', num2str(ptCloud.Count)]);
disp(['Point cloud format: ', ptCloud.Properties.DataType]);
```

### Solution 2: Denoise a point cloud

```matlab
ptCloud = pcread('scan.pcd');
cleanCloud = pcdenoise(ptCloud, 'NumNeighbors', 20, 'Threshold', 0.5);
fprintf('Removed %d points\n', ptCloud.Count - cleanCloud.Count);
pcshow(cleanCloud);
title('Denoised Point Cloud');
```

### Solution 3: Downsample before processing

```matlab
ptCloud = pcread('large_scan.pcd');
dsCloud = pcdownsample(ptCloud, 'random', 0.1);  % Keep 10%
fprintf('Downsampled to %d points\n', dsCloud.Count);
pcshow(dsCloud);
```

### Solution 4: Create point cloud from XYZ data

```matlab
xyz = randn(1000, 3);
rgb = uint8(255 * rand(1000, 3));
ptCloud = pointCloud(xyz, 'Color', rgb);
pcshow(ptCloud);
title('Random Point Cloud');
```

### Solution 5: Merge multiple point clouds

```matlab
ptCloud1 = pcread('scan1.pcd');
ptCloud2 = pcread('scan2.pcd');
merged = pcmerge(ptCloud1, ptCloud2, 0.01);
pcshow(merged);
title('Merged Point Cloud');
```

## Examples

Segment ground plane from point cloud:

```matlab
ptCloud = pcread('outdoor_scan.pcd');
maxDistance = 0.5;
referenceVector = [0 0 1];
[labeledPtCloud, inlierIdx] = pcfitplane(ptCloud, maxDistance, referenceVector, 0.1);
ground = select(ptCloud, inlierIdx);
objects = select(ptCloud, ~inlierIdx);
pcshow(objects);
title('Ground Removed');
```

## Related Errors

- [MATLAB Computer Vision Error](matlab-computer-vision) — feature detection and matching
- [MATLAB Image Processing Error](matlab-image-processing-error) — 2D image operations
- [MATLAB Image Segmentation Error](matlab-image-segmentation) — segmentation methods
