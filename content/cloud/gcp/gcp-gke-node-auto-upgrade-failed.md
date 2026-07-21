---
title: "[Solution] GCP GKE Node Auto-Upgrade Failed"
description: "Fix GKE node auto-upgrade failures. Troubleshoot node pool upgrades, version skew policies, and cluster health issues in GCP GKE."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP GKE Node Auto-Upgrade Failed

The GKE Node Auto-Upgrade Failed error occurs when automatic node pool upgrades cannot complete due to misconfiguration, resource constraints, or incompatibilities.

## Common Causes

- Pod disruption budget prevents node draining
- Insufficient cluster capacity for rescheduling pods
- Custom node configuration conflicts with upgrade
- Node pool version skew policy is too strict
- Regional upgrade exceeds resource availability

## How to Fix

### 1. Check node pool upgrade status
```bash
gcloud container operations list --filter="type=UPGRADE_NODE_POOL"
```

### 2. Manually drain and upgrade a node
```bash
gcloud container node-pools update NODE_POOL_NAME \
  --cluster=CLUSTER_NAME \
  --zone=ZONE \
  --image-type=COS_CONTAINERD
```

### 3. Verify PDB constraints
```bash
kubectl get pdb -A
```

### 4. Set maintenance window
```bash
gcloud container clusters update CLUSTER_NAME \
  --maintenance-window-start="2025-01-01T02:00:00Z" \
  --maintenance-window-end="2025-01-01T06:00:00Z" \
  --maintenance-window-recurrence="FREQ=WEEKLY;BYDAY=SA"
```

### 5. Force node pool upgrade
```bash
gcloud container node-pools upgrade NODE_POOL_NAME \
  --cluster=CLUSTER_NAME \
  --zone=ZONE
```

## Examples

### Check upgrade operation details
```bash
gcloud container operations describe OPERATION_NAME --zone=ZONE
```

### Set version skew policy
```bash
gcloud container node-pools update default-pool \
  --cluster=CLUSTER_NAME \
  --zone=ZONE \
  --max-surge-upgrade=1 \
  --max-unavailable-upgrade=0
```

## Related Errors

- [GCP GKE Error]({{< relref "/cloud/gcp/gcp-gke-error" >}})
- [GCP GKE Upgrade]({{< relref "/cloud/gcp/gcp-gke-upgrade" >}})
