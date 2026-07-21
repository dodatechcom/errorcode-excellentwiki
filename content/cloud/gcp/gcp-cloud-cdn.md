---
title: "[Solution] GCP Cloud CDN"
description: "CDNError for Cloud CDN."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Cloud CDN` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Backend bucket not found
- Cache key policy invalid
- Signed URL key mismatch

## How to Fix

### Enable CDN

```bash
gcloud compute backend-buckets create myBucket --gcs-bucket-name=myBucket --enable-cdn
```

## Examples

- Example scenario: backend bucket not found
- Example scenario: cache key policy invalid
- Example scenario: signed url key mismatch

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
