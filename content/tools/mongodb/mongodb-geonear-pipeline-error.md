---
title: "[Solution] MongoDB $geoNear Pipeline Error"
description: "Fix MongoDB $geoNear pipeline error when geospatial queries fail due to missing indexes or invalid coordinates"
tools: ["mongodb"]
error-types: ["tool-error"]
severities: ["error"]
---

# MongoDB $geoNear Pipeline Error

The $geoNear aggregation stage fails when the collection lacks a geospatial index, coordinates are invalid, or distance parameters are misconfigured.

## Common Causes

- No 2dsphere or 2d index exists on the location field
- Coordinates are outside valid longitude/latitude ranges
- $geoNear is not the first stage in the pipeline
- maxDistance or minDistance values are invalid
- Near parameter format does not match the index type

## How to Fix

### Create a Geospatial Index

```javascript
// For GeoJSON data (recommended)
db.collection('stores').createIndex({ location: '2dsphere' })

// For legacy coordinate pairs
db.collection('stores').createIndex({ location: '2d' })
```

### Use Correct $geoNear Format

```javascript
db.collection('stores').aggregate([
  {
    $geoNear: {
      near: { type: 'Point', coordinates: [-73.99279, 40.719296] },
      distanceField: 'distance',
      maxDistance: 5000,      // 5km in meters
      minDistance: 100,       // 100m minimum
      spherical: true,
      key: 'location'
    }
  },
  { $limit: 10 },
  { $project: { name: 1, distance: 1 } }
])
```

### Validate Coordinates

```javascript
function validateCoordinates(lon, lat) {
  if (lon < -180 || lon > 180) {
    throw new Error(`Invalid longitude: ${lon}`);
  }
  if (lat < -90 || lat > 90) {
    throw new Error(`Invalid latitude: ${lat}`);
  }
  return true;
}

validateCoordinates(-73.99279, 40.719296);
```

### Ensure $geoNear Is First Stage

```javascript
// Correct: $geoNear is first
db.collection('stores').aggregate([
  { $geoNear: { near: {...}, distanceField: 'dist' } },
  { $match: { category: 'restaurant' } }
])

// Wrong: $match before $geoNear
// This will fail
db.collection('stores').aggregate([
  { $match: { category: 'restaurant' } },
  { $geoNear: { near: {...}, distanceField: 'dist' } }
])
```

## Examples

```
MongoServerError: $geoNear requires a 2dsphere or 2d index on
  the location field of collection "stores"

MongoServerError: $geoNear: coordinates must be [longitude, latitude]
  Got [91.0, -181.0] which is outside valid range

MongoServerError: $geoNear is not the first stage in the pipeline.
  Move $geoNear to the beginning of the aggregation.
```

## Related Errors

- [MongoDB Geospatial Index Error]({{< relref "/tools/mongodb/mongodb-geospatial-index-error" >}}) -- index issues
- [MongoDB GeoNear Syntax Error]({{< relref "/tools/mongodb/mongodb-geonear-syntax-error" >}}) -- syntax issues
- [MongoDB Index Not Found]({{< relref "/tools/mongodb/mongodb-index-not-found" >}}) -- missing index
