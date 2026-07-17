---
title: "[Solution] GCP Cloud Storage — bucket not found"
description: "Fix Cloud Storage bucket not found. Resolve GCS bucket access and permission issues."
cloud: ["gcp"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["gcp", "storage", "bucket", "not-found", "gcs", "access", "object"]
weight: 5
---

A Cloud Storage bucket not found error means the specified bucket does not exist, or the caller lacks the `storage.buckets.get` permission. The storage operation cannot proceed.

## What This Error Means

Google Cloud Storage buckets are globally named and project-scoped. When a client attempts to access a bucket, GCS validates both existence and permissions. A "not found" (HTTP 404) can mean the bucket truly does not exist, while "access denied" (HTTP 403) means the bucket exists but the caller lacks permission. The confusing part is that GCS may return 404 instead of 403 if the caller lacks `storage.buckets.get` — this is a security measure to avoid leaking bucket existence information to unauthorized callers.

## Common Causes

- Bucket name is misspelled (bucket names are globally unique)
- Bucket is in a different project than the one being used
- Bucket was deleted
- Caller lacks `storage.buckets.get` permission
- Object path within the bucket is incorrect
- Bucket lifecycle policy deleted the bucket
- Uniform bucket-level access enabled without proper IAM

## How to Fix

### List Buckets

```bash
gsutil ls -p my-project
```

### Check Bucket Exists

```bash
gsutil ls -b gs://my-bucket
gsutil stat gs://my-bucket
```

### Check Permissions

```bash
gsutil iam get gs://my-bucket
```

### Grant Bucket Access

```bash
gsutil iam ch user:admin@example.com:objectViewer gs://my-bucket
```

### Create Missing Bucket

```bash
gsutil mb -l us-central1 gs://my-new-bucket
```

### List Objects in Bucket

```bash
gsutil ls gs://my-bucket/
gsutil ls gs://my-bucket/path/to/object
```

### Grant Project-Level Permission

```bash
gcloud projects add-iam-policy-binding my-project \
  --member="user:admin@example.com" \
  --role="roles/storage.objectViewer"
```

### Test with Service Account

```bash
gcloud auth activate-service-account --key-file=key.json
gsutil ls gs://my-bucket
```

### Check Bucket Location

```bash
gsutil ls -L gs://my-bucket | grep Location
```

## Related Errors

- [GCP IAM Error]({{< relref "/cloud/gcp/gcp-iam-error-v2" >}}) — permission denied
- [AWS S3 Error]({{< relref "/cloud/aws/aws-s3-error-v2" >}}) — S3 access denied
- [Azure Storage Error]({{< relref "/cloud/azure/azure-storage-error-v2" >}}) — authentication failed
