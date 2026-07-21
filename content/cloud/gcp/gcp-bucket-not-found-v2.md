---
title: "[Solution] GCP Bucket Not Found"
description: "BucketNotFound for GCS buckets."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Bucket Not Found` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Bucket name incorrect
- Deleted by admin
- Not globally unique

## How to Fix

### List buckets

```bash
gsutil ls
```

## Examples

- Example scenario: bucket name incorrect
- Example scenario: deleted by admin
- Example scenario: not globally unique

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
