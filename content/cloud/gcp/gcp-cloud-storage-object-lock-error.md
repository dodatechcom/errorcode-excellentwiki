---
title: "[Solution] GCP Cloud Storage Object Lock Error"
description: "Fix Cloud Storage object lock errors. Resolve object retention, WORM compliance, and immutable storage issues in Google Cloud Storage."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Cloud Storage Object Lock Error

The Cloud Storage Object Lock error occurs when object retention or WORM (Write Once Read Many) policies prevent object modification or deletion.

## Common Causes

- Object has a retention period that has not expired
- Bucket has object lock enabled preventing deletion
- Object is in a legal hold status
- Retention policy is at the bucket level blocking all changes
- Object generation mismatch during update

## How to Fix

### 1. Check object retention
```bash
gsutil stat gs://BUCKET/OBJECT
```

### 2. View bucket retention policy
```bash
gsutil retention get gs://BUCKET_NAME
```

### 3. Remove legal hold
```bash
gsutil retention TEMPORARYHOLD OFF gs://BUCKET_NAME/OBJECT
```

### 4. Check object lock status
```bash
gsutil object lock info gs://BUCKET_NAME
```

## Examples

### Set object retention period
```bash
gsutil retention set 30d gs://BUCKET_NAME/OBJECT
```

### Remove retention (only if expired)
```bash
gsutil retention clear gs://BUCKET_NAME/OBJECT
```

## Related Errors

- [GCP Object Retention]({{< relref "/cloud/gcp/gcp-object-retention" >}})
- [GCP Storage Error]({{< relref "/cloud/gcp/gcp-storage-error" >}})
