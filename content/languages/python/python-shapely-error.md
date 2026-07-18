---
title: "[Solution] Python Shapely Geometry Error — How to Fix"
description: "Fix Python Shapely geometry errors. Resolve invalid polygon, spatial operation failures, and coordinate system issues."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python Shapely Geometry Error

A `shapely.errors.TopologicalError` or `GEOSException` occurs when Shapely fails to construct valid geometries, encounters self-intersecting polygons, or performs spatial operations on incompatible geometries.

## Why It Happens

Shapely provides geometric operations using the GEOS library. Errors arise when polygon coordinates create self-intersecting rings, when spatial operations produce degenerate geometries, when coordinate types are incompatible, or when operations require valid but complex geometries.

## Common Error Messages

- `GEOSException: IllegalArgumentException: ...`
- `TopologicalError: self-intersection at or near point`
- `ShapelyDeprecationWarning: Iteration over multi-part geometries is deprecated`
- `ValueError: A线性Ring must have at least 3 coordinate tuples`

## How to Fix It

### Fix 1: Create valid geometries

```python
from shapely.geometry import Polygon, Point, LineString

# Wrong — self-intersecting polygon
# coords = [(0, 0), (2, 2), (2, 0), (0, 2), (0, 0)]
# poly = Polygon(coords)  # self-intersects

# Correct — use valid coordinate order
coords = [(0, 0), (2, 0), (2, 2), (0, 2), (0, 0)]
poly = Polygon(coords)
print(f"Valid polygon: {poly.is_valid}")
print(f"Area: {poly.area}")
```

### Fix 2: Fix self-intersecting polygons

```python
from shapely.geometry import Polygon
from shapely.validation import make_valid

# Wrong — self-intersecting polygon
# bowtie = Polygon([(0, 0), (2, 2), (2, 0), (0, 2)])
# bowtie.is_valid  # False

# Correct — use make_valid to fix
bowtie = Polygon([(0, 0), (2, 2), (2, 0), (0, 2)])
if not bowtie.is_valid:
    fixed = make_valid(bowtie)
    print(f"Fixed geometry type: {fixed.geom_type}")
    print(f"Is valid: {fixed.is_valid}")

# Or buffer(0) to fix minor issues
fixed2 = bowtie.buffer(0)
print(f"Buffer fix: {fixed2.is_valid}")
```

### Fix 3: Handle spatial operations

```python
from shapely.geometry import Polygon, Point

poly1 = Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])
poly2 = Polygon([(1, 1), (3, 1), (3, 3), (1, 3)])

# Wrong — intersection of non-overlapping polygons
# result = poly1.intersection(Polygon([(10, 10), (12, 10), (12, 12)]))

# Correct — check before operating
intersection = poly1.intersection(poly2)
if not intersection.is_empty:
    print(f"Intersection area: {intersection.area}")

# Use prepared geometries for repeated operations
from shapely.prepared import prep
prepared_poly = prep(poly1)
points = [Point(x, y) for x in range(5) for y in range(5)]
inside = [p for p in points if prepared_poly.contains(p)]
print(f"Points inside: {len(inside)}")
```

### Fix 4: Handle coordinate systems

```python
from shapely.geometry import Point, LineString

# Wrong — mixing coordinate systems
# p1 = Point(1.0, 2.0)        # WGS84
# p2 = Point(500000, 4000000)  # UTM
# distance = p1.distance(p2)   # meaningless

# Correct — ensure consistent CRS
p1_utm = Point(500000, 4000000)
p2_utm = Point(500100, 4000100)
distance = p1_utm.distance(p2_utm)
print(f"Distance in meters: {distance:.2f}")

# Validate coordinates are in expected range
def validate_wgs84(lon, lat):
    if not (-180 <= lon <= 180):
        raise ValueError(f"Invalid longitude: {lon}")
    if not (-90 <= lat <= 90):
        raise ValueError(f"Invalid latitude: {lat}")
    return True

validate_wgs84(74.006, 40.7128)
```

## Common Scenarios

- **Self-intersecting polygon** — Bowtie shapes or crossing edges cause TopologicalError during spatial operations.
- **Empty intersection** — Non-overlapping geometries produce empty intersection results.
- **CRS mismatch** — Mixing WGS84 (lat/lon) coordinates with projected coordinates produces meaningless distances.

## Prevent It

- Always check `geometry.is_valid` after constructing complex polygons.
- Use `make_valid()` or `buffer(0)` to fix minor validity issues before spatial operations.
- Verify coordinate reference systems are consistent before computing distances or intersections.

## Related Errors

- [GEOSException](/languages/python/geos-error/) — GEOS library operation failed
- [TopologicalError](/languages/python/topological-error/) — geometry self-intersection
- [ValueError](/languages/python/valueerror/) — invalid coordinate values
