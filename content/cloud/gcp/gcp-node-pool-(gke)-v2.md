---
title: "[Solution] GCP Node Pool (GKE)"
description: "GKENodePoolError for node pools."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Node Pool (GKE)` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Pool name taken
- Node version mismatch with control plane
- Machine type not available

## How to Fix

### Create node pool

```bash
gcloud container node-pools create myPool --cluster=myCluster --num-nodes=3
```

## Examples

- Example scenario: pool name taken
- Example scenario: node version mismatch with control plane
- Example scenario: machine type not available

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
