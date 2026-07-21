---
title: "[Solution] GCP Bucket Policy (GCS)"
description: "BucketPolicyError for access."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Bucket Policy (GCS)` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Policy too large (>25KB)
- Member not found
- Role not supported on buckets

## How to Fix

### Get policy

```bash
gsutil iam get gs://my-bucket
```

## Examples

- Example scenario: policy too large (>25kb)
- Example scenario: member not found
- Example scenario: role not supported on buckets

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
