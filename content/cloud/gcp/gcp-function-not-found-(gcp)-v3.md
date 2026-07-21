---
title: "[Solution] GCP Function Not Found (GCP)"
description: "GCFunctionNotFound for Cloud Functions."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Function Not Found (GCP)` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Function name incorrect
- Region mismatch
- Deleted by admin

## How to Fix

### List functions

```bash
gcloud functions list
```

## Examples

- Example scenario: function name incorrect
- Example scenario: region mismatch
- Example scenario: deleted by admin

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
