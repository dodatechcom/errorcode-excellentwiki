---
title: "[Solution] GCP Cloud Storage Transfer"
description: "StorageTransferError for transfer jobs."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Cloud Storage Transfer` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Transfer job already exists with name
- Source/destination not accessible
- Schedule overlap detected

## How to Fix

### Create job

```bash
gcloud transfer jobs create ...
```

## Examples

- Example scenario: transfer job already exists with name
- Example scenario: source/destination not accessible
- Example scenario: schedule overlap detected

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
