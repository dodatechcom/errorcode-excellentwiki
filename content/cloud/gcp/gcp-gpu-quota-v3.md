---
title: "[Solution] GCP GPU Quota"
description: "GPUQuotaError for GPUs."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `GPU Quota` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- GPU quota not enough in zone
- GPU not available in this zone
- GPU requires specific machine types

## How to Fix

### Check GPUs

```bash
gcloud compute accelerator-types list
```

## Examples

- Example scenario: gpu quota not enough in zone
- Example scenario: gpu not available in this zone
- Example scenario: gpu requires specific machine types

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
