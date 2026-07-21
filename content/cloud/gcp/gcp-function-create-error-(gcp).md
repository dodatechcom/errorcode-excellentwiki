---
title: "[Solution] GCP Function Create Error (GCP)"
description: "GCFunctionCreateError for creation."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Function Create Error (GCP)` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Function name taken (per region)
- Bucket not found for source code
- Runtime not supported

## How to Fix

### Create function

```bash
gcloud functions deploy myFunction --runtime=python311 --trigger-http --entry-point=hello
```

## Examples

- Example scenario: function name taken (per region)
- Example scenario: bucket not found for source code
- Example scenario: runtime not supported

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
