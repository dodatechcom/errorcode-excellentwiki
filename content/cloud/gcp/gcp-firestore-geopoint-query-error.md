---
title: "[Solution] GCP Firestore Geopoint Query Error"
description: "Fix Firestore geopoint query errors. Resolve GeoPoint, geolocation, and compound query issues in Google Cloud Firestore."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Firestore Geopoint Query Error

The Firestore Geopoint Query error occurs when queries using GeoPoint fields fail due to missing composite indexes or incorrect query construction.

## Common Causes

- GeoPoint queries require a composite index that was not created
- Query chains inequality filters on different fields
- GeoPoint is stored as a map instead of a GeoPoint type
- Query attempts unsupported range operations on GeoPoint
- Field type mismatch between stored data and query filter

## How to Fix

### 1. Create composite index for geo queries
```bash
gcloud firestore indexes composite create \
  --collection-id=locations \
  --field-config=name=geopoint,order=ascending \
  --field-config=name=status,order=ascending
```

### 2. Check index build status
```bash
gcloud firestore indexes composite list \
  --collection-id=locations \
  --project=PROJECT_ID --format="table(name,state)"
```

### 3. Use GeoPoint type correctly
```python
from google.cloud.firestore_v1 import GeoPoint
doc_ref = db.collection("locations").document("place1")
doc_ref.set({
    "name": "Central Park",
    "location": GeoPoint(40.785091, -73.968285)
})
```

### 4. Query with GeoPoint
```python
query = db.collection("locations").where(
    "location", "==", GeoPoint(40.785091, -73.968285)
)
```

## Examples

### Store location data
```python
from google.cloud.firestore_v1 import GeoPoint

locations = [
    {"name": "Park", "location": GeoPoint(40.78, -73.96)},
    {"name": "Museum", "location": GeoPoint(40.77, -73.97)},
]
for loc in locations:
    db.collection("locations").add(loc)
```

### Query locations by proximity
```python
from google.cloud import firestore
import math

def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * \
        math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    return R * 2 * math.asin(math.sqrt(a))
```

## Related Errors

- [GCP Firestore Error]({{< relref "/cloud/gcp/gcp-firestore-error" >}})
- [GCP Firestore Index Error]({{< relref "/cloud/gcp/gcp-firestore-index-error" >}})
