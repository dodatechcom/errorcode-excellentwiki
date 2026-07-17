---
title: "[Solution] GKE — cluster upgrade failed"
description: "Fix GKE cluster upgrade failed. Resolve Google Kubernetes Engine upgrade and version issues."
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

A GKE cluster upgrade failed error means the Kubernetes master or node pool upgrade could not complete. The cluster may be stuck in an upgrade or rolled back to the previous version.

## What This Error Means

GKE upgrades involve updating the control plane (master) and then the node pools. Each step can fail independently. The control plane upgrade is managed by Google and cannot be rolled back, while node pool upgrades can fail due to capacity issues, PDB violations, or node configuration errors. When an upgrade fails, the cluster may be in a partially upgraded state where the control plane is at a new version but nodes are still at the old version.

## Common Causes

- Node pool upgrade blocked by PodDisruptionBudgets
- Insufficient capacity in the target zone for new node VMs
- Workload identity or node config incompatible with new version
- Cluster add-ons (VPC CNI, monitoring) failing to upgrade
- Regional vs zonal cluster upgrade coordination issues
- Custom node image incompatible with target Kubernetes version

## How to Fix

### Check Cluster Status

```bash
gcloud container clusters describe my-cluster \
  --zone us-central1-a \
  --query='[currentMasterVersion,currentNodeVersion,status]'
```

### Check Upgrade Status

```bash
gcloud container operations list \
  --filter="operationType=UPGRADE_CLUSTER" \
  --limit=5
```

### Describe Operation

```bash
gcloud container operations describe <operation-id>
```

### Check Node Pool Status

```bash
gcloud container node-pools list \
  --cluster my-cluster \
  --zone us-central1-a
```

### Monitor Upgrade Progress

```bash
gcloud container clusters describe my-cluster \
  --zone us-central1-a \
  --format="value(status)"
watch -n 10 "gcloud container clusters describe my-cluster --zone us-central1-a --format='value(status)'"
```

### Start Upgrade Manually

```bash
# Upgrade control plane
gcloud container clusters upgrade my-cluster \
  --zone us-central1-a \
  --master

# Upgrade node pool
gcloud container clusters upgrade my-cluster \
  --zone us-central1-a \
  --node-pool default-pool
```

### Check for PDB Conflicts

```bash
kubectl get pdb --all-namespaces
kubectl describe pdb <pdb-name>
```

### Upgrade to Specific Version

```bash
gcloud container clusters upgrade my-cluster \
  --zone us-central1-a \
  --cluster-version 1.29.3
```

## Related Errors

- [Kubernetes Node NotReady]({{< relref "/tools/kubernetes/k8s-node-not-ready-v2" >}}) — node unhealthy
- [AWS EKS Error]({{< relref "/cloud/aws/aws-eks-error-v2" >}}) — EKS health check failed
- [Azure AKS Error]({{< relref "/cloud/azure/azure-aks-error-v2" >}}) — node pool not ready
