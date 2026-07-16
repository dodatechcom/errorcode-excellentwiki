---
title: "GKE: Cluster Is Currently Unusable"
description: "GKE: Cluster is currently unusable — Fix Google Kubernetes Engine cluster health errors."
cloud: ["gcp"]
error-types: ["api-error"]
severities: ["error"]
tags: ["gcp", "gke", "kubernetes", "cluster", "unusable", "node-pool", "control-plane"]
weight: 5
---

The `Cluster is currently unusable` error occurs when a GKE cluster enters a degraded state where it cannot schedule or run workloads. This may be caused by control plane issues, node pool failures, or networking misconfiguration.

## Common Causes

- Control plane is in a `RECONCILING` state (upgrades, maintenance)
- Node pool has zero healthy nodes
- Network policy blocks pod-to-pod communication
- Insufficient quota for node pool resources
- The cluster's VPC network is misconfigured

## How to Fix

Check cluster status:

```bash
gcloud container clusters describe my-cluster \
  --zone=us-central1-a \
  --format="value(status, currentMasterVersion, currentNodeVersion)"
```

Check node pool health:

```bash
gcloud container node-pools list \
  --cluster=my-cluster \
  --zone=us-central1-a \
  --format="table(name, status, config.machineType, initialNodeCount)"
```

Check node health:

```bash
kubectl get nodes -o wide
kubectl describe node <node-name>
```

Repair or recreate the node pool:

```bash
# Delete and recreate the node pool
gcloud container node-pools delete default-pool \
  --cluster=my-cluster \
  --zone=us-central1-a \
  --quiet

gcloud container node-pools create default-pool \
  --cluster=my-cluster \
  --zone=us-central1-a \
  --num-nodes=3 \
  --machine-type=e2-medium
```

Check control plane logs:

```bash
gcloud container operations list --filter="TYPE:UPGRADE_MASTER"
gcloud container operations describe <operation-id>
```

## Examples

- Cluster shows `RUNNING` but all nodes are `NotReady` after a kernel panic
- Control plane upgrade is stuck in `RECONCILING` for more than 30 minutes
- Node pool autoscaler cannot add nodes because the project has reached the CPU quota

## Related Errors

- [GCP Quota Exceeded]({{< relref "/cloud/gcp/quota-exceeded2" >}}) — quota limits.
- [GCP Network Error]({{< relref "/cloud/gcp/network-error" >}}) — network connectivity issues.
- [Azure AKS Error]({{< relref "/cloud/azure/aks-error" >}}) — Azure equivalent.
