---
title: "[Solution] Python Rasterio Raster Data Error — How to Fix"
description: "Fix Python Rasterio raster data errors. Resolve band reading failures, CRS issues, and georeferencing problems."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python Rasterio Raster Data Error

A `rasterio.errors.RasterioError` or `CRSError` occurs when Rasterio fails to read raster bands, encounters incompatible CRS definitions, or when georeferencing transforms are invalid.

## Why It Happens

Rasterio reads and writes geospatial raster data using GDAL. Errors arise when band indices are out of range, when the raster file is corrupt, when CRS cannot be determined, when the data type does not match the read operation, or when window parameters exceed the raster bounds.

## Common Error Messages

- `RasterioError: band index out of range`
- `CRSError: The WKT could not be parsed`
- `RasterioError: not a rasterio dataset`
- `ValueError: math domain error`

## How to Fix It

### Fix 1: Read bands correctly

```python
import rasterio

# Wrong — band index out of range
# with rasterio.open("data.tif") as src:
#     band = src.read(4)  # only 3 bands available

# Correct — check band count first
with rasterio.open("data.tif") as src:
    print(f"Band count: {src.count}")
    print(f"CRS: {src.crs}")
    print(f"Bounds: {src.bounds}")

    # Read specific bands
    red = src.read(1)
    green = src.read(2)
    blue = src.read(3)

    # Read as RGB composite
    rgb = src.read([1, 2, 3])
    print(f"RGB shape: {rgb.shape}")
```

### Fix 2: Handle CRS and transforms

```python
import rasterio
from rasterio.transform import from_bounds

# Wrong — missing CRS information
# data = rasterio.open("data.tif")
# reprojected = ...  # cannot reproject without CRS

# Correct — set CRS and transform
with rasterio.open(
    "output.tif",
    "w",
    driver="GTiff",
    height=100,
    width=100,
    count=1,
    dtype="float32",
    crs="EPSG:4326",
    transform=from_bounds(0, 0, 1, 1, 100, 100),
) as dst:
    import numpy as np
    data = np.random.rand(100, 100).astype("float32")
    dst.write(data, 1)
```

### Fix 3: Read windows of large rasters

```python
import rasterio
from rasterio.windows import Window

# Wrong — reading entire large raster into memory
# with rasterio.open("huge.tif") as src:
#     data = src.read()

# Correct — read specific windows
with rasterio.open("huge.tif") as src:
    # Read a 256x256 window
    window = Window(0, 0, 256, 256)
    data = src.read(1, window=window)
    print(f"Window shape: {data.shape}")

    # Read with downsampling
    data_downsampled = src.read(
        1,
        window=Window(0, 0, 1024, 1024),
        out_shape=(256, 256),
    )
```

### Fix 4: Write raster data correctly

```python
import rasterio
import numpy as np

# Wrong — wrong data shape
# with rasterio.open("output.tif", "w", ...) as dst:
#     dst.write(array_1d, 1)  # need 2D array

# Correct — match shape to band dimensions
with rasterio.open(
    "output.tif",
    "w",
    driver="GTiff",
    height=100,
    width=100,
    count=3,
    dtype="uint8",
    crs="EPSG:4326",
) as dst:
    # Write each band
    for i in range(3):
        band = np.random.randint(0, 255, (100, 100), dtype="uint8")
        dst.write(band, i + 1)

    # Or write all bands at once
    rgb = np.random.randint(0, 255, (3, 100, 100), dtype="uint8")
    dst.write(rgb)
```

## Common Scenarios

- **Band index error** — Attempting to read band 4 from a 3-band RGB raster.
- **CRS undefined** — Raster files without CRS metadata cannot be reprojected or overlaid.
- **Memory overflow** — Reading entire large rasters (multi-GB) without windowed reading.

## Prevent It

- Always check `src.count`, `src.dtypes`, and `src.crs` before reading specific bands.
- Use windowed reading with `rasterio.windows.Window` for files larger than available RAM.
- Set explicit CRS using EPSG codes when writing new raster files.

## Related Errors

- [CRSError](/languages/python/crs-error/) — coordinate reference system error
- [RasterioError](/languages/python/rasterio-error/) — raster operation failed
- [MemoryError](/languages/python/memoryerror/) — raster too large for memory
