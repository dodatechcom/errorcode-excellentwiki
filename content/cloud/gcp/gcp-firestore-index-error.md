---
title: "[Solution] GCP Firestore Index Error"
description: "Fix Firestore composite index errors. Resolve index creation, query performance, and index build failures in Google Cloud Firestore."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Firestore Index Error

The Firestore Index error occurs when composite or single-field indexes fail to build or queries require indexes that do not exist.

## Common Causes

- Query requires a composite index that has not been created
- Index build is still in progress (BUILDING state)
- Too many field combinations hit the index limit per collection
- Firestore TTL deletes documents before index build completes
- Incompatible field values for indexing (nested arrays)

## How to Fix

### 1. Check index status
```bash
gcloud firestore indexes list --collection-id=COLLECTION \
  --project=PROJECT_ID --format="table(name,state)"
```

### 2. Create a composite index
```bash
gcloud firestore indexes composite create \
  --collection-id=COLLECTION \
  --field-config=name=FIELD1,order=ascending \
  --field-config=name=FIELD2,order=descending \
  --project=PROJECT_ID
```

### 3. Check build progress
```bash
gcloud firestore indexes composite describe INDEX_ID \
  --collection-id=COLLECTION \
  --project=PROJECT_ID
```

### 4. Use index auto-creation
```bash
# Run the query once -- Firestore will create the needed index
# Follow the link in the error message to create it
```

## Examples

### Create single-field index
```bash
gcloud firestore indexes composite create \
  --collection-id=users \
  --field-config=name=age,order=ascending \
  --field-config=name=name,order=ascending
```

### View all indexes
```bash
gcloud firestore indexes composite list \
  --project=PROJECT_ID \
  --format="yaml(collectionId,fields)"
```

## Related Errors

- [GCP Firestore Error]({{< relref "/cloud/gcp/gcp-firestore-error" >}})
- [GCP Database Firestore]({{< relref "/cloud/gcp/gcp-database-(firestore)" >}})
