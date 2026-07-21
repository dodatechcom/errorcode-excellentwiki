---
title: "[Solution] GCP Cloud Storage Bucket Versioning Error"
description: "Fix Cloud Storage bucket versioning errors. Resolve versioning configuration, lifecycle, and object retention issues in Google Cloud Storage."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Cloud Storage Bucket Versioning Error

The Cloud Storage Bucket Versioning error occurs when versioning operations fail due to configuration conflicts, lifecycle rules, or bucket policy restrictions.

## Common Causes

- Bucket has object retention policies that conflict with versioning
- Lifecycle rules delete all versions causing data loss
- Uniform bucket-level access blocks object-level versioning
- Bucket was created with versioning disabled and cannot re-enable
- KMS key access prevents version operations

## How to Fix

### 1. Enable versioning
```bash
gsutil versioning set on gs://BUCKET_NAME
```

### 2. Check current versioning status
```bash
gsutil versioning get gs://BUCKET_NAME
```

### 3. Set lifecycle rules for old versions
```bash
cat > lifecycle.json << EOF
{
  "rule": [
    {
      "action": {"type": "Delete"},
      "condition": {"age": 90, "isLive": false}
    }
  ]
}
EOF
gsutil lifecycle set lifecycle.json gs://BUCKET_NAME
```

### 4. Remove conflicting retention policy
```bash
gsutil retention clear gs://BUCKET_NAME
```

## Examples

### List object versions
```bash
gsutil ls -a gs://BUCKET_NAME/path/to/object
```

### Restore a previous version
```bash
gsutil cp gs://BUCKET_NAME/object#1234567890 gs://BUCKET_NAME/object
```

## Related Errors

- [GCP Bucket Policy GCS]({{< relref "/cloud/gcp/gcp-bucket-policy-(gcs)" >}})
- [GCP Object Retention]({{< relref "/cloud/gcp/gcp-object-retention" >}})
