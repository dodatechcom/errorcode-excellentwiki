---
title: "[Solution] GCP Bucket Create Error"
description: "BucketCreateError for creation."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Bucket Create Error` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Global uniqueness violated
- Location constraint conflict
- Bucket already exists in another project

## How to Fix

### Create bucket

```bash
gsutil mb gs://my-bucket
```

## Examples

- Example scenario: global uniqueness violated
- Example scenario: location constraint conflict
- Example scenario: bucket already exists in another project

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
