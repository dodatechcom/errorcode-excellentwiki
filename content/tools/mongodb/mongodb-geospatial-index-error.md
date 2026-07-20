---
title: "[Solution] MongoDB Geospatial Index Error"
description: "Fix MongoDB geospatial index creation and query errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Geospatial Index Error

Geospatial operations fail with various errors:

```
MongoServerError: can't use legacy geo queries (use 2d index): ...
```

```
MongoServerError: longitude must be between -180 and 180, got: 200
```

## Common Causes

- The location data has invalid coordinates (e.g., longitude > 180)
- The wrong index type is used (`2d` vs `2dsphere`)
- Query operators do not match the index type
- The coordinate pair is in the wrong order (lat/lng vs lng/lat)
- The field contains non-GeoJSON data

## How to Fix

### 1. Use the correct index type for your data

```javascript
// For GeoJSON data (recommended)
db.places.createIndex({ location: "2dsphere" });

// For legacy coordinate pairs (flat 2D space)
db.places.createIndex({ location: "2d" });
```

### 2. Store location as GeoJSON

```javascript
await db.places.insertOne({
  name: "Central Park",
  location: {
    type: "Point",
    coordinates: [-73.97, 40.78]  // [longitude, latitude]
  }
});
```

### 3. Validate coordinates

```javascript
function validateGeoJSON(doc) {
  if (doc.coordinates[0] < -180 || doc.coordinates[0] > 180) {
    throw new Error("Invalid longitude: " + doc.coordinates[0]);
  }
  if (doc.coordinates[1] < -90 || doc.coordinates[1] > 90) {
    throw new Error("Invalid latitude: " + doc.coordinates[1]);
  }
}
```

### 4. Use the correct query operators

```javascript
// For 2dsphere index
db.places.find({
  location: {
    $geoWithin: {
      $centerSphere: [[-73.97, 40.78], 1 / 6378.1]  // 1km radius
    }
  }
});
```

## Examples

```bash
# Create a geospatial collection
mongosh --eval '
  db.places.drop();
  db.places.createIndex({location: "2dsphere"});
  db.places.insertMany([
    {name:"Times Square", location:{type:"Point", coordinates:[-73.9857, 40.7580]}},
    {name:"Central Park", location:{type:"Point", coordinates:[-73.9654, 40.7829]}},
    {name:"Brooklyn Bridge", location:{type:"Point", coordinates:[-73.9969, 40.7061]}}
  ]);
  let near = db.places.find({
    location: {$near: {$geometry:{type:"Point",coordinates:[-73.97,40.78]}, $maxDistance: 5000}}
  }).toArray();
  print("Nearby places:", near.map(p => p.name));
'
```