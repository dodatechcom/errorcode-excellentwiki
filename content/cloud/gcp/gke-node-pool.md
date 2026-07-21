---
title: "[Solution] GCP GKE Node Pool Error"
description: "NodePoolError when node pool operations fail."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `GKE Node Pool Error` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Node pool name is incorrect
- Node pool is in a failed state
- Node count exceeds maximum
- Node pool VM size not available

## How to Fix

### Check node pool

```bash
gcloud container node-pools describe my-pool --cluster my-cluster --zone us-central1-a
```
### List node pools

```bash
gcloud container node-pools list --cluster my-cluster --zone us-central1-a
```
### Scale node pool

```bash
gcloud container clusters resize my-cluster --num-nodes 5 --node-pool my-pool --zone us-central1-a
```

## Examples

- Node pool in failed state due to VM allocation failure
- Scaling beyond vCPU limit

## Related Errors

- [GKE Error]({{< relref "/cloud/gcp/gcp-gke-error" >}}) -- General GKE errors
- [Cluster Not Found]({{< relref "/cloud/gcp/gke-cluster-not-found" >}}) -- Cluster not found
