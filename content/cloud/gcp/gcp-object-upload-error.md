---
title: "[Solution] GCP Object Upload Error"
description: "ObjectUploadError for uploads."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Object Upload Error` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Bucket not writable (permissions)
- Object size > 5 TB limit
- Checksum mismatch

## How to Fix

### Upload object

```bash
gsutil cp file.txt gs://my-bucket/
```

## Examples

- Example scenario: bucket not writable (permissions)
- Example scenario: object size > 5 tb limit
- Example scenario: checksum mismatch

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
