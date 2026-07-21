---
title: "[Solution] GCP Object Not Found"
description: "ObjectNotFound for GCS objects."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Object Not Found` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Object name/path incorrect
- Object deleted or archived
- Version not specified

## How to Fix

### List objects

```bash
gsutil ls gs://my-bucket/path/
```

## Examples

- Example scenario: object name/path incorrect
- Example scenario: object deleted or archived
- Example scenario: version not specified

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
