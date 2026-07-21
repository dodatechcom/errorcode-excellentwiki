---
title: "[Solution] GCP Object Retention"
description: "ObjectRetentionError for retention."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Object Retention` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Retention policy not set on bucket
- Object locked (non-removable)
- Retention duration insufficient

## How to Fix

### Set retention

```bash
gsutil retention set 1d gs://my-bucket/object.txt
```

## Examples

- Example scenario: retention policy not set on bucket
- Example scenario: object locked (non-removable)
- Example scenario: retention duration insufficient

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
