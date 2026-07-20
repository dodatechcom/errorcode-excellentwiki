---
title: "[Solution] Redis Geospatial Command Error"
description: "How to fix Redis geospatial command errors"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Invalid longitude/latitude values
- GEOADD with wrong number of arguments
- GEOSEARCH with invalid parameters

## Fix

Verify coordinates:

```bash
# Longitude: -180 to 180, Latitude: -85 to 85
redis-cli GEOADD locations 2.3522 48.8566 "Paris"
```

Search within radius:

```bash
redis-cli GEORADIUS locations 2.3522 48.8566 100 km
```

Get distance between points:

```bash
redis-cli GEODIST locations "Paris" "London" km
```

## Examples

```bash
# Add location
redis-cli GEOADD locations 2.3522 48.8566 "Paris"
redis-cli GEOADD locations -0.1278 51.5074 "London"

# Search nearby
redis-cli GEORADIUS locations 2.3522 48.8566 500 km WITHCOORD

# Get distance
redis-cli GEODIST locations "Paris" "London" km
```
