---
title: "[Solution] GCP Cloud Storage Object Not Found"
description: "NoSuchKey when the specified object does not exist."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Cloud Storage Object Not Found` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Object path is incorrect
- Object was deleted
- Object in different bucket
- Object version ID is wrong

## How to Fix

### List objects

```bash
gsutil ls gs://my-bucket/
```
### Check object

```bash
gsutil stat gs://my-bucket/file.txt
```
### Download object

```bash
gsutil cp gs://my-bucket/file.txt ./local.txt
```

## Examples

- Object at path/to/file.txt referenced but not found
- Object was deleted with versioning

## Related Errors

- [GCS Error]({{< relref "/cloud/gcp/gcp-storage-error" >}}) -- General Storage errors
- [Bucket Not Found]({{< relref "/cloud/gcp/gcs-bucket-not-found" >}}) -- Bucket not found
