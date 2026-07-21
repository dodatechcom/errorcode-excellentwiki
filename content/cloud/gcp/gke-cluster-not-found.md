---
title: "[Solution] GCP GKE Cluster Not Found"
description: "NOT_FOUND when the specified GKE cluster does not exist."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `GKE Cluster Not Found` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Cluster name is incorrect
- Cluster was deleted
- Cluster in different project
- Cluster in different zone/region

## How to Fix

### List clusters

```bash
gcloud container clusters list
```
### Check cluster

```bash
gcloud container clusters describe my-cluster --zone us-central1-a
```
### Create cluster

```bash
gcloud container clusters create my-cluster --zone us-central1-a --num-nodes 3
```

## Examples

- Cluster my-cluster not found in zone us-central1-a
- Cluster deleted but kubectl still configured

## Related Errors

- [GKE Error]({{< relref "/cloud/gcp/gcp-gke-error" >}}) -- General GKE errors
- [Node Pool]({{< relref "/cloud/gcp/gke-node-pool" >}}) -- Node pool
