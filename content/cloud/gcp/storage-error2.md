---
title: "GCP Cloud Storage: The Bucket Does Not Exist"
description: "Cloud Storage: The bucket does not exist — Fix Google Cloud Storage bucket lookup errors."
cloud: ["gcp"]
error-types: ["api-error"]
severities: ["error"]
tags: ["gcp", "storage", "gcs", "bucket", "not-found", "cloud-storage"]
weight: 5
---

The `The bucket does not exist` error occurs when a Google Cloud Storage API call references a bucket that does not exist in the project or is not accessible to the caller. This is the GCS equivalent of S3's `NoSuchBucket`.

## Common Causes

- The bucket name is incorrect (GCS bucket names are globally unique and must be lowercase)
- The bucket was deleted and the reference is stale
- The bucket is in a different project than the one currently active
- The caller lacks `storage.buckets.get` permission

## How to Fix

List buckets in the current project:

```bash
gsutil ls -p my-project
# Or
gcloud storage buckets list --project=my-project
```

Check if a specific bucket exists:

```bash
gsutil ls -b gs://my-bucket
# Or
gcloud storage buckets describe gs://my-bucket
```

Create the bucket if it does not exist:

```bash
gcloud storage buckets create gs://my-unique-bucket-name \
  --location=us-central1 \
  --storage-class=STANDARD
```

Check permissions:

```bash
gcloud storage buckets get-iam-policy gs://my-bucket
```

## Examples

- gsutil command fails with `BucketNotFoundException: 404 gs://my-bucket` after the bucket was deleted
- Code uses `my-bucket` but the actual bucket is `my-unique-bucket-12345`
- Bucket is in project `prod-project` but `gcloud` is configured for `staging-project`

## Related Errors

- [GCP Permission Denied]({{< relref "/cloud/gcp/permission-denied10" >}}) — permission issues.
- [GCP Quota Exceeded]({{< relref "/cloud/gcp/quota-exceeded2" >}}) — quota limits.
- [AWS S3 AccessDenied]({{< relref "/cloud/aws/s3-access-denied2" >}}) — S3 equivalent.
