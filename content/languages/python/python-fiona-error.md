---
title: "[Solution] Python Fiona Geospatial File Error — How to Fix"
description: "Fix Python Fiona geospatial file errors. Resolve shapefile reading failures, driver issues, and CRS projection errors."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python Fiona Geospatial File Error

A `fiona.errors.FionaError` or `DriverError` occurs when Fiona fails to open geospatial files due to missing GDAL drivers, incompatible file formats, or when coordinate reference system transformations fail.

## Why It Happens

Fiona reads and writes geospatial vector files using GDAL/OGR. Errors arise when the file format driver is not available, when the shapefile has corrupt .dbf files, when CRS information is missing or incompatible, or when field types do not match the data.

## Common Error Messages

- `DriverError: driver not found`
- `FionaError: Collection could not be opened`
- `CRSError: Invalid CRS`
- `DriverSupportError: Driver not supported`

## How to Fix It

### Fix 1: Check available drivers

```python
import fiona

# Wrong — assuming driver is available
# collection = fiona.open("data.shp", driver="GeoJSON")

# Correct — check drivers first
print(fiona.supported_drivers)

# Open with explicit driver
collection = fiona.open(
    "data.shp",
    driver="ESRI Shapefile",
    encoding="utf-8",
)
print(f"Feature count: {len(collection)}")
collection.close()
```

### Fix 2: Handle CRS issues

```python
import fiona
from fiona.crs import from_epsg

# Wrong — writing without CRS
# with fiona.open("output.shp", "w", schema=schema) as dst:
#     dst.write(feature)

# Correct — set CRS properly
schema = {
    "geometry": "Point",
    "properties": {"name": "str", "value": "float"},
}

with fiona.open(
    "output.shp",
    "w",
    driver="ESRI Shapefile",
    schema=schema,
    crs=from_epsg(4326),  # WGS84
) as dst:
    feature = {
        "geometry": {"type": "Point", "coordinates": [0, 0]},
        "properties": {"name": "test", "value": 1.0},
    }
    dst.write(feature)
```

### Fix 3: Read shapefiles with encoding

```python
import fiona

# Wrong — default encoding may miss characters
# collection = fiona.open("data.shp")

# Correct — specify encoding
collection = fiona.open(
    "data.shp",
    encoding="utf-8",
    layer="layer_name",
)

for feature in collection:
    props = feature["properties"]
    geom = feature["geometry"]
    print(f"{props['name']}: {geom}")

collection.close()
```

### Fix 4: Handle field type mismatches

```python
import fiona
from fiona import Field

# Wrong — field type mismatch
# schema = {"geometry": "Polygon", "properties": {"id": "int"}}
# data has string in "id" field

# Correct — match schema to actual data types
schema = {
    "geometry": "Polygon",
    "properties": {
        "id": "str",  # match actual data type
        "area": "float",
        "name": "str",
    },
}

with fiona.open("output.shp", "w", driver="ESRI Shapefile", schema=schema) as dst:
    feature = {
        "geometry": {
            "type": "Polygon",
            "coordinates": [[(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]],
        },
        "properties": {"id": "001", "area": 1.0, "name": "Zone A"},
    }
    dst.write(feature)
```

## Common Scenarios

- **Missing GDAL driver** — The target file format (e.g., GeoPackage) requires a GDAL driver not compiled into the Fiona installation.
- **Corrupt shapefile** — Missing .shx or .dbf sidecar files prevent opening the shapefile.
- **CRS undefined** — Files written without CRS metadata cannot be reprojected.

## Prevent It

- Always specify `encoding="utf-8"` when reading shapefiles to avoid character encoding issues.
- Use `fiona.supported_drivers` to verify driver availability before attempting to open files.
- Write CRS information explicitly using `from_epsg()` or WKT strings.

## Related Errors

- [DriverError](/languages/python/driver-error/) — GDAL driver not available
- [CRSError](/languages/python/crs-error/) — invalid coordinate reference system
- [FionaError](/languages/python/fiona-error/) — file cannot be opened
