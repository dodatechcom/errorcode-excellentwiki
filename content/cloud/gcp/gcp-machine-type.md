---
title: "[Solution] GCP Machine Type"
description: "MachineTypeError for machine types."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Machine Type` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Machine type not available in zone
- GPU requires specific machine types
- Custom machine type constraints

## How to Fix

### List types

```bash
gcloud compute machine-types list
```

## Examples

- Example scenario: machine type not available in zone
- Example scenario: gpu requires specific machine types
- Example scenario: custom machine type constraints

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
