---
title: "[Solution] GCP GKE Autopilot"
description: "GKEAutopilotError for Autopilot."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `GKE Autopilot` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Autopilot not available in region
- GPUs require node pool (not Autopilot)
- Resource limits not respected

## How to Fix

### Create Autopilot

```bash
gcloud container clusters create-auto myCluster --region=us-central1
```

## Examples

- Example scenario: autopilot not available in region
- Example scenario: gpus require node pool (not autopilot)
- Example scenario: resource limits not respected

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
