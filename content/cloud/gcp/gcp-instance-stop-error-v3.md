---
title: "[Solution] GCP Instance Stop Error"
description: "InstanceStopError for stopping."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Instance Stop Error` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Instance already stopped
- Sole-tenant node maintenance
- Local SSD attached prevents stop

## How to Fix

### Stop instance

```bash
gcloud compute instances stop myVM
```

## Examples

- Example scenario: instance already stopped
- Example scenario: sole-tenant node maintenance
- Example scenario: local ssd attached prevents stop

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
