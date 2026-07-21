---
title: "[Solution] GCP Function Permissions (GCP)"
description: "GCFunctionPermissionError for permissions."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Function Permissions (GCP)` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Invoker role not granted
- Service account lacks permissions
- VPC connector not authorized

## How to Fix

### Add invoker

```bash
gcloud functions add-iam-policy-binding myFunction --member=allUsers --role=roles/cloudfunctions.invoker
```

## Examples

- Example scenario: invoker role not granted
- Example scenario: service account lacks permissions
- Example scenario: vpc connector not authorized

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
