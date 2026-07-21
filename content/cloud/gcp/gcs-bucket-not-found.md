---
title: "[Solution] GCP Cloud Storage Bucket Not Found"
description: "NoSuchBucket when the specified bucket does not exist."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Cloud Storage Bucket Not Found` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Bucket name is incorrect
- Bucket was deleted
- Bucket in different project
- Bucket is in a different location

## How to Fix

### List buckets

```bash
gsutil ls
```
### Check bucket

```bash
gsutil ls -L gs://my-bucket
```
### Create bucket

```bash
gsutil mb -l us-central1 gs://my-new-bucket
```

## Examples

- Bucket my-bucket not found (check name)
- Bucket deleted but still referenced in code

## Related Errors

- [GCS Error]({{< relref "/cloud/gcp/gcp-storage-error" >}}) -- General Storage errors
- [Object Not Found]({{< relref "/cloud/gcp/gcs-object-not-found" >}}) -- Object not found
