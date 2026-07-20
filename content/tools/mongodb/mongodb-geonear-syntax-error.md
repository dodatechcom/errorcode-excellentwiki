---
title: "[Solution] MongoDB $geoNear Syntax Error"
description: "Fix MongoDB $geoNear aggregation stage syntax errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB $geoNear Syntax Error

The `$geoNear` stage has strict syntax requirements:

```
MongoServerError: $geoNear requires that 'near' is a GeoJSON point
```

```
MongoServerError: $geoNear requires 'distanceField' to be specified
```

## Common Causes

- Missing required fields (`near`, `distanceField`)
- The `near` value is not a valid GeoJSON point
- Using `$geoNear` without a `2dsphere` index
- Mixing `maxDistance` and `minDistance` incorrectly
- The `key` field references a non-indexed field

## How to Fix

### 1. Include all required fields

```javascript
db.places.aggregate([
  {
    $geoNear: {
      near: { type: "Point", coordinates: [-73.97, 40.78] },
      distanceField: "distance",
      maxDistance: 5000,
      query: { type: "park" },
      spherical: true
    }
  }
]);
```

### 2. Ensure a 2dsphere index exists

```javascript
db.places.createIndex({ location: "2dsphere" });
```

### 3. Use the correct distanceField output

```javascript
db.places.aggregate([
  {
    $geoNear: {
      near: { type: "Point", coordinates: [-73.97, 40.78] },
      distanceField: "distFromCenter",
      maxDistance: 10000,
      spherical: true
    }
  },
  { $sort: { distFromCenter: 1 } },
  { $limit: 10 }
]);
```

## Examples

```bash
# Create geospatial collection with correct setup
mongosh --eval '
  db.places.drop();
  db.places.createIndex({location:"2dsphere"});
  db.places.insertMany([
    {name:"Library", location:{type:"Point",coordinates:[-73.97,40.78]}, type:"building"},
    {name:"Park", location:{type:"Point",coordinates:[-73.96,40.79]}, type:"park"},
    {name:"Cafe", location:{type:"Point",coordinates:[-73.98,40.77]}, type:"restaurant"}
  ]);

  let result = db.places.aggregate([
    {$geoNear:{
      near:{type:"Point", coordinates:[-73.97,40.78]},
      distanceField:"distance",
      maxDistance:2000,
      spherical:true,
      query:{type:"park"}
    }}
  ]).toArray();
  printjson(result);
'
```